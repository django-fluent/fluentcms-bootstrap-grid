from django.conf import settings
from django.utils.translation import ugettext_lazy as _

FLUENTCMS_BOOTSTRAP_GRID_COLUMNS = getattr(settings, 'FLUENTCMS_GRID_COLUMNS', 12)
FLUENTCMS_BOOTSTRAP_GRID_SIZES = getattr(settings, 'FLUENTCMS_BOOTSTRAP_GRID_SIZES', ('xs', 'sm', 'md', 'lg'))

FLUENTCMS_BOOTSTRAP_GRID_TITLES = {
    'xs': _("Mobile"),
    'sm': _("Tablet"),
    'md': _("Desktop"),
    'lg': _("Large Display"),
}

FLUENTCMS_BOOTSTRAP_GRID_TITLES.update(getattr(settings, 'FLUENTCMS_BOOTSTRAP_GRID_TITLES', {}))
