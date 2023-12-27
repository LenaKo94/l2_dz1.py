number = int(input('Type x: '))
number_1 = number // 100
number_2 = (number % 1000) // 100
number_3 = (number % 100) // 10
number_4 = number % 10

print(number_1)
print(number_2)
print(number_3)
print(number_4)

