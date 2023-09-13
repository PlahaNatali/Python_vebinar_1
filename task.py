# Task_1

# a = int(input(f'Введите сторону a : '))
# b = int(input(f'Введите сторону b : '))
# c = int(input(f'Введите сторону c : '))
# if a == b == c:
#     print('Треугольник существует! Он равносторонний.')
# elif a > b > c:
#     print('Треугольник существует! Он разносторонний.')
# elif a == b or a == c or b == c:
#     print('Треугольник существует! Он равнобедренный.')
# else:
#     print('Такой треугольник не существует!')

# Task_2

number = int(input("Введите число: "))
i = 2 
if number < 0 or number > 100000:
    print("Число недопустимо. Допустимы числа от 0 до 100000.")
while number > i: 
    if (number % i) == 0: 
        print('Это составное число.') 
        break 
    i += 1 
if i == number: 
    print('Это простое число.')