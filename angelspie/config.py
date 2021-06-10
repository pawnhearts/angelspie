from functools import partial
from pathlib import Path

import yaml



from .logic import kb, bindings, If, Then, rebind

import gi
gi.require_version('Wnck', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('Gtk', '3.0')
gi.require_version('Keybinder', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Wnck, Gtk, Keybinder, Gdk, GObject


CONFIG_EXAMPLE = '''
click_with_F1:
  if:
    key: F1
  then:
    click: 3

print_debug:
  if:
      event:
  then:
    debug:

win_changed:
  if:
    event: active_window_changed
  then:
    echo: "window changed {name} {class_group}"

switched_to_xterm:
  if:
    name:
      contains: mc
    class_group: XTerm
  then:
    - disable: win_changed
    - trigger: print_debug

timer_test:
  if:
    event: timer 5.0
  then:
    echo: tick


need_F1_outside_mc:
  if:
    or:
      class_group:
        ne: xterm
      name:
        contains_not: mc
  then:
    - sh: date

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

    cfg = yaml.load(path.open(), Loader=yaml.FullLoader)
    rules = {}


    if isinstance(cfg, list):
        cfg = convert_config_from_old_version(cfg)

    for rule_name, rule in cfg.items():
        then = Then(rule.get('then', {}), rule_name, rules)
        cond = If(rule.get('if', {}), then, rule_name, rules)
        rules[rule_name] = cond
        if cond.event == 'active_window_changed':
            scr.connect(cond.event, partial(cond._cb, 'active_window_changed'))
        if cond.event.startswith('timer'):
            secs = float(cond.event.split()[1])
            GObject.timeout_add_seconds(secs, cond._cb, cond.event)
    if bindings:
        scr.connect('active_window_changed', rebind)

    return rules

