def add(num1, num2):
    return num1 + num2
    
def subtract(num1, num2):
    return num2 - num1

def multiply(num1, num2):
    return num1 * num2
    
def divide(num1, num2):
    return int(num1 / num2)
    
do = input("What operation would you like to do?\nA = Add 2 numbers\nS = Subtract 2 numbers\nM = Multiply 2 numbers\nD = Divide 2 numbers\n")

n1 = int(input("Number 1:\n"))
n2 = int(input("Number 2:\n"))

if (do == "a" or do == "A"):
    add(n1, n2)
elif (do == "s" or do == "S"):
    subtract(n1, n2)
elif (do == "m" or do == "M"):
    multiply(n1, n2)
elif (do == "d" or do == "D"):
    divide(n1, n2)

