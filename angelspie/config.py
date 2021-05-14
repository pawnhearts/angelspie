from functools import partial
from pathlib import Path

import yaml



from .logic import kb, bindings, If, Then, rebind

import gi
gi.require_version('Wnck', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('Gtk', '3.0')
gi.require_version('Keybinder', '3.0')
from gi.repository import Wnck, Gtk, Keybinder, Gdk



def loadconf(path):
    scr = Wnck.Screen.get_default()
    kb.init()
    path = path.expanduser()
    if not path.exists():
        path.write_text('''- if:
    key: F1
  then::
    click: 3
- then:
    debug:
- if:
    name:
      contains: xterm
  then:
    minimize:
    move: 100 100
''')

    rules = yaml.load(Path('~/.pypie.yaml').expanduser().open(), Loader=yaml.FullLoader)
    for rule in rules:
        then = Then(rule.get('then', {}))
        cond = If(rule.get('if', {}), then)
        if cond.event != 'key_pressed':
            scr.connect(cond.event, partial(cond._cb, 'active_window_changed'))
    if bindings:
        scr.connect('active_window_changed', rebind)

