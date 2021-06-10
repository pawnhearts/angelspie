import inspect

import gi
gi.require_version('Wnck', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('Gtk', '3.0')
gi.require_version('Keybinder', '3.0')
from gi.repository import Gdk, Wnck, Keybinder, Gtk

try:
    from .xtest import get_mouse_pos
except ModuleNotFoundError:
    get_mouse_pos = None

wnck_screen = Wnck.Screen.get_default()
gdk_screen = Gdk.Screen.get_default()


# This module contains autogenerated code


class IfWindow:
    @staticmethod
    def mouse_x():
        ''' Mouse x '''
        return get_mouse_pos()[0]
    @staticmethod
    def mouse_y():
        ''' Mouse y '''
        return get_mouse_pos()[1]
    @staticmethod
    def name():
        ''' Active window name '''
        if w := wnck_screen.get_active_window():
            return w.get_name()
        return ''
    @staticmethod
    def class_group():
        ''' Active window class group name'''
        if w := wnck_screen.get_active_window():
            return w.get_class_group_name()
        return ''
    @staticmethod
    def app():
        ''' Application name '''
        if w := wnck_screen.get_active_window():
            if a := w.get_application():
                return a.get_name()
        return ''
    @staticmethod
    def desktop():
        ''' Return desktop number '''
        return wnck_screen.get_active_workspace() and wnck_screen.get_active_workspace().get_number() or ''

    @staticmethod
    def is_skip_tasklist():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().is_skip_tasklist() or 0 )

    @staticmethod
    def is_fullscreen():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().is_fullscreen() or 0 )

    @staticmethod
    def is_pinned():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().is_pinned() or 0 )

    @staticmethod
    def is_minimized():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().is_minimized() or 0 )

    @staticmethod
    def is_above():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().is_above() or 0 )

    @staticmethod
    def is_floating():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().is_floating() or 0 )

    @staticmethod
    def is_below():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().is_below() or 0 )

    @staticmethod
    def is_maximized():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().is_maximized() or 0 )

    @staticmethod
    def is_maximized_vertically():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().is_maximized_vertically() or 0 )

    @staticmethod
    def is_shaded():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().is_shaded() or 0 )

    @staticmethod
    def icon_is_fallback():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().get_icon_is_fallback() or 0 )

    @staticmethod
    def is_active():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().is_active() or 0 )

    @staticmethod
    def is_sticky():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().is_sticky() or 0 )

    @staticmethod
    def is_most_recently_activated():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().is_most_recently_activated() or 0 )

    @staticmethod
    def is_skip_pager():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().is_skip_pager() or 0 )

    @staticmethod
    def transient_is_most_recently_activated():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().transient_is_most_recently_activated() or 0 )

    @staticmethod
    def is_maximized_horizontally():
        return int( wnck_screen.get_active_window() and wnck_screen.get_active_window().is_maximized_horizontally() or 0 )

    @staticmethod
    def composited():
        return int( gdk_screen.get_active_window() and gdk_screen.get_active_window().get_composited() or 0 )

    @staticmethod
    def pass_through():
        return int( gdk_screen.get_active_window() and gdk_screen.get_active_window().get_pass_through() or 0 )

    @staticmethod
    def event_compression():
        return int( gdk_screen.get_active_window() and gdk_screen.get_active_window().get_event_compression() or 0 )

    @staticmethod
    def is_visible():
        return int( gdk_screen.get_active_window() and gdk_screen.get_active_window().is_visible() or 0 )

    @staticmethod
    def is_shaped():
        return int( gdk_screen.get_active_window() and gdk_screen.get_active_window().is_shaped() or 0 )

    @staticmethod
    def is_viewable():
        return int( gdk_screen.get_active_window() and gdk_screen.get_active_window().is_viewable() or 0 )

    @staticmethod
    def accept_focus():
        return int( gdk_screen.get_active_window() and gdk_screen.get_active_window().get_accept_focus() or 0 )

    @staticmethod
    def modal_hint():
        return int( gdk_screen.get_active_window() and gdk_screen.get_active_window().get_modal_hint() or 0 )

    @staticmethod
    def support_multidevice():
        return int( gdk_screen.get_active_window() and gdk_screen.get_active_window().get_support_multidevice() or 0 )

    @staticmethod
    def is_floating():
        return int( gdk_screen.get_active_window() and gdk_screen.get_active_window().is_floating() or 0 )

    @staticmethod
    def is_input_only():
        return int( gdk_screen.get_active_window() and gdk_screen.get_active_window().is_input_only() or 0 )

    @staticmethod
    def focus_on_map():
        return int( gdk_screen.get_active_window() and gdk_screen.get_active_window().get_focus_on_map() or 0 )

    @staticmethod
    def is_destroyed():
        return int( gdk_screen.get_active_window() and gdk_screen.get_active_window().is_destroyed() or 0 )

    @staticmethod
    def session_id():
        return wnck_screen.get_active_window() and wnck_screen.get_active_window().get_session_id() or ''

    @staticmethod
    def role():
        return wnck_screen.get_active_window() and wnck_screen.get_active_window().get_role() or ''

    @staticmethod
    def xid():
        return wnck_screen.get_active_window() and wnck_screen.get_active_window().get_xid() or ''

    @staticmethod
    def session_id_utf8():
        return wnck_screen.get_active_window() and wnck_screen.get_active_window().get_session_id_utf8() or ''

    @staticmethod
    def class_group_name():
        if w := wnck_screen.get_active_window():
            return w.get_class_group_name()
        return ''

    @staticmethod
    def pid():
        return wnck_screen.get_active_window() and wnck_screen.get_active_window().get_pid() or ''

    @staticmethod
    def group_leader():
        return wnck_screen.get_active_window() and wnck_screen.get_active_window().get_group_leader() or ''

    @staticmethod
    def icon_name():
        return wnck_screen.get_active_window() and wnck_screen.get_active_window().get_icon_name() or ''

    @staticmethod
    def width():
        return gdk_screen.get_active_window() and gdk_screen.get_active_window().get_width() or ''

    @staticmethod
    def origin():
        return gdk_screen.get_active_window() and gdk_screen.get_active_window().get_origin() or ''

    @staticmethod
    def height():
        return gdk_screen.get_active_window() and gdk_screen.get_active_window().get_height() or ''

    @staticmethod
    def scale_factor():
        return gdk_screen.get_active_window() and gdk_screen.get_active_window().get_scale_factor() or ''


