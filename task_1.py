import math


def expr_1(x: float):
    """
    Возвращает значение выражения, вычисленного по формуле, при указанном x
    https://www.wolframalpha.com/input?i=sqrt%28e%5E+%282.2+*+x%29%29+-+%7Csin%28%28pi+*+x%29+%2F+%28x+%2B+2.0+%2F+3.0%29%29%7C+%2B+1.0+%2F+7.0

    Возвращает значение выражения, вычисленного по формуле, при x = -1
    https://www.wolframalpha.com/input?i=sqrt%28e%5E+%282.2+*+%28-1.0%29%29%29+-+%7Csin%28%28%28pi+*+%28-1.0%29%29%29+%2F+%28%28%28-1.0%29+%2B+2.0+%2F+3.0%29%29%29%7C+%2B+1.0+%2F+7.0

    Возвращает значение выражения, вычисленного по формуле, при x = 0,5
    https://www.wolframalpha.com/input?i=sqrt%28e%5E+%282.2+*+0.5%29%29+-+%7Csin%28%28pi+*+0.5%29+%2F+%280.5+%2B+2.0+%2F+3.0%29%29%7C+%2B+1.0+%2F+7.0

    Возвращает значение выражения, вычисленного по формуле, при x = 1
    https://www.wolframalpha.com/input?i=sqrt%28e%5E+%282.2+*+1.0%29%29+-+%7Csin%28%28pi+*+1.0%29+%2F+%281.0+%2B+2.0+%2F+3.0%29%29%7C+%2B+1.0+%2F+7.0

    :param x: аргумент x
    :return: результат y, при указанном x
    """
    res = math.sqrt(math.pow(math.e, (2.2 * x))) - math.fabs(math.sin((math.pi * x) / (x + 2.0 / 3.0))) + 1.0 / 7.0
    return res

def expr_3(x: float):
    """
    Возвращает значение выражения, вычисленного по формуле, при указанном x
    https://www.wolframalpha.com/input?i=%281%2F7+%2Bln%28sqrt%28x%29%29%29+*E%5E%28sqrt%28abs%28x%29%29%29%29

    Возвращает значение выражения, вычисленного по формуле, при x = 0,5
    https://www.wolframalpha.com/input?i=%281%2F7+%2Bln%28sqrt%280.5%29%29%29+*E%5E%28sqrt%28abs%280.5+-+2%29%29%29%29

    Возвращает значение выражения, вычисленного по формуле, при x = 1
    https://www.wolframalpha.com/input?i=%281%2F7+%2Bln%28sqrt%281%29%29%29+*E%5E%28sqrt%28abs%281%29%29%29%29
    :param x: аргумент x
    :return: результат y, при указанном x
    """
    #другой вариант записи math.exp(math.sqrt(math.fabs(x - 2.0))) -> math.pow(math.e, math.sqrt(x - 2.0))
    res = (1.0/7.0 + math.log(math.sqrt(x))) * math.exp(math.sqrt(math.fabs(x - 2.0)))
    return res


if __name__ == '__main__':
    x = 0.5
    res = expr_1(x)
    print("Выражение №1:Значение выражения при x = 0.5: ", res)
    x =float(input("Ведите число для выражения N1"))
    res = expr_1(x)
    print("Выражение №1: Значение выражения при введеном x: ", res)

    x = 0.5
    res = expr_3(x)
    print("Выражение №3: Значение выражения при x = 0.5: ", res)
    x = int(input("Ведите число для выражения N3"))
    res = expr_3(x)
    print("Выражение №3: Значение выражения при введеном x: ", res)