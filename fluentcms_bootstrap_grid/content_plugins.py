from django import forms
from django.utils.encoding import force_text
from django.utils.translation import pgettext, ugettext_lazy as _
from fluent_contents.extensions import ContainerPlugin, plugin_pool, ContentItemForm
from . import appsettings
from .models import BootstrapRow, BootstrapColumn


GRID_COLUMNS = appsettings.FLUENTCMS_BOOTSTRAP_GRID_COLUMNS


def _get_size_choices():
    choices = [('', '----')]
    for i in range(1, GRID_COLUMNS + 1):
        title = '{0} / {1}'.format(i, GRID_COLUMNS)
        choices.append((i, title))
    return choices

SIZE_CHOICES = _get_size_choices()
OFFSET_CHOICES = [('', '----')] + [(i, force_text(i)) for i in range(1, GRID_COLUMNS + 1)]

size_widget = forms.Select(choices=SIZE_CHOICES)
offset_widget = forms.Select(choices=OFFSET_CHOICES)
push_widget = forms.Select(choices=OFFSET_CHOICES)


@plugin_pool.register
class BootstrapRowPlugin(ContainerPlugin):
    """
    Row plugin
    """
    model = BootstrapRow
    render_template = 'fluentcms_bootstrap_grid/row.html'
    empty_children_message = _("Add a new column here.")


class BootstrapColumnForm(ContentItemForm):
    """
    Custom form for the bootstrap column
    """
    def __init__(self, *args, **kwargs):
        super(BootstrapColumnForm, self).__init__(*args, **kwargs)

        for size in appsettings.FLUENTCMS_BOOTSTRAP_GRID_SIZES:
            col = self.fields['col_{0}'.format(size)]
            offset = self.fields['col_{0}_offset'.format(size)]
            push = self.fields['col_{0}_push'.format(size)]

            col.label = appsettings.FLUENTCMS_BOOTSTRAP_GRID_TITLES[size]
            offset.label = pgettext("bootstrap-grid", u"Offset")
            push.label = pgettext("bootstrap-grid", u"Push")


@plugin_pool.register
class BootstrapColumnPlugin(ContainerPlugin):
    """
    Column plugin
    """
    model = BootstrapColumn
    form = BootstrapColumnForm
    render_template = 'fluentcms_bootstrap_grid/column.html'
    allowed_parent_types = (BootstrapRowPlugin,)
    formfield_overrides = {
        'col_xs': {'widget': size_widget},
        'col_sm': {'widget': size_widget},
        'col_md': {'widget': size_widget},
        'col_lg': {'widget': size_widget},
        'col_xs_offset': {'widget': offset_widget},
        'col_sm_offset': {'widget': offset_widget},
        'col_md_offset': {'widget': offset_widget},
        'col_lg_offset': {'widget': offset_widget},
        'col_xs_push': {'widget': push_widget},
        'col_sm_push': {'widget': push_widget},
        'col_md_push': {'widget': push_widget},
        'col_lg_push': {'widget': push_widget},
    }

    fieldsets = (
        (None, {
            'fields': (
                ('col_xs', 'col_xs_offset', 'col_xs_push'),
                ('col_sm', 'col_sm_offset', 'col_sm_push'),
                ('col_md', 'col_md_offset', 'col_md_push'),
                ('col_lg', 'col_lg_offset', 'col_lg_push'),
            ),
        }),
    )

    class Media:
        css = {
            'all': ('admin/fluentcms_bootstrap_grid/grid_admin.css',),
        }
