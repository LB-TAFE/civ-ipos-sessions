def add(num1: [int, float, complex], num2: [int, float, complex]):
    """
    Add two numbers together
    :param num1:
    :param num2:
    :return:
    """
    ...
    for num in [num1, num2]:
        for type in [int, float, complex]:
            if isinstance(num, type):
                break
            else:
                raise TypeError
    return num1 + num2


add(1, 2)