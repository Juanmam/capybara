"""
Rule registry for managing inference rules.

Allows registration and discovery of inference rules.
"""

from typing import List
from capybara.inference.base import InferenceRule


class RuleRegistry:
    """Registry for managing inference rules.
    
    Provides registration and retrieval of inference rules.
    Rules are automatically sorted by priority when retrieved.
    """
    
    def __init__(self):
        """Initialize empty registry."""
        self._rules: List[InferenceRule] = []
    
    def register(self, rule: InferenceRule) -> None:
        """Register an inference rule.
        
        Args:
            rule: InferenceRule instance to register
        """
        if rule not in self._rules:
            self._rules.append(rule)
    
    def get_rules(self) -> List[InferenceRule]:
        """Get all registered rules, sorted by priority (highest first).
        
        Returns:
            List of InferenceRule instances sorted by priority
        """
        return sorted(self._rules, key=lambda r: r.priority, reverse=True)
    
    def clear(self) -> None:
        """Clear all registered rules."""
        self._rules.clear()
