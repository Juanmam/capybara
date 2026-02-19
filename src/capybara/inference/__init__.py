"""
Relationship inference engine.

Provides rule-based relationship inference capabilities to detect
non-trivial relationships beyond explicit foreign key constraints.
"""

from capybara.inference.engine import InferenceEngine
from capybara.inference.base import InferenceRule
from capybara.inference.registry import RuleRegistry

__all__ = ["InferenceEngine", "InferenceRule", "RuleRegistry"]
