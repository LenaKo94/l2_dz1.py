num1 = input('Перше число:')
operation = input('Введіть операцію:')
num2 = input('Друге число')

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
    if num2 == 0:
        print('Помилка ділення на 0.')
print('Результат:', result)




