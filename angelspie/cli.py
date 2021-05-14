"""Console script for ."""
import argparse
import inspect
import sys
from pathlib import Path

import gi
gi.require_version('Wnck', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('Gtk', '3.0')
gi.require_version('Keybinder', '3.0')

from gi.repository import Wnck, Gtk, Keybinder, Gdk, GObject
from .config import loadconf
from .logic import If, Then, Match


def wininfo():
    def cb(*args):
        for k, v in If._vars().items():
            print(f'{k}: {v}')
        sys.exit(0)
    def cb0():
        Wnck.Screen.get_default().connect('active_window_changed', cb)
    GObject.idle_add(cb0)
    Gtk.main()


def help():
    if_help = '\n'.join(f"{k} : {v.__doc__ or k}" for k, v in inspect.getmembers(If) if not k.startswith('_'))
    then_help = '\n'.join(f"{k} : {v.__doc__ or k}" for k, v in inspect.getmembers(Then) if not k.startswith('_'))
    match_help = '\n'.join(f"{k} : {v.__doc__ or k}" for k, v in inspect.getmembers(Match) if not k.startswith('_'))
    print(f''' Config format:
yaml list, each item is an associative array, containing "if" and "then" keys.

Possible keys inside "if" block:
{if_help}

Value could be a string or associative array:
{match_help}

Possible keys inside "then" block:
{then_help}
''')
    sys.exit(0)


def main():
    """Console script for angelspie."""
    parser = argparse.ArgumentParser()
    # parser.add_argument('_', nargs='*')
    parser.add_argument("-c", "--config", help="Path to config file", default=Path('~/.angelspie.yaml'), type=Path)
    parser.add_argument("--help-config", help="Help on config format", const='help', default='main', action='store_const', dest='command')
    parser.add_argument("--win-info", help="Info on window", const='wininfo', default='main', action='store_const', dest='command')
    args = parser.parse_args()
    if args.command == 'help':
        help()
    elif args.command == 'wininfo':
        wininfo()
    else:
        loadconf(args.config)
        Gtk.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
