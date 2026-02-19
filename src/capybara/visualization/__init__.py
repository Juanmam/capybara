"""
Visualization layer for diagram generation.

Provides strategy pattern for generating diagrams in multiple formats:
- PlantUML
- Mermaid
- Future: JSONGraph, HTMLInteractive
"""

from capybara.visualization.base import DiagramStrategy
from capybara.visualization.factory import DiagramStrategyFactory
from capybara.visualization.plantuml import PlantUMLStrategy
from capybara.visualization.mermaid import MermaidStrategy

# Register built-in strategies
DiagramStrategyFactory.register("plantuml", PlantUMLStrategy)
DiagramStrategyFactory.register("mermaid", MermaidStrategy)

__all__ = [
    "DiagramStrategy",
    "DiagramStrategyFactory",
    "PlantUMLStrategy",
    "MermaidStrategy",
]
