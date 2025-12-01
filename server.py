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
def check_category(category: str) -> dict:
    """
    Check if a category exists in the valid categories list.

    Args:
        category: The category string to check (e.g., "Gem/Cuisson/Divers")

    Returns:
        A dict with 'exists' (bool) and 'category' (str) fields
    """
    exists = category in CATEGORIES
    return {
        "exists": exists,
        "category": category,
        "message": f"Category '{category}' {'exists' if exists else 'does not exist'} in the list.",
    }


if __name__ == "__main__":
    mcp.run()

