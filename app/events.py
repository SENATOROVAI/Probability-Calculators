from probability import calculator_probability
def two_coins(a,b):
    """
    Вычисляем веротяность вападение подряд b любых исхода
    a = орел или решка 0, орел, 1 - решка
    b = кол-во выпадений
    """
    prob_2_coins = calculator_probability("coin",a)**b
    return prob_2_coins
    
def two_dice(a,b):
    """
    Вычисляем веротяность вападение подряд b любых исхода
    a = число на кубике 1,2,3,4,5,6
    b = кол-во выпадений
    """
    prob_2_coins = calculator_probability("dice",a)**b
    return prob_2_coins