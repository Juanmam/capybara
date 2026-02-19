"""
Abstract base class for warehouse implementations.

Defines the contract that all warehouse implementations must follow.
"""

from abc import ABC, abstractmethod
from capybara.domain.schema import SchemaGraph
from capybara.domain.relationships import RelationshipMap


class Warehouse(ABC):
    """Abstract base class for warehouse implementations.
    
    This class defines the contract for warehouse operations:
    - Connection management
    - Schema introspection
    - Relationship inference (delegates to InferenceEngine)
    - Diagram export (delegates to DiagramStrategy)
    """
    
    @abstractmethod
    def connect(self) -> str:
        """Establish connection to warehouse.
        
        Returns:
            Connection status message
            
        Raises:
            ConnectionError: If connection fails
        """
        pass
    
    @abstractmethod
    def introspect_schema(self) -> SchemaGraph:
        """Extract schema metadata and build SchemaGraph.
        
        This method queries warehouse-specific metadata tables
        and constructs a warehouse-agnostic SchemaGraph.
        
        Returns:
            SchemaGraph representing warehouse structure
            
        Raises:
            IntrospectionError: If schema extraction fails
        """
        pass
    
    def infer_relationships(self, schema: SchemaGraph) -> RelationshipMap:
        """Infer relationships using rule-based engine.
        
        Default implementation delegates to InferenceEngine.
        Can be overridden for warehouse-specific inference logic.
        
        Args:
            schema: SchemaGraph to analyze
            
        Returns:
            RelationshipMap containing inferred relationships
        """
        # Default implementation will delegate to InferenceEngine
        # This keeps Warehouse layer independent of Inference layer
        # Implementation will be added when InferenceEngine is created
        raise NotImplementedError("InferenceEngine integration pending")
    
    def export_diagram(
        self, 
        schema: SchemaGraph, 
        format: str = "plantuml"
    ) -> str:
        """Generate diagram in specified format.
        
        Delegates to DiagramStrategyFactory to create appropriate
        strategy and render the diagram.
        
        Args:
            schema: SchemaGraph to visualize
            format: Diagram format ("plantuml", "mermaid")
            
        Returns:
            String representation of diagram
            
        Raises:
            UnsupportedFormatError: If format not supported
        """
        # Default implementation will delegate to DiagramStrategyFactory
        # This keeps Warehouse layer independent of Visualization layer
        # Implementation will be added when DiagramStrategyFactory is created
        raise NotImplementedError("DiagramStrategyFactory integration pending")
