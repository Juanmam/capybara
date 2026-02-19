"""
Abstract base class for diagram generation strategies.

Defines the contract for diagram rendering implementations.
"""

from abc import ABC, abstractmethod
from capybara.domain.schema import SchemaGraph


class DiagramStrategy(ABC):
    """Abstract base class for diagram generation strategies.
    
    Each concrete strategy knows how to render a SchemaGraph
    into a specific diagram format (PlantUML, Mermaid, etc.).
    """
    
    @abstractmethod
    def render(self, schema: SchemaGraph) -> str:
        """Render SchemaGraph as diagram string.
        
        Args:
            schema: SchemaGraph to visualize
            
        Returns:
            String representation of diagram in this strategy's format
        """
        pass
    
    @property
    @abstractmethod
    def format_name(self) -> str:
        """Format identifier (e.g., 'plantuml', 'mermaid').
        
        Returns:
            String identifier for this diagram format
        """
        pass
