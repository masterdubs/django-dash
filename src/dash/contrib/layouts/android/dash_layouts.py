__all__ = ('AndroidLayout')

from dash.base import BaseDashboardLayout, BaseDashboardPlaceholder, layout_registry


class AndroidMainPlaceholder(BaseDashboardPlaceholder):
    """
    Main placeholder.
    """
    uid = 'main'
    cols = 6
    rows = 5
    cell_width = 150
    cell_height = 110


class AndroidShortcutsPlaceholder(BaseDashboardPlaceholder):
    """
    Shortcuts placeholder.
    """
    uid = 'shortcuts'
    cols = 1
    rows = 10
    cell_width = 60
    cell_height = 55


class AndroidLayout(BaseDashboardLayout):
    """
    Android layout.
    """
    uid = 'android'
    name = 'Android'
    view_template_name = 'android/view_layout.html'
    edit_template_name = 'android/edit_layout.html'
    placeholders = [AndroidMainPlaceholder, AndroidShortcutsPlaceholder]
    cell_units = 'px'
    media_css = (
        'css/dash_dotted_borders.css',
        'css/dash_layout_android.css',
    )
    #media_js = ('js/dash_layout_android.js',)


layout_registry.register(AndroidLayout)
