import re
from contextlib import contextmanager
from itertools import repeat, chain
import time

import Xlib
from Xlib import X, XK
from Xlib.display import Display
from Xlib.ext.xtest import fake_input
from Xlib.ext import xtest


display = Display()


@contextmanager
def hold_button(key):
    number = display.keysym_to_keycode(XK.string_to_keysym(key))
    display.sync()
    fake_input(display, X.KeyPress, number, X.CurrentTime)
    yield
    fake_input(display, X.KeyRelease, number, X.CurrentTime)
    display.sync()
    display.flush()


def press(key):
    keys = re.findall('([\w\d]+)', key)
    for key, event in chain(zip(keys, repeat(X.KeyPress)), zip(reversed(keys), repeat(X.KeyRelease))):
        number = display.keysym_to_keycode(XK.string_to_keysym(key))
        display.sync()
        fake_input(display, event, number, X.CurrentTime)
        display.sync()
    display.flush()


def click(button=1, x=0, y=0):
    for event in [X.ButtonPress, X.ButtonRelease]:
        display.sync()
        fake_input(display, event, button, X.CurrentTime, X.NONE, x, y)
        display.sync()
        display.flush()


def get_mouse_pos():
    display.sync()
    mpos = display.screen().root.query_pointer()._data
    return mpos['root_x'], mpos['root_y']


def set_mouse_pos(x, y):
    display.screen().root.warp_pointer(x, y)
    display.sync()
    display.flush()
