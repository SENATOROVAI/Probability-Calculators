def calculator_probability(event_type: str, event: int) -> float:
    """
    Вычисляет вероятность события. 
     
    Args: 
        event_type: Тип события(монетка, кубик, ваш текст здесь)
        event: событие(сторона монетки, число на кубике, ваш текст здесь)
    Return: 
        Веротность события
    """
    if event_type == "coin": 
        prob = 1/2
        return prob
    elif event_type == "dice":
        prob = 1/6
        return prob
     
    #  ваш код дальнейшей реализации здесь???
    
    # иначе: ???
    #     райс велью еррор (неверный тип события)??