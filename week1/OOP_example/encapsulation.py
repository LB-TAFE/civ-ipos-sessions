# ├── main.py
# └── calculator.py

# Encapsulation is the practice of hiding the internal details of an object from the outside world. 
# In Python, we can achieve encapsulation by using classes and access modifiers. 
# Here is an example of how we can encapsulate the add, subtract, and multiply functions:

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b


class ScientificCalculator(Calculator):
    def __init__(self, a, b):
        super().__init__(a, b)

    def power(self):
        return self.a ** self.b
