"""
Domain models for warehouse-agnostic schema representation.

This module contains the core domain objects that represent database
structure independently of any specific warehouse implementation.
"""

from capybara.domain.schema import SchemaGraph, Table, Column
from capybara.domain.relationships import Relationship, RelationshipMap, RelationshipType

__all__ = [
    "SchemaGraph",
    "Table",
    "Column",
    "Relationship",
    "RelationshipMap",
    "RelationshipType",
]
