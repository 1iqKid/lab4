
from validation import input_napryazh, input_tok
from menu import show_menu, select_mode, mode_name
from operations import moshnost_privoda , napryazh_class


def main() -> None:
    print("=== Расчёт мощности электропривода ===")

    while True:
        show_menu()
        c = select_mode()
        if c is None:
            print("Работа завершена.")
            break

        u = input_napryazh()
        i = input_tok()

        v = moshnost_privoda(u, i, c)
        cls = napryazh_class (u)

        print("\n Результаты ")
        print(f"Режим:        {mode_name(c)} (c = {c})")
        print(f"V (мощность привода):      {v} кВт")
        print(f"класс напряжения: {cls}")
        print("\n")


if __name__ == "__main__":
    main()