operator = input()
a = int(input())
b = int(input())


def calculate_numbers(a, b, operator):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = a // b
    elif operator == "subtract":
        result = a - b
    elif operator == "add":
        result = a + b

    return result

print(calculate_numbers(a,b,operator))