Architecture
============

CaPybara is built with a modular, extensible architecture that separates concerns and enables easy extension.

Core Principles
---------------

* **Separation of Concerns**: Discovery, modeling, and visualization are completely separated
* **Warehouse-Agnostic Domain Model**: SchemaGraph is independent of any specific warehouse
* **Strategy Pattern**: Both warehouses and diagram formats use the strategy pattern
* **Extensibility**: New warehouses, formats, and inference rules can be added without refactoring

Architecture Overview
---------------------

The system is organized into four main layers:

Domain Layer
~~~~~~~~~~~~

The domain layer contains warehouse-agnostic models that represent database structure:

* :class:`~capybara.domain.schema.SchemaGraph` - Central immutable representation of schema
* :class:`~capybara.domain.schema.Table` - Represents a database table
* :class:`~capybara.domain.schema.Column` - Represents a database column
* :class:`~capybara.domain.relationships.Relationship` - Represents relationships between tables
* :class:`~capybara.domain.relationships.RelationshipMap` - Collection of relationships

Warehouse Layer
~~~~~~~~~~~~~~~

The warehouse layer provides abstractions for connecting to and introspecting different warehouse engines:

* :class:`~capybara.warehouse.base.Warehouse` - Abstract base class
* :class:`~capybara.warehouse.fabric.FabricWarehouse` - Microsoft Fabric implementation

Inference Layer
~~~~~~~~~~~~~~

The inference layer provides rule-based relationship detection:

* :class:`~capybara.inference.engine.InferenceEngine` - Orchestrates inference
* :class:`~capybara.inference.base.InferenceRule` - Base class for inference rules
* :class:`~capybara.inference.registry.RuleRegistry` - Manages inference rules

Visualization Layer
~~~~~~~~~~~~~~~~~~

The visualization layer generates diagrams in multiple formats:

* :class:`~capybara.visualization.base.DiagramStrategy` - Abstract base class
* :class:`~capybara.visualization.plantuml.PlantUMLStrategy` - PlantUML format
* :class:`~capybara.visualization.mermaid.MermaidStrategy` - Mermaid format
* :class:`~capybara.visualization.factory.DiagramStrategyFactory` - Factory for creating strategies

Data Flow
---------

1. **Connection**: Warehouse connects to the data source
2. **Introspection**: Warehouse queries metadata and builds SchemaGraph
3. **Inference**: InferenceEngine applies rules to detect relationships
4. **Visualization**: DiagramStrategy renders SchemaGraph as diagram text

For detailed architecture documentation, see the :doc:`../ARCHITECTURE` document.
