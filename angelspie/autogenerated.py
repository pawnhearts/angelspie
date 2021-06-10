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
    def name(win=None):
        ''' Active window name '''
        if w := (win or wnck_screen.get_active_window()):
            return w.get_name()
        return ''
    @staticmethod
    def class_group(win=None):
        ''' Active window class group name'''
        if w := (win or wnck_screen.get_active_window()):
            return w.get_class_group_name()
        return ''
    @staticmethod
    def app(win=None):
        ''' Application name '''
        if w := (win or wnck_screen.get_active_window()):
            if a := w.get_application():
                return a.get_name()
        return ''
    @staticmethod
    def desktop(win=None):
        ''' Return desktop number '''
        return wnck_screen.get_active_workspace() and wnck_screen.get_active_workspace().get_number() or ''

    @staticmethod
    def is_skip_tasklist(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).is_skip_tasklist() or 0 )

    @staticmethod
    def is_fullscreen(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).is_fullscreen() or 0 )

    @staticmethod
    def is_pinned(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).is_pinned() or 0 )

    @staticmethod
    def is_minimized(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).is_minimized() or 0 )

    @staticmethod
    def is_above(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).is_above() or 0 )

    @staticmethod
    def is_floating(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).is_floating() or 0 )

    @staticmethod
    def is_below(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).is_below() or 0 )

    @staticmethod
    def is_maximized(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).is_maximized() or 0 )

    @staticmethod
    def is_maximized_vertically(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).is_maximized_vertically() or 0 )

    @staticmethod
    def is_shaded(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).is_shaded() or 0 )

    @staticmethod
    def icon_is_fallback(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).get_icon_is_fallback() or 0 )

    @staticmethod
    def is_active(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).is_active() or 0 )

    @staticmethod
    def is_sticky(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).is_sticky() or 0 )

    @staticmethod
    def is_most_recently_activated(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).is_most_recently_activated() or 0 )

    @staticmethod
    def is_skip_pager(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).is_skip_pager() or 0 )

    @staticmethod
    def transient_is_most_recently_activated(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).transient_is_most_recently_activated() or 0 )

    @staticmethod
    def is_maximized_horizontally(win=None):
        return int( (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).is_maximized_horizontally() or 0 )

    @staticmethod
    def composited(win=None):
        return int( (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).get_composited() or 0 )

    @staticmethod
    def pass_through(win=None):
        return int( (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).get_pass_through() or 0 )

    @staticmethod
    def event_compression(win=None):
        return int( (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).get_event_compression() or 0 )

    @staticmethod
    def is_visible(win=None):
        return int( (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).is_visible() or 0 )

    @staticmethod
    def is_shaped(win=None):
        return int( (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).is_shaped() or 0 )

    @staticmethod
    def is_viewable(win=None):
        return int( (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).is_viewable() or 0 )

    @staticmethod
    def accept_focus(win=None):
        return int( (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).get_accept_focus() or 0 )

    @staticmethod
    def modal_hint(win=None):
        return int( (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).get_modal_hint() or 0 )

    @staticmethod
    def support_multidevice(win=None):
        return int( (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).get_support_multidevice() or 0 )

    @staticmethod
    def is_floating(win=None):
        return int( (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).is_floating() or 0 )

    @staticmethod
    def is_input_only(win=None):
        return int( (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).is_input_only() or 0 )

    @staticmethod
    def focus_on_map(win=None):
        return int( (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).get_focus_on_map() or 0 )

    @staticmethod
    def is_destroyed(win=None):
        return int( (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).is_destroyed() or 0 )

    @staticmethod
    def session_id(win=None):
        return (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).get_session_id() or ''

    @staticmethod
    def role(win=None):
        return (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).get_role() or ''

    @staticmethod
    def xid(win=None):
        return (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).get_xid() or ''

    @staticmethod
    def session_id_utf8(win=None):
        return (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).get_session_id_utf8() or ''

    @staticmethod
    def class_group_name(win=None):
        if w := (win or wnck_screen.get_active_window()):
            return w.get_class_group_name()
        return ''

    @staticmethod
    def pid(win=None):
        return (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).get_pid() or ''

    @staticmethod
    def group_leader(win=None):
        return (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).get_group_leader() or ''

    @staticmethod
    def icon_name(win=None):
        return (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).get_icon_name() or ''

    @staticmethod
    def width(win=None):
        return (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).get_width() or ''

    @staticmethod
    def origin(win=None):
        return (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).get_origin() or ''

    @staticmethod
    def height(win=None):
        return (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).get_height() or ''

    @staticmethod
    def scale_factor(win=None):
        return (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).get_scale_factor() or ''


