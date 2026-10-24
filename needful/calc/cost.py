"""Rekenkern: pure Python, geen I/O, volledig getest.

Voorbeeld uit de pitch: €149 · 3× per jaar · 4 jaar → €12,42 per gebruik.
"""


def cost_per_use(price: float, uses_per_year: int, years: int) -> float:
    """Kost per gebruik in euro, afgerond op 2 cijfers."""
    if price <= 0:
        raise ValueError("price moet groter zijn dan 0")
    total_uses = uses_per_year * years
    if total_uses <= 0:
        raise ValueError("aantal gebruiken moet groter zijn dan 0")
    return round(price / total_uses, 2)
