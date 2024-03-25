from .app import main


def calculator_probability(a) -> float:
    """
    Вычисляет вероятность события.

    Args:
        event_type: Тип события(монетка, кубик, ваш текст здесь)
        event: событие(сторона монетки, число на кубике, ваш текст здесь)
    Return:
        Веротность события
    """

    
    if a == "coin":
        prob = 1 / 2 * 100
        return f"{prob}%"
    elif a == "dice":
        return f"{round((1 / 6) * 100, 1)}%"