class WnckWindowActions:
    def minimize(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().minimize() or ''

    def make_below(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().make_below() or ''

    def make_above(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().make_above() or ''

    def unmake_below(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().unmake_below() or ''

    def maximize(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().maximize() or ''

    def unshade(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().unshade() or ''

    def pin(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().pin() or ''

    def set_sort_order(self, arg):
        order = arg.split()
        order = int(order)
        wnck_screen.get_active_window() and wnck_screen.get_active_window().set_sort_order(order) or ''

    def stick(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().stick() or ''

    def set_fullscreen(self, arg):
        fullscreen = arg.split()
        wnck_screen.get_active_window() and wnck_screen.get_active_window().set_fullscreen(fullscreen) or ''

    def set_geometry(self, arg):
        gravity, geometry_mask, x, y, width, height = arg.split()
        gravity = getattr(Wnck.WindowGravity, "gravity") if not gravity.isnumeric() else int(gravity)
        geometry_mask = getattr(Wnck.WindowMoveResizeMask, "geometry_mask") if not geometry_mask.isnumeric() else int(
            geometry_mask)
        x = int(x)
        y = int(y)
        width = int(width)
        height = int(height)
        wnck_screen.get_active_window() and wnck_screen.get_active_window().set_geometry(gravity, geometry_mask, x, y, width, height) or ''

    def maximize_vertically(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().maximize_vertically() or ''

    def set_skip_pager(self, arg):
        skip = arg.split()
        wnck_screen.get_active_window() and wnck_screen.get_active_window().set_skip_pager(skip) or ''

    def set_icon_geometry(self, arg):
        x, y, width, height = arg.split()
        x = int(x)
        y = int(y)
        width = int(width)
        height = int(height)
        wnck_screen.get_active_window() and wnck_screen.get_active_window().set_icon_geometry(x, y, width, height) or ''

    def unpin(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().unpin() or ''

    def activate(self, arg):
        timestamp = arg.split()
        timestamp = int(timestamp)
        wnck_screen.get_active_window() and wnck_screen.get_active_window().activate(timestamp) or ''

    def unminimize(self, arg):
        timestamp = arg.split()
        timestamp = int(timestamp)
        wnck_screen.get_active_window() and wnck_screen.get_active_window().unminimize(timestamp) or ''

    def move_to_workspace(self, arg):
        space = arg.split()
        space = getattr(Wnck.Workspace, "space") if not space.isnumeric() else int(space)
        wnck_screen.get_active_window() and wnck_screen.get_active_window().move_to_workspace(space) or ''

    def set_window_type(self, arg):
        wintype = arg.split()
        wintype = getattr(Wnck.WindowType, "wintype") if not wintype.isnumeric() else int(wintype)
        wnck_screen.get_active_window() and wnck_screen.get_active_window().set_window_type(wintype) or ''

    def maximize_horizontally(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().maximize_horizontally() or ''

    def close(self, arg):
        timestamp = arg.split()
        timestamp = int(timestamp)
        wnck_screen.get_active_window() and wnck_screen.get_active_window().close(timestamp) or ''

    def unstick(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().unstick() or ''

    def unmaximize(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().unmaximize() or ''

    def unmake_above(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().unmake_above() or ''

    def shade(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().shade() or ''

    def unmaximize_horizontally(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().unmaximize_horizontally() or ''

    def set_skip_tasklist(self, arg):
        skip = arg.split()
        wnck_screen.get_active_window() and wnck_screen.get_active_window().set_skip_tasklist(skip) or ''

    def unmaximize_vertically(self, arg):
        wnck_screen.get_active_window() and wnck_screen.get_active_window().unmaximize_vertically() or ''


for name, func in inspect.getmembers(WnckWindowActions):
    if not name.startswith('_'):
        func.__doc__ = getattr(Wnck.Window, name).__doc__


class GdkWindowActions:
    def set_group(self, arg):
        leader = arg.split()
        leader = getattr(Gdk.Window, "leader") if not leader.isnumeric() else int(leader)
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_group(leader) or ''

    def show_unraised(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().show_unraised() or ''

    def fullscreen(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().fullscreen() or ''

    def move_to_rect(self, arg):
        rect, rect_anchor, window_anchor, anchor_hints, rect_anchor_dx, rect_anchor_dy = arg.split()
        rect = getattr(Gdk.Rectangle, "rect") if not rect.isnumeric() else int(rect)
        rect_anchor = getattr(Gdk.Gravity, "rect_anchor") if not rect_anchor.isnumeric() else int(rect_anchor)
        window_anchor = getattr(Gdk.Gravity, "window_anchor") if not window_anchor.isnumeric() else int(window_anchor)
        anchor_hints = getattr(Gdk.AnchorHints, "anchor_hints") if not anchor_hints.isnumeric() else int(anchor_hints)
        rect_anchor_dx = int(rect_anchor_dx)
        rect_anchor_dy = int(rect_anchor_dy)
        gdk_screen.get_active_window() and gdk_screen.get_active_window().move_to_rect(rect, rect_anchor, window_anchor, anchor_hints, rect_anchor_dx, rect_anchor_dy)

    def raise_(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().raise_() or ''

    def set_geometry_hints(self, arg):
        geometry, geom_mask = arg.split()
        geometry = getattr(Gdk.Geometry, "geometry") if not geometry.isnumeric() else int(geometry)
        geom_mask = getattr(Gdk.WindowHints, "geom_mask") if not geom_mask.isnumeric() else int(geom_mask)
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_geometry_hints(geometry, geom_mask) or ''

    def set_skip_pager_hint(self, arg):
        skips_pager = arg.split()
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_skip_pager_hint(skips_pager) or ''

    def move(self, arg):
        x, y = arg.split()
        x = int(x)
        y = int(y)
        gdk_screen.get_active_window() and gdk_screen.get_active_window().move(x, y) or ''

    def set_title(self, arg):
        title = arg.split()
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_title(title) or ''

    def iconify(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().iconify() or ''

    def maximize(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().maximize() or ''

    def withdraw(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().withdraw() or ''

    def set_type_hint(self, arg):
        hint = arg.split()
        hint = getattr(Gdk.WindowTypeHint, "hint") if not hint.isnumeric() else int(hint)
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_type_hint(hint) or ''

    def set_skip_taskbar_hint(self, arg):
        skips_taskbar = arg.split()
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_skip_taskbar_hint(skips_taskbar) or ''

    def hide(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().hide() or ''

    def stick(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().stick() or ''

    def show(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().show() or ''

    def set_functions(self, arg):
        functions = arg.split()
        functions = getattr(Gdk.WMFunction, "functions") if not functions.isnumeric() else int(functions)
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_functions(functions) or ''

    def destroy(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().destroy() or ''

    def set_icon_name(self, arg):
        name = arg.split()
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_icon_name(name) or ''

    def set_composited(self, arg):
        composited = arg.split()
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_composited(composited) or ''

    def set_keep_below(self, arg):
        setting = arg.split()
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_keep_below(setting) or ''

    def set_accept_focus(self, arg):
        accept_focus = arg.split()
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_accept_focus(accept_focus) or ''

    def set_role(self, arg):
        role = arg.split()
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_role(role) or ''

    def set_opacity(self, arg):
        opacity = arg.split()
        opacity = float(opacity)
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_opacity(opacity) or ''

    def resize(self, arg):
        width, height = arg.split()
        width = int(width)
        height = int(height)
        gdk_screen.get_active_window() and gdk_screen.get_active_window().resize(width, height) or ''

    def beep(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().beep() or ''

    def unfullscreen(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().unfullscreen() or ''

    def set_modal_hint(self, arg):
        modal = arg.split()
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_modal_hint(modal) or ''

    def focus(self, arg):
        timestamp = arg.split()
        timestamp = int(timestamp)
        gdk_screen.get_active_window() and gdk_screen.get_active_window().focus(timestamp) or ''

    def show_window_menu(self, arg):
        event = arg.split()
        event = getattr(Gdk.Event, "event") if not event.isnumeric() else int(event)
        gdk_screen.get_active_window() and gdk_screen.get_active_window().show_window_menu(event) or ''

    def unstick(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().unstick() or ''

    def unmaximize(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().unmaximize() or ''

    def move_resize(self, arg):
        x, y, width, height = arg.split()
        x = int(x)
        y = int(y)
        width = int(width)
        height = int(height)
        gdk_screen.get_active_window() and gdk_screen.get_active_window().move_resize(x, y, width, height) or ''

    def set_fullscreen_mode(self, arg):
        mode = arg.split()
        mode = getattr(Gdk.FullscreenMode, "mode") if not mode.isnumeric() else int(mode)
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_fullscreen_mode(mode) or ''

    def set_keep_above(self, arg):
        setting = arg.split()
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_keep_above(setting) or ''

    def deiconify(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().deiconify() or ''

    def lower(self, arg):
        gdk_screen.get_active_window() and gdk_screen.get_active_window().lower() or ''

    def set_shadow_width(self, arg):
        left, right, top, bottom = arg.split()
        left = int(left)
        right = int(right)
        top = int(top)
        bottom = int(bottom)
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_shadow_width(left, right, top, bottom) or ''

    def set_urgency_hint(self, arg):
        urgent = arg.split()
        gdk_screen.get_active_window() and gdk_screen.get_active_window().set_urgency_hint(urgent) or ''

    def fullscreen_on_monitor(self, arg):
        monitor = arg.split()
        monitor = int(monitor)
        gdk_screen.get_active_window() and gdk_screen.get_active_window().fullscreen_on_monitor(monitor) or ''

    def restack(self, arg):
        sibling, above = arg.split()
        sibling = getattr(Gdk.Window, "sibling") if not sibling.isnumeric() else int(sibling)
        gdk_screen.get_active_window() and gdk_screen.get_active_window().restack(sibling, above) or ''


for name, func in inspect.getmembers(GdkWindowActions):
    if not name.startswith('_'):
        func.__doc__ = getattr(Gdk.Window, name).__doc__
