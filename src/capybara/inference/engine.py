"""
Inference engine orchestrator.

Applies all registered inference rules to a SchemaGraph
and returns a RelationshipMap with inferred relationships.
"""

from capybara.domain.schema import SchemaGraph
from capybara.domain.relationships import RelationshipMap
from capybara.inference.registry import RuleRegistry


class InferenceEngine:
    """Orchestrates relationship inference.
    
    Applies all registered rules to a SchemaGraph and collects
    inferred relationships into a RelationshipMap.
    """
    
    def __init__(self, registry: RuleRegistry):
        """Initialize inference engine with rule registry.
        
        Args:
            registry: RuleRegistry containing inference rules
        """
        self.registry = registry
    
    def infer(self, schema: SchemaGraph) -> RelationshipMap:
        """Infer relationships from schema using all registered rules.
        
        Args:
            schema: SchemaGraph to analyze
            
        Returns:
            RelationshipMap containing all inferred relationships
        """
        relationships = []
        
        # Get all rules sorted by priority
        rules = self.registry.get_rules()
        
        # Apply each rule
        for rule in rules:
            inferred = rule.infer(schema)
            relationships.extend(inferred)
        
        return RelationshipMap(relationships=relationships)
