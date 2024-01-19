class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num1

    def multiply(self):
        return self.num1 * self.num1

    def divide(self):
        return self.num1 / self.num1



num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
operator = input("Enter operator(+, -, *, /): ")

calculator = Calculator(num1, num2)

if operator == '+':
    print(calculator.add())
elif operator == '-':
    print(calculator.subtract())
elif operator == '*':
    print(calculator.multiply())
elif operator == '/':
    print(calculator.divide())
else:
    print("Invalid operator")

