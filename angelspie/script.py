import inspect
import re
import time
from functools import partial

from gi.repository import Gdk, Wnck, Keybinder

try:
    from xtest import hold_button, click, key_press
except ModuleNotFoundError:
    pass

scr = Wnck.Screen.get_default()
kb = Keybinder
kb.init()


def window_match(win, **kwargs):
    kmap = {'name': lambda w: w.get_name(), 'application': lambda w: w.get_application().get_name(),
            'class_group': lambda w: w.get_class_group_name()}
    for k, v in kwargs.items():
        val = kmap[k](win)
        if v.startswith('~'):
            if not re.search(v[1:], val):
                return False
        else:
            if v != val:
                return False
    return True


def wait_for_window(**kwargs):
    screen = Wnck.Screen.get_default()
    while True:
        if window_match(screen.get_active_window(), **kwargs):
            return
        time.sleep(0.1)


def get_args(func):
    args = inspect.getargs(func.__code__).args
    arg_map = {'scr': scr, 'win': scr.get_active_window, 'ws': scr.get_active_workspace,
               'app': lambda: scr.get_active_window().get_application(),
               'class_group': lambda: scr.get_active_window().get_class_group()}
    return {arg: arg_map[arg]() for arg in args}


def screen_connect(name, func):
    def cb(*args):
        func(**get_args(func))

    scr.connect(name, cb)


bound_keys = []
bound = set()


def rebind(*args):
    for key in bound:
        kb.unbind(key)
    for condition, key, func in bound_keys:
        if condition(**get_args(condition)):
            bound.add(key)
            kb.bind(key, func)


def key_pressed(key, conditions=None):
    def wrapper(func):
        bound_keys.append((conditions, key, func))
        return func

    return wrapper


for name in ['active_window_changed',
             'active_workspace_changed',
             'application_closed',
             'application_opened',
             'background_changed',
             'class_group_closed',
             'class_group_opened',
             'showing_desktop_changed',
             'viewports_changed',
             'window_closed',
             'window_manager_changed',
             'window_opened',
             'window_stacking_changed',
             'workspace_created',
             'workspace_destroyed']:
    globals()[name] = partial(screen_connect, name)

scr.connect('active_workspace_changed', rebind)
