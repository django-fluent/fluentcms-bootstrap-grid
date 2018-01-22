fluentcms-bootstrap-grid
========================

.. image:: https://img.shields.io/travis/django-fluent/fluentcms-bootstrap-grid/master.svg?branch=master
    :target: http://travis-ci.org/django-fluent/fluentcms-bootstrap-grid
.. image:: https://img.shields.io/pypi/v/fluentcms-bootstrap-grid.svg
    :target: https://pypi.python.org/pypi/fluentcms-bootstrap-grid/
.. image:: https://img.shields.io/badge/wheel-yes-green.svg
    :target: https://pypi.python.org/pypi/fluentcms-bootstrap-grid/
.. image:: https://img.shields.io/pypi/l/fluentcms-bootstrap-grid.svg
    :target: https://pypi.python.org/pypi/fluentcms-bootstrap-grid/
.. image:: https://img.shields.io/codecov/c/github/django-fluent/fluentcms-bootstrap-grid/master.svg
    :target: https://codecov.io/github/django-fluent/fluentcms-bootstrap-grid?branch=master

Displaying a Bootstrap 3 grid_ in a page.


Installation
============

First install the module, preferably in a virtual environment. It can be installed from PyPI:

.. code-block:: bash

    pip install fluentcms-bootstrap_-rid

First make sure the project is configured for django-fluent-contents_.

Then add the following settings:

.. code-block:: python

    INSTALLED_APPS += (
        'fluentcms_bootstrap_grid',
    )

    FLUENT_CONTENTS_PLACEHOLDER_CONFIG = {
        'slot name': {
            'plugins': ('BootstrapRowPlugin', 'BootstrapColumnPlugin', ...),
        },
    }

The database tables can be created afterwards:

.. code-block:: bash

    ./manage.py migrate


Frontend styling
================

The plugins are renderd with the HTML that Bootstrap prescribes:

.. code-block:: html+django

    <!-- the row that contains multiple columns -->
    <div class="row">

        <!-- a single column -->
        <div class="col-xs-6">
            ..
        </div>

    </div>

The standard Bootstrap 3 CSS will provide the proper styling for this.


Contributing
------------

If you like this module, forked it, or would like to improve it, please let us know!
Pull requests are welcome too. :-)

.. _django-fluent-contents: https://github.com/django-fluent/django-fluent-contents
.. _grid: http://getbootstrap.com/css/#grid
