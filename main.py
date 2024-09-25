"""
    AUTHOR:  Robin Trachsel
    VERSION: 1.0
    DATE:    25.09.2024

    DESCRIPTION: This program adjusts the ingredient quantities of a recipe based on the number of people.
"""

import json


def adjust_recipe(recipe_, num_people):
    """
    Adjusts the ingredient quantities based on the number of people.

    Args:
    - recipe: A dictionary representing the original recipe.
    - num_people: The number of people to adjust the recipe for.

    Returns:
    - A dictionary with the adjusted recipe.
    """
    factor = num_people / recipe_["servings"]
    adjusted_ingredients = {
        ingredient: int(quantity * factor)
        for ingredient, quantity in recipe_["ingredients"].items()
    }
    return {
        "title": recipe_["title"],
        "ingredients": adjusted_ingredients,
        "servings": num_people
    }


def load_recipe(json_string):
    """
    Loads a recipe from a JSON string.

    Args:
    - json_string: A JSON string representing the recipe.

    Returns:
    - A dictionary with the loaded recipe.
    """
    return json.loads(json_string)


if __name__ == "__main__":
    # Example usage
    recipe_json = (
        '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, '
        '"Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'
    )
    recipe = load_recipe(recipe_json)
    print("Loaded Recipe:", recipe)
    adjusted_recipe = adjust_recipe(recipe, 2)
    print("Adjusted Recipe:", adjusted_recipe)
