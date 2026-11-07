from __future__ import annotations
from connstans import U_MIN, U_MAX, I_MIN, I_MAX
from logger import log_error


def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    if value < low:
        return False, f"Ошибка: значение меньше нижней границы ({low})."
    elif value > high:
        return False, f"Ошибка: значение больше верхней границы ({high})."
    else:
        return True, ""


def input_number(prompt: str, low: float, high: float) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"Ошибка: введено не число ('{raw}'). {msg}"
            print(msg)
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        print(msg + " Повторите ввод.")
        log_error(msg)


def input_napryazh() -> float:
    return input_number(
        "Введите напряжение U, В (12..1000): ",
        U_MIN, U_MAX,
    )


def input_tok() -> float:
    return input_number(
        "Введите значение тока I, А (0.1..500): ",
        I_MIN, I_MAX,
    )