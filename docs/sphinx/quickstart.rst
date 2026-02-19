Quick Start
===========

This guide will help you get started with CaPybara quickly.

Basic Usage
-----------

Here's a simple example of using CaPybara to introspect a warehouse schema:

.. code-block:: python

   from capybara.warehouse.fabric import FabricWarehouse

   # Create a warehouse connection
   warehouse = FabricWarehouse(connection_string="your_connection_string")

   # Connect to the warehouse
   status = warehouse.connect()
   print(status)

   # Introspect the schema
   schema = warehouse.introspect_schema()

   # Get information about tables
   for table_name, table in schema.tables.items():
       print(f"Table: {table_name}")
       print(f"  Columns: {len(table.columns)}")
       print(f"  Primary Keys: {len(table.get_primary_keys())}")

   # Infer relationships
   relationships = warehouse.infer_relationships(schema)
   print(f"Found {len(relationships.relationships)} relationships")

   # Generate a diagram
   diagram = warehouse.export_diagram(schema, format="mermaid")
   print(diagram)

Next Steps
----------

* Read the :doc:`architecture` guide to understand the system design
* Explore the :doc:`api/index` for detailed API documentation
* Check out the :doc:`examples` for more use cases
