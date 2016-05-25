from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from fluent_contents.models import ContainerItem


@python_2_unicode_compatible
class BootstrapRow(ContainerItem):
    """
    Bootstrap 3 row that can host columns
    """

    class Meta:
        verbose_name = _("Bootstrap Row")
        verbose_name_plural = _("Bootstrap Rows")

    def __str__(self):
        return 'row'


@python_2_unicode_compatible
class BootstrapColumn(ContainerItem):
    """
    Bootstrap 3 column
    """
    # Size for mobile/tablet/desktop/large
    col_xs = models.PositiveSmallIntegerField('col-xs-', blank=True, null=True)
    col_sm = models.PositiveSmallIntegerField('col-sm-', blank=True, null=True)
    col_md = models.PositiveSmallIntegerField('col-md-', blank=True, null=True)
    col_lg = models.PositiveSmallIntegerField('col-lg-', blank=True, null=True)

    # Offset
    col_xs_offset = models.PositiveSmallIntegerField('col-xs-offset-', blank=True, null=True)
    col_sm_offset = models.PositiveSmallIntegerField('col-sm-offset-', blank=True, null=True)
    col_md_offset = models.PositiveSmallIntegerField('col-md-offset-', blank=True, null=True)
    col_lg_offset = models.PositiveSmallIntegerField('col-lg-offset-', blank=True, null=True)

    # Enforced location
    col_xs_push = models.PositiveSmallIntegerField('col-xs-push-', blank=True, null=True)
    col_sm_push = models.PositiveSmallIntegerField('col-sm-push-', blank=True, null=True)
    col_md_push = models.PositiveSmallIntegerField('col-md-push-', blank=True, null=True)
    col_lg_push = models.PositiveSmallIntegerField('col-lg-push-', blank=True, null=True)

    class Meta:
        verbose_name = _("Bootstrap Column")
        verbose_name_plural = _("Bootstrap Columns")

    def __str__(self):
        return self.css_classes.replace('col-', '')

    @property
    def css_classes(self):
        """
        Return the CSS classes to add to the column
        """
        classes = []
        sizes = ('xs', 'sm', 'md', 'lg')
        suffixes = ('', '_offset', '_push')
        for size in sizes:
            for suffix in suffixes:
                field = "col_{0}{1}".format(size, suffix)
                value = getattr(self, field)
                if value:
                    classes.append("{0}-{1}".format(field.replace('_', '-'), value))

        return ' '.join(classes)