class WnckWindowActions:
    def minimize(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).minimize() or ''

    def make_below(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).make_below() or ''

    def make_above(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).make_above() or ''

    def unmake_below(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).unmake_below() or ''

    def maximize(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).maximize() or ''

    def unshade(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).unshade() or ''

    def pin(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).pin() or ''

    def set_sort_order(self, arg, win=None):
        order = arg.split()
        order = int(order)
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).set_sort_order(order) or ''

    def stick(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).stick() or ''

    def set_fullscreen(self, arg, win=None):
        fullscreen = arg.split()
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).set_fullscreen(fullscreen) or ''

    def set_geometry(self, arg, win=None):
        gravity, geometry_mask, x, y, width, height = arg.split()
        gravity = getattr(Wnck.WindowGravity, "gravity") if not gravity.isnumeric() else int(gravity)
        geometry_mask = getattr(Wnck.WindowMoveResizeMask, "geometry_mask") if not geometry_mask.isnumeric() else int(
            geometry_mask)
        x = int(x)
        y = int(y)
        width = int(width)
        height = int(height)
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).set_geometry(gravity, geometry_mask, x, y, width, height) or ''

    def maximize_vertically(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).maximize_vertically() or ''

    def set_skip_pager(self, arg, win=None):
        skip = arg.split()
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).set_skip_pager(skip) or ''

    def set_icon_geometry(self, arg, win=None):
        x, y, width, height = arg.split()
        x = int(x)
        y = int(y)
        width = int(width)
        height = int(height)
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).set_icon_geometry(x, y, width, height) or ''

    def unpin(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).unpin() or ''

    def activate(self, arg, win=None):
        timestamp = arg.split()
        timestamp = int(timestamp)
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).activate(timestamp) or ''

    def unminimize(self, arg, win=None):
        timestamp = arg.split()
        timestamp = int(timestamp)
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).unminimize(timestamp) or ''

    def move_to_workspace(self, arg, win=None):
        space = arg.split()
        space = getattr(Wnck.Workspace, "space") if not space.isnumeric() else int(space)
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).move_to_workspace(space) or ''

    def set_window_type(self, arg, win=None):
        wintype = arg.split()
        wintype = getattr(Wnck.WindowType, "wintype") if not wintype.isnumeric() else int(wintype)
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).set_window_type(wintype) or ''

    def maximize_horizontally(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).maximize_horizontally() or ''

    def close(self, arg, win=None):
        timestamp = arg.split()
        timestamp = int(timestamp)
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).close(timestamp) or ''

    def unstick(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).unstick() or ''

    def unmaximize(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).unmaximize() or ''

    def unmake_above(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).unmake_above() or ''

    def shade(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).shade() or ''

    def unmaximize_horizontally(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).unmaximize_horizontally() or ''

    def set_skip_tasklist(self, arg, win=None):
        skip = arg.split()
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).set_skip_tasklist(skip) or ''

    def unmaximize_vertically(self, arg, win=None):
        (win or wnck_screen.get_active_window()) and (win or wnck_screen.get_active_window()).unmaximize_vertically() or ''


for name, func in inspect.getmembers(WnckWindowActions):
    if not name.startswith('_'):
        func.__doc__ = getattr(Wnck.Window, name).__doc__


