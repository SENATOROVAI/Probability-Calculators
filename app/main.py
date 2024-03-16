# одключаем ядро

# Прописание инпуты:
def get_value():
    """
    Принимает занчения
    
    Выбор типа события 
    """
    event_type = int(input("Выберите тип события:\n1 - coin\n2 - dice\n"))
    while event_type != 1 or event_type !=2: 
        if event_type == 1:
            type =  'coin'
            break

        elif event_type == 2:
            type =  'dice'
            break

        else:
            event_type =  int(input('Повторите попытку ввода значения:\n1 - coin\n2 - dice\n'))
    
    if event_type == 1:
        event = int(input('Выбирите сторону монетки:\n1 - O\n2 - P\n'))
        while event < 1 or event > 2:
            event = int(input('Повторите выбор стороны:\n1 - O\n2 - P\n'))
        return type, {2: 'P', 1: 'O'}[event]
    else:
        event = int(input('Выбирите число на кубике:\nОт 1 до 6\n'))
        while event > 6 or event < 1:
            event = int(input('Повторите выбор числа на кубике:\nОт 1 до 6\n'))
        return type, event
# def get():
#     b = get_value()
#     return b   
# print(get())
# print(get_value())
# старт проекта(вызов функций)

