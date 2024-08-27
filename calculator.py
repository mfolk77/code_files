def calculations():
    a = float(input("Type your first number: "))
    b = float(input("Type your second number: "))

    term = input("Enter the operation (+, -, *, /): ")

    if term == "+":
        result = a + b
    elif term == "-":
        result = a - b
    elif term == "*":
        result = a * b
    elif term == "/":
        result = a / b

    return result

print(calculations())