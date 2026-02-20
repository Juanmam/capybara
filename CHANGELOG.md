# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-02-19

### Added

#### Core Architecture
- **Domain Layer**: Warehouse-agnostic domain models
  - `SchemaGraph`: Immutable central domain object representing database structure
  - `Table`: Represents database tables with schema and columns
  - `Column`: Represents database columns with types and constraints
  - `Relationship`: Represents table relationships (explicit FK or inferred)
  - `RelationshipMap`: Collection of relationships with query capabilities
  - `RelationshipType`: Enum for relationship types

- **Warehouse Layer**: Abstraction for warehouse implementations
  - `Warehouse`: Abstract base class defining warehouse operations contract
  - `FabricWarehouse`: Microsoft Fabric warehouse implementation (Phase 1 skeleton)
  - Support for future warehouse implementations (Synapse, Databricks)

- **Inference Layer**: Rule-based relationship detection
  - `InferenceRule`: Abstract base class for inference rules
  - `RuleRegistry`: Manages collection of inference rules
  - `InferenceEngine`: Orchestrates relationship inference
  - Ready for concrete rule implementations (naming heuristics, surrogate keys, semantic matching)

- **Visualization Layer**: Diagram generation with strategy pattern
  - `DiagramStrategy`: Abstract base class for diagram formats
  - `DiagramStrategyFactory`: Factory with dependency inversion
  - `PlantUMLStrategy`: PlantUML ER diagram generation (skeleton)
  - `MermaidStrategy`: Mermaid ER diagram generation (skeleton)
  - Extensible for additional formats

#### Documentation
- Complete Sphinx documentation structure
  - Installation guide
  - Quick start guide
  - Architecture overview
  - API documentation for all modules
  - Usage examples
  - Contributing guidelines

- GitHub Pages integration
  - GitHub Actions workflow for automated documentation builds
  - Automatic deployment on push to main branch

#### Packaging
- PyPI packaging configuration (`pyproject.toml`)
- Modern Python packaging with setuptools
- Development and documentation dependencies
- Tool configurations (black, ruff, mypy, pytest)

### Architecture

This release establishes the foundational architecture for a warehouse introspection and visualization system:

- **Separation of Concerns**: Discovery, modeling, and visualization are completely separated
- **Warehouse-Agnostic Domain Model**: SchemaGraph is independent of any specific warehouse
- **Strategy Pattern**: Both warehouses and diagram formats use the strategy pattern
- **Extensibility**: New warehouses, formats, and inference rules can be added without refactoring

### Known Limitations

- FabricWarehouse connection and schema introspection are not yet implemented (Phase 1 pending)
- Inference rules are not yet implemented (skeleton only)
- Diagram rendering (PlantUML/Mermaid) is not yet implemented (skeleton only)
- Integration between layers (InferenceEngine and DiagramStrategyFactory in Warehouse) is pending

### Notes

This is the initial release (v0.1.0) establishing the architectural foundation. The system is designed for extensibility and future evolution. Core domain models and abstractions are in place, ready for Phase 1 implementation.

[0.1.0]: https://github.com/juanmmejia/capybara/releases/tag/v0.1.0
