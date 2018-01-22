# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fluent_contents', '0003_set_mptt_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='BootstrapColumn',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fluent_contents.ContentItem', on_delete=models.CASCADE)),
                ('col_xs', models.PositiveSmallIntegerField(null=True, verbose_name=b'col-xs-', blank=True)),
                ('col_sm', models.PositiveSmallIntegerField(null=True, verbose_name=b'col-sm-', blank=True)),
                ('col_md', models.PositiveSmallIntegerField(null=True, verbose_name=b'col-md-', blank=True)),
                ('col_lg', models.PositiveSmallIntegerField(null=True, verbose_name=b'col-lg-', blank=True)),
                ('col_xs_offset', models.PositiveSmallIntegerField(null=True, verbose_name=b'col-xs-offset-', blank=True)),
                ('col_sm_offset', models.PositiveSmallIntegerField(null=True, verbose_name=b'col-sm-offset-', blank=True)),
                ('col_md_offset', models.PositiveSmallIntegerField(null=True, verbose_name=b'col-md-offset-', blank=True)),
                ('col_lg_offset', models.PositiveSmallIntegerField(null=True, verbose_name=b'col-lg-offset-', blank=True)),
                ('col_xs_push', models.PositiveSmallIntegerField(null=True, verbose_name=b'col-xs-push-', blank=True)),
                ('col_sm_push', models.PositiveSmallIntegerField(null=True, verbose_name=b'col-sm-push-', blank=True)),
                ('col_md_push', models.PositiveSmallIntegerField(null=True, verbose_name=b'col-md-push-', blank=True)),
                ('col_lg_push', models.PositiveSmallIntegerField(null=True, verbose_name=b'col-lg-push-', blank=True)),
            ],
            options={
                'db_table': 'contentitem_fluentcms_bootstrap_grid_bootstrapcolumn',
                'verbose_name': 'Bootstrap Column',
                'verbose_name_plural': 'Bootstrap Columns',
            },
            bases=('fluent_contents.containeritem',),
        ),
        migrations.CreateModel(
            name='BootstrapRow',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fluent_contents.ContentItem', on_delete=models.CASCADE)),
            ],
            options={
                'db_table': 'contentitem_fluentcms_bootstrap_grid_bootstraprow',
                'verbose_name': 'Bootstrap Row',
                'verbose_name_plural': 'Bootstrap Rows',
            },
            bases=('fluent_contents.containeritem',),
        ),
    ]
