from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()

    ingredients_lower = ingredients.lower()

    valid = any(
        ingredient in ingredients_lower
        for ingredient in allowed
    )

    status = "VALID" if valid else "INVALID"

    return f"{ingredients} - {status}"
