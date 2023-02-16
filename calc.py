def calculate(operator, num1, num2):
    if (operator == "+"):
        return num1 + num2
    if (operator == "-"):
        return num1 - num2
    if (operator == "*"):
        return num1 * num2
    if (operator == "/")
        return num1 / num2
    
while True:
    operator = input("What operation would you like to do?\nA = Add 2 numbers\nS = Subtract 2 numbers\nM = Multiply 2 numbers\nD = Divide 2 numbers\n")
    n1 = int(input("Number 1:\n"))
    n2 = int(input("Number 2:\n"))
    print(calculate(operator, n1, n2))
