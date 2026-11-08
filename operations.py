from typing import Annotated
from connstans import U_SMALL_LIMIT, U_LARGE_LIMIT



def moshnost_privoda(
    u: Annotated[float, "значение напряжения, В"],
    i: Annotated[float, "значение тока, А"],
    c: Annotated[float, 'тип нагрузки']
) -> float:
    return u * i * c / 1000.0


def napryazh_class(
    d: Annotated[float, "напряжение, кВт"],
) -> str:
    if d < U_SMALL_LIMIT:
        return "низкое напряжение"
    elif d <= U_LARGE_LIMIT:
        return "нормальное напряжение"
    else:
        return "высокое напряжение"