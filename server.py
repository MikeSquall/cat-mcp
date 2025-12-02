"""
FastMCP server for checking categories.
"""

import json
from pathlib import Path

from fastmcp import FastMCP

mcp = FastMCP("Category Checker")

# Load categories once at startup
CATEGORIES_FILE = Path(__file__).parent / "uniques_categories.json"


def load_categories() -> set[str]:
    """Load categories from JSON file."""
    try:
        with open(CATEGORIES_FILE) as f:
            return set(json.load(f))
    except FileNotFoundError:
        return set()


CATEGORIES = load_categories()


@mcp.tool()
def is_category_valid(category: str) -> bool:
    """
    Check if a category name is in the valid categories list.

    Args:
        category: The category string to check (e.g., "Gem/Cuisson/Divers")

    Returns:
        True if the category name is in the valid categories list, False otherwise
    """
    return category in CATEGORIES


@mcp.tool()
def get_possible_subcategories(category: str) -> list[str]:
    """
    Get all possible subcategories for a given category.

    Args:
        category: The category to get the subcategories for (e.g., "Gem/Cuisson/Divers")

    Returns:
        List of possible subcategories
    """
    return sorted(cat for cat in CATEGORIES if cat.startswith(category))

if __name__ == "__main__":
    mcp.run()
