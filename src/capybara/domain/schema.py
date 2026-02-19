"""
Schema domain models.

Core domain objects representing database structure:
- SchemaGraph: Central immutable representation
- Table: Represents a database table
- Column: Represents a database column
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class Column:
    """Represents a database column.
    
    Attributes:
        name: Column name
        data_type: Column data type (warehouse-specific string)
        nullable: Whether column allows NULL values
        is_primary_key: Whether column is part of primary key
        is_foreign_key: Whether column is a foreign key
        foreign_key_target: If foreign key, tuple of (target_table, target_column)
    """
    name: str
    data_type: str
    nullable: bool
    is_primary_key: bool = False
    is_foreign_key: bool = False
    foreign_key_target: Optional[tuple[str, str]] = None  # (table, column)
    
    def __post_init__(self):
        """Validate column state."""
        if self.is_foreign_key and self.foreign_key_target is None:
            raise ValueError("Foreign key columns must specify target")


@dataclass(frozen=True)
class Table:
    """Represents a database table.
    
    Attributes:
        name: Table name
        schema: Schema/database name
        columns: List of Column objects
    """
    name: str
    schema: str
    columns: tuple[Column, ...]  # Immutable tuple
    
    @property
    def fully_qualified_name(self) -> str:
        """Return schema.table format."""
        return f"{self.schema}.{self.name}"
    
    def get_column(self, name: str) -> Optional[Column]:
        """Get column by name."""
        return next((col for col in self.columns if col.name == name), None)
    
    def get_primary_keys(self) -> tuple[Column, ...]:
        """Get all primary key columns."""
        return tuple(col for col in self.columns if col.is_primary_key)


@dataclass(frozen=True)
class SchemaGraph:
    """Immutable warehouse-agnostic representation of database schema.
    
    This is the central domain object. All warehouse implementations
    produce SchemaGraph, and all consumers (visualization, inference)
    operate on SchemaGraph.
    
    Attributes:
        tables: Dictionary mapping fully qualified table names to Table objects
        relationships: List of explicit foreign key relationships
    """
    tables: dict[str, Table] = field(default_factory=dict)
    relationships: tuple = field(default_factory=tuple)  # Will be Relationship objects
    
    def get_table(self, name: str) -> Optional[Table]:
        """Get table by fully qualified name."""
        return self.tables.get(name)
    
    def get_tables_by_schema(self, schema: str) -> list[Table]:
        """Get all tables in a schema."""
        return [
            table for table in self.tables.values()
            if table.schema == schema
        ]
    
    def get_columns(self, table_name: str) -> list[Column]:
        """Get all columns for a table."""
        table = self.get_table(table_name)
        return list(table.columns) if table else []
