num1 = int(input("Enter the first number: " ))
num2 = int(input("enter the second number:" ))
operation = (input("enter any operation +, -, x, /: "))
def total(): 
    if operation == "+":
        return  num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "x":
        return num1 * num2 
    elif operation == "/":
        return num1 / num2
print(f"{num1} {operation} {num2} = {total()}")
