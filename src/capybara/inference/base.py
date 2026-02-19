"""
Abstract base class for inference rules.

Defines the contract for relationship inference rules.
"""

from abc import ABC, abstractmethod
from capybara.domain.schema import SchemaGraph
from capybara.domain.relationships import Relationship


class InferenceRule(ABC):
    """Abstract base class for relationship inference rules.
    
    Each rule implements heuristics to detect relationships
    that are not explicitly defined as foreign keys.
    """
    
    @abstractmethod
    def infer(self, schema: SchemaGraph) -> list[Relationship]:
        """Infer relationships from schema.
        
        Args:
            schema: SchemaGraph to analyze
            
        Returns:
            List of inferred relationships with confidence scores
        """
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Rule identifier name."""
        pass
    
    @property
    @abstractmethod
    def priority(self) -> int:
        """Rule priority (higher = applied first).
        
        Rules with higher priority are applied first.
        This allows more specific rules to override general ones.
        """
        pass
