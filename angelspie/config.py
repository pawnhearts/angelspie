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


CONFIG_EXAMPLE = '''
click_with_F1:
  if:
    key: F1
  then::
    click: 3

print_debug:
  if:
    event: active_window_changed
  then:
    debug:

need_F1_in_mc:
  if:
    name:
      contains: mc
    class_group: xterm
  then:
    - disable: click_with_F1

need_F1_outside_mc:
  if:
    any:
      class_group:
        ne: xterm
      name:
        not:
          contains: mc
  then:
    - enable: click_with_F1

'''


def convert_config_from_old_version(cfg):
    return {f'rule{i}': rule for i, rule in enumerate(cfg)}



def loadconf(path='~/.angelspie.yaml'):
    path = Path(path).expanduser()
    scr = Wnck.Screen.get_default()
    kb.init()
    path = path.expanduser()
    if not path.exists():
        path.write_text(CONFIG_EXAMPLE)

    rules = yaml.load(path.open(), Loader=yaml.FullLoader)

    if isinstance(rules, list):
        rules = convert_config_from_old_version(rules)

    for rule_name, rule in rules.items():
        then = Then(rule.get('then', {}))
        cond = If(rule.get('if', {}), then, rule_name)
        if cond.event != 'key_pressed':
            scr.connect(cond.event, partial(cond._cb, 'active_window_changed'))
    if bindings:
        scr.connect('active_window_changed', rebind)

