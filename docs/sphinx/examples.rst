Examples
========

This section provides practical examples of using CaPybara.

Basic Schema Introspection
---------------------------

.. code-block:: python

   from capybara.warehouse.fabric import FabricWarehouse

   warehouse = FabricWarehouse(connection_string="...")
   warehouse.connect()

   schema = warehouse.introspect_schema()

   # List all tables
   for table_name, table in schema.tables.items():
       print(f"{table.schema}.{table.name}")

   # Get columns for a specific table
   table = schema.get_table("dbo.users")
   if table:
       for column in table.columns:
           print(f"  {column.name}: {column.data_type}")

Relationship Inference
----------------------

.. code-block:: python

   from capybara.inference.engine import InferenceEngine
   from capybara.inference.registry import RuleRegistry

   # Create inference engine
   registry = RuleRegistry()
   # Register rules (when implemented)
   engine = InferenceEngine(registry)

   # Infer relationships
   relationships = engine.infer(schema)

   # Find relationships for a table
   table_rels = relationships.get_relationships_for_table("dbo.orders")
   for rel in table_rels:
       print(f"{rel.source_table}.{rel.source_column} -> "
             f"{rel.target_table}.{rel.target_column}")

Diagram Generation
------------------

.. code-block:: python

   # Generate PlantUML diagram
   plantuml_diagram = warehouse.export_diagram(schema, format="plantuml")
   with open("schema.puml", "w") as f:
       f.write(plantuml_diagram)

   # Generate Mermaid diagram
   mermaid_diagram = warehouse.export_diagram(schema, format="mermaid")
   with open("schema.mmd", "w") as f:
       f.write(mermaid_diagram)

Custom Inference Rules
----------------------

.. code-block:: python

   from capybara.inference.base import InferenceRule
   from capybara.domain.schema import SchemaGraph
   from capybara.domain.relationships import Relationship, RelationshipType

   class CustomRule(InferenceRule):
       @property
       def name(self) -> str:
           return "custom_rule"

       @property
       def priority(self) -> int:
           return 100

       def infer(self, schema: SchemaGraph) -> list[Relationship]:
           # Your inference logic here
           return []

   # Register the rule
   registry = RuleRegistry()
   registry.register(CustomRule())
   engine = InferenceEngine(registry)
