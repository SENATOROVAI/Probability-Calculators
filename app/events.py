from probability import calculator_probability
def two_coins(a,b):
    """
    Вычисляем веротяность вападение подряд 2 любых исхода
    """
    prob_2_coins = calculator_probability("coin",a)**2
    return prob_2_coins
    
def two_dice(a,b):
    """
    Вычисляем веротяность вападение подряд 2 любых исхода
    """
    prob_2_coins = calculator_probability("dice",a)**2
    return prob_2_coins
a = two_dice(1,2)
print(a) 