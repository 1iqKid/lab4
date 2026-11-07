from __future__ import annotations
from connstans import C_ACTIVE, C_IND, C_SM

def show_menu() -> None:
    print('\n выберите нагрузку:')
    print(' 1 - активная (c = 1.0) ')
    print(' 2 - индуктивная (c = 0.85)')
    print(' 3 - смешанная (c = 0.75 )')

def select_mode() -> float | None:
    while True:
        choice = input('введите номер (от 0 до 3):').strip()
        match choice:
            case '1':
                return C_ACTIVE
            case '2':
                return C_IND
            case '3':
                return C_SM
            case '0':
                return None
            case _:
                print("Ошибка: неверный пункт меню. Повторите ввод.")

def mode_name(c: float) -> str:
    match c:
        case 1.0:
            return "активная"
        case 0.85:
            return "индуктивная"
        case 0.75:
            return "смешанная"
        case _:
            return "неизвестный"
                    