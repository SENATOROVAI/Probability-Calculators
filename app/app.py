from typing import Tuple, Union


# Union - условная констуркция объединяет 2 типа данных
# Прописание инпуты:
def main() -> Tuple[str, Union[int, str]]:
    """
    Принимает занчения

    Выбор типа события
    """
    event_type = input("Выберите тип события:\n1 - coin\n2 - dice\n")
    while event_type != "1" or event_type != "2":
        if event_type == '1':
            type = "coin"
            break

        elif event_type == '2':
            type = "dice"
            break

        else:
            event_type = input("Повторите попытку ввода значения ЦИФРОЙ:\n1 - coin\n2 - dice\n")

    if event_type == "1":
        event = input("Выбирите сторону монетки:\n1 - O\n2 - P\n")
        while event < "1" or event > "2":
            event = input("Повторите выбор стороны ЦИФРОЙ:\n1 - O\n2 - P\n")
        return type, {"2": "P", "1": "O"}[event]
    else:
        event = input("Выбирите число на кубике:\nОт 1 до 6\n")
        while event > "6" or event < "1":
            event = input("Повторите выбор числа на кубике ЦИФРОЙ:\nОт 1 до 6\n")
        return type, event
