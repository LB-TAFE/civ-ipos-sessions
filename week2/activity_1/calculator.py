class Calculator:
    # Because this class doesn't require any attribues/properties to function, the __init__ is unecessary because theres
    # no reason to instantiate it, but Pycharm complains so its like this now

    # To make instantiating it meaningful, we could make num1 and num2 properties, but this adds barriers to use it easily so.. no
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

    def power(self, num1, num2):
        return num1 ** num2