Installation
============

CaPybara can be installed from PyPI using pip:

.. code-block:: bash

   pip install capybara

For development, you can install from source:

.. code-block:: bash

   git clone https://github.com/juanmmejia/capybara.git
   cd capybara
   pip install -e .

Development dependencies can be installed with:

.. code-block:: bash

   pip install -e ".[dev]"

Documentation dependencies can be installed with:

.. code-block:: bash

   pip install -e ".[docs]"

Requirements
------------

CaPybara requires Python 3.8 or higher.

Optional Dependencies
----------------------

Depending on your use case, you may need additional dependencies:

* **pandas** - For pandas DataFrame support
* **polars** - For polars DataFrame support
* **pyspark** - For PySpark DataFrame support
* **fabric** - For Microsoft Fabric warehouse support

These are not included by default to keep the core library lightweight. Install them as needed:

.. code-block:: bash

   pip install pandas polars pyspark
