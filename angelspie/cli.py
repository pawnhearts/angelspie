"""Console script for ."""
import argparse
import inspect
import sys
import os
import random
from pathlib import Path

import yaml
import gi

gi.require_version("Wnck", "3.0")
gi.require_version("Gdk", "3.0")
gi.require_version("Gtk", "3.0")
gi.require_version("Keybinder", "3.0")

from gi.repository import Wnck, Gtk, Keybinder, Gdk, GObject
from .config import loadconf, CONFIG_EXAMPLE
from .logic import If, Then, Match


def wininfo():
    def cb(*args):
        for k, v in If({}, None, "wininfo", {})._vars().items():
            print(f"{k}: {v}")
        sys.exit(0)

    def cb0():
        Wnck.Screen.get_default().connect("active_window_changed", cb)

    GObject.idle_add(cb0)
    Gtk.main()


def addrule():
    def cb(scr, old_win):
        win = scr.get_active_window()
        geo = win.get_geometry()
        rule = {
            f"rule_{random.randint(0, 32768)}": {
                "if": {
                    "name": {"contains": win.get_name()},
                    "class_group": win.get_class_group_name(),
                },
                "then": {
                    "echo": "window {name}",
                    "move": f"{geo[0]} {geo[1]}",
                    "resize": f"{geo[2]} {geo[3]}",
                },
            }
        }
        sys.stdout.write(os.linesep)
        yaml.dump(rule, sys.stdout)
        sys.stdout.write(os.linesep)
        sys.stdout.flush()

        sys.exit(0)

    def cb0():
        Wnck.Screen.get_default().connect("active_window_changed", cb)

    GObject.idle_add(cb0)
    Gtk.main()


def help():
    if_help = "\n".join(
        f"{k} : {v.__doc__ or k}"
        for k, v in inspect.getmembers(If)
        if not k.startswith("_")
    )
    then_help = "\n".join(
        f"{k} : {v.__doc__ or k}"
        for k, v in inspect.getmembers(Then)
        if not k.startswith("_")
    )
    match_help = "\n".join(
        f"{k} : {v.__doc__ or k}"
        for k, v in inspect.getmembers(Match)
        if not k.startswith("_")
    )
    print(
        f""" Config format:

Possible keys inside "if" block:
{if_help}

Value could be a string or associative array:
{match_help}

Possible keys inside "then" block:
{then_help}

Config example:
{CONFIG_EXAMPLE}
"""
    )
    sys.exit(0)


def main():
    """Console script for angelspie."""
    parser = argparse.ArgumentParser()
    # parser.add_argument('_', nargs='*')
    parser.add_argument(
        "-c",
        "--config",
        help="Path to config file",
        default=Path("~/.angelspie.yaml"),
        type=Path,
    )
    parser.add_argument(
        "--help-config",
        help="Help on config format",
        const="help",
        default="main",
        action="store_const",
        dest="command",
    )
    parser.add_argument(
        "--win-info",
        help="Info on window",
        const="wininfo",
        default="main",
        action="store_const",
        dest="command",
    )
    parser.add_argument(
        "--add-rule",
        help="Generate rule",
        const="addrule",
        default="main",
        action="store_const",
        dest="command",
    )
    args = parser.parse_args()
    if args.command == "help":
        help()
    elif args.command == "wininfo":
        wininfo()
    elif args.command == "addrule":
        addrule()
    else:
        loadconf(args.config)
        Gtk.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