class GdkWindowActions:
    def set_group(self, arg, win=None):
        leader = arg.split()
        leader = getattr(Gdk.Window, "leader") if not leader.isnumeric() else int(leader)
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_group(leader) or ''

    def show_unraised(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).show_unraised() or ''

    def fullscreen(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).fullscreen() or ''

    def move_to_rect(self, arg, win=None):
        rect, rect_anchor, window_anchor, anchor_hints, rect_anchor_dx, rect_anchor_dy = arg.split()
        rect = getattr(Gdk.Rectangle, "rect") if not rect.isnumeric() else int(rect)
        rect_anchor = getattr(Gdk.Gravity, "rect_anchor") if not rect_anchor.isnumeric() else int(rect_anchor)
        window_anchor = getattr(Gdk.Gravity, "window_anchor") if not window_anchor.isnumeric() else int(window_anchor)
        anchor_hints = getattr(Gdk.AnchorHints, "anchor_hints") if not anchor_hints.isnumeric() else int(anchor_hints)
        rect_anchor_dx = int(rect_anchor_dx)
        rect_anchor_dy = int(rect_anchor_dy)
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).move_to_rect(rect, rect_anchor, window_anchor, anchor_hints, rect_anchor_dx, rect_anchor_dy)

    def raise_(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).raise_() or ''

    def set_geometry_hints(self, arg, win=None):
        geometry, geom_mask = arg.split()
        geometry = getattr(Gdk.Geometry, "geometry") if not geometry.isnumeric() else int(geometry)
        geom_mask = getattr(Gdk.WindowHints, "geom_mask") if not geom_mask.isnumeric() else int(geom_mask)
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_geometry_hints(geometry, geom_mask) or ''

    def set_skip_pager_hint(self, arg, win=None):
        skips_pager = arg.split()
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_skip_pager_hint(skips_pager) or ''

    def move(self, arg, win=None):
        x, y = arg.split()
        x = int(x)
        y = int(y)
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).move(x, y) or ''

    def set_title(self, arg, win=None):
        title = arg.split()
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_title(title) or ''

    def iconify(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).iconify() or ''

    def maximize(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).maximize() or ''

    def withdraw(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).withdraw() or ''

    def set_type_hint(self, arg, win=None):
        hint = arg.split()
        hint = getattr(Gdk.WindowTypeHint, "hint") if not hint.isnumeric() else int(hint)
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_type_hint(hint) or ''

    def set_skip_taskbar_hint(self, arg, win=None):
        skips_taskbar = arg.split()
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_skip_taskbar_hint(skips_taskbar) or ''

    def hide(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).hide() or ''

    def stick(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).stick() or ''

    def show(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).show() or ''

    def set_functions(self, arg, win=None):
        functions = arg.split()
        functions = getattr(Gdk.WMFunction, "functions") if not functions.isnumeric() else int(functions)
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_functions(functions) or ''

    def destroy(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).destroy() or ''

    def set_icon_name(self, arg, win=None):
        name = arg.split()
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_icon_name(name) or ''

    def set_composited(self, arg, win=None):
        composited = arg.split()
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_composited(composited) or ''

    def set_keep_below(self, arg, win=None):
        setting = arg.split()
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_keep_below(setting) or ''

    def set_accept_focus(self, arg, win=None):
        accept_focus = arg.split()
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_accept_focus(accept_focus) or ''

    def set_role(self, arg, win=None):
        role = arg.split()
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_role(role) or ''

    def set_opacity(self, arg, win=None):
        opacity = arg.split()
        opacity = float(opacity)
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_opacity(opacity) or ''

    def resize(self, arg, win=None):
        width, height = arg.split()
        width = int(width)
        height = int(height)
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).resize(width, height) or ''

    def beep(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).beep() or ''

    def unfullscreen(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).unfullscreen() or ''

    def set_modal_hint(self, arg, win=None):
        modal = arg.split()
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_modal_hint(modal) or ''

    def focus(self, arg, win=None):
        timestamp = arg.split()
        timestamp = int(timestamp)
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).focus(timestamp) or ''

    def show_window_menu(self, arg, win=None):
        event = arg.split()
        event = getattr(Gdk.Event, "event") if not event.isnumeric() else int(event)
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).show_window_menu(event) or ''

    def unstick(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).unstick() or ''

    def unmaximize(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).unmaximize() or ''

    def move_resize(self, arg, win=None):
        x, y, width, height = arg.split()
        x = int(x)
        y = int(y)
        width = int(width)
        height = int(height)
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).move_resize(x, y, width, height) or ''

    def set_fullscreen_mode(self, arg, win=None):
        mode = arg.split()
        mode = getattr(Gdk.FullscreenMode, "mode") if not mode.isnumeric() else int(mode)
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_fullscreen_mode(mode) or ''

    def set_keep_above(self, arg, win=None):
        setting = arg.split()
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_keep_above(setting) or ''

    def deiconify(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).deiconify() or ''

    def lower(self, arg, win=None):
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).lower() or ''

    def set_shadow_width(self, arg, win=None):
        left, right, top, bottom = arg.split()
        left = int(left)
        right = int(right)
        top = int(top)
        bottom = int(bottom)
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_shadow_width(left, right, top, bottom) or ''

    def set_urgency_hint(self, arg, win=None):
        urgent = arg.split()
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).set_urgency_hint(urgent) or ''

    def fullscreen_on_monitor(self, arg, win=None):
        monitor = arg.split()
        monitor = int(monitor)
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).fullscreen_on_monitor(monitor) or ''

    def restack(self, arg, win=None):
        sibling, above = arg.split()
        sibling = getattr(Gdk.Window, "sibling") if not sibling.isnumeric() else int(sibling)
        (win or gdk_screen.get_active_window()) and (win or gdk_screen.get_active_window()).restack(sibling, above) or ''


for name, func in inspect.getmembers(GdkWindowActions):
    if not name.startswith('_'):
        func.__doc__ = getattr(Gdk.Window, name).__doc__
