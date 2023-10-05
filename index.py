def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return 'Invalid operator'

print(calculator(2, 3, '+'))
print(calculator(2, 3, '-'))
print(calculator(2, 3, '*'))
print(calculator(2, 3, '/'))
print(calculator(2, 3, '%'))
