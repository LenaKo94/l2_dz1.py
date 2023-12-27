number = int(input("Введіть 5-ти значне число: "))
number_1 = number % 10
number_2 = (number % 100) // 10
number_3 = (number % 1000) // 100
number_4 = (number % 10000) // 1000
number_5 = number // 10000
reversed_number = number_1 * 10000 + number_2 * 1000 + number_3 * 100 + number_4 * 10 + number_5
print(reversed_number)


