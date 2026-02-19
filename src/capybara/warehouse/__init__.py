"""
Warehouse abstraction layer.

Provides abstract base class for warehouse implementations and
concrete implementations for various warehouse engines.
"""

from capybara.warehouse.base import Warehouse

__all__ = ["Warehouse"]
