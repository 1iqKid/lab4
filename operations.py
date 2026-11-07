from typing import Annotated
from connstans import U_SMALL_LIMIT, U_LARGE_LIMIT



def cutting_speed(
    u: Annotated[float, "значение напряжения, В"],
    i: Annotated[float, "значение тока, А"],
    c: Annotated[float, 'тип нагрузки']
) -> float:
    return u * i * c / 1000.0


def diameter_class(
    d: Annotated[float, "Диаметр, мм"],
) -> str:
    """
    Классифицировать диаметр через if-elif-else.

    D < 10 — малый диаметр;
    10 ≤ D ≤ 100 — нормальный диаметр;
    D > 100 — крупный диаметр.

    Args:
        d: диаметр, мм.

    Returns:
        Строка с названием класса диаметра.
    """
    if d < D_SMALL_LIMIT:
        return "малый диаметр"
    elif d <= D_LARGE_LIMIT:
        return "нормальный диаметр"
    else:
        return "крупный диаметр"