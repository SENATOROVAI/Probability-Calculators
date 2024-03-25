from app import main



def calculator_probability() -> float:
    """
    Вычисляет вероятность события.

    Args:
        event_type: Тип события(монетка, кубик, ваш текст здесь)
        event: событие(сторона монетки, число на кубике, ваш текст здесь)
    Return:
        Веротность события
    """

    event_type, event = main()
    if event_type == "coin":
        prob = 1 / 2 
        return prob #f"{prob}%"
    elif event_type == "dice":
        return (1 / 6)