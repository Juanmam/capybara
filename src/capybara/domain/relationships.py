"""
Relationship domain models.

Represents relationships between tables, both explicit (FK constraints)
and inferred (detected via heuristics).
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class RelationshipType(Enum):
    """Type of relationship."""
    EXPLICIT_FK = "explicit_fk"  # From foreign key constraint
    INFERRED = "inferred"  # Detected via heuristics


@dataclass(frozen=True)
class Relationship:
    """Represents a relationship between tables.
    
    Attributes:
        source_table: Fully qualified source table name
        source_column: Source column name
        target_table: Fully qualified target table name
        target_column: Target column name
        relationship_type: Type of relationship (EXPLICIT_FK or INFERRED)
        confidence: Confidence score (0.0 to 1.0), 1.0 for explicit FKs
    """
    source_table: str
    source_column: str
    target_table: str
    target_column: str
    relationship_type: RelationshipType
    confidence: float = 1.0
    
    def __post_init__(self):
        """Validate relationship."""
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("Confidence must be between 0.0 and 1.0")


@dataclass
class RelationshipMap:
    """Collection of relationships with query capabilities.
    
    Attributes:
        relationships: List of Relationship objects
    """
    relationships: list[Relationship] = field(default_factory=list)
    
    def get_relationships_for_table(self, table: str) -> list[Relationship]:
        """Get all relationships involving a table."""
        return [
            rel for rel in self.relationships
            if rel.source_table == table or rel.target_table == table
        ]
    
    def get_outgoing_relationships(self, table: str) -> list[Relationship]:
        """Get relationships where table is source."""
        return [
            rel for rel in self.relationships
            if rel.source_table == table
        ]
    
    def get_incoming_relationships(self, table: str) -> list[Relationship]:
        """Get relationships where table is target."""
        return [
            rel for rel in self.relationships
            if rel.target_table == table
        ]
    
    def merge(self, other: 'RelationshipMap') -> 'RelationshipMap':
        """Merge with another RelationshipMap, deduplicating."""
        # TODO: Implement deduplication logic
        combined = self.relationships + other.relationships
        return RelationshipMap(relationships=combined)
