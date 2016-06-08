from django.test import TestCase

from fluent_contents.tests.factories import create_placeholder, create_content_item
from fluent_contents.tests.testapp.models import RawHtmlTestItem
from fluent_contents.tests.utils import render_content_items
from fluentcms_bootstrap_grid.models import BootstrapColumn, BootstrapRow


class ModelTests(TestCase):
    """
    Testing the models
    """

    def test_column_css_classes(self):
        """
        Test how the column CSS classes are generated
        """
        item = BootstrapColumn(
            col_xs=6,
            col_sm_offset=2,
            col_md=3,
            col_md_offset=4,
            col_xs_push=1,
        )
        self.assertEqual(item.css_classes, 'col-xs-6 col-xs-push-1 col-sm-offset-2 col-md-3 col-md-offset-4')

    def test_rendering(self):
        placeholder = create_placeholder()
        row = create_content_item(BootstrapRow, placeholder=placeholder)
        col1 = create_content_item(BootstrapColumn, placeholder=placeholder, parent_item=row, col_xs=6)
        col2 = create_content_item(BootstrapColumn, placeholder=placeholder, parent_item=row, col_xs=6, col_sm=12)
        text = create_content_item(RawHtmlTestItem, placeholder=placeholder, parent_item=col1, html='AA')
        text = create_content_item(RawHtmlTestItem, placeholder=placeholder, parent_item=col2, html='BB')

        items = placeholder.get_content_items()
        self.assertHTMLEqual(render_content_items(items).html, ''
                             '<div class="row">'
                             '<div class="col-xs-6">AA</div>'
                             '<div class="col-sm-12 col-xs-6">BB</div>'
                             '</div>')
