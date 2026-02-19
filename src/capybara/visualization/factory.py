"""
Factory for creating diagram strategies.

Provides dependency inversion point for diagram generation.
"""

from typing import Type, List
from capybara.visualization.base import DiagramStrategy


class UnsupportedFormatError(Exception):
    """Raised when requested diagram format is not supported."""
    pass


class DiagramStrategyFactory:
    """Factory for creating diagram strategies.
    
    Encapsulates strategy creation logic and provides
    extensibility point for registering new formats.
    """
    
    _strategies: dict[str, Type[DiagramStrategy]] = {}
    
    @classmethod
    def create(cls, format: str) -> DiagramStrategy:
        """Create strategy for given format.
        
        Args:
            format: Format identifier (e.g., "plantuml", "mermaid")
            
        Returns:
            DiagramStrategy instance for the requested format
            
        Raises:
            UnsupportedFormatError: If format not supported
        """
        if format not in cls._strategies:
            raise UnsupportedFormatError(
                f"Format '{format}' not supported. "
                f"Available formats: {list(cls._strategies.keys())}"
            )
        return cls._strategies[format]()
    
    @classmethod
    def register(cls, format: str, strategy_class: Type[DiagramStrategy]) -> None:
        """Register a new strategy (extensibility point).
        
        Args:
            format: Format identifier
            strategy_class: DiagramStrategy subclass
        """
        cls._strategies[format] = strategy_class
    
    @classmethod
    def get_supported_formats(cls) -> List[str]:
        """Get list of supported format identifiers.
        
        Returns:
            List of format names
        """
        return list(cls._strategies.keys())
