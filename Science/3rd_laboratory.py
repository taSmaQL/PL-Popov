###
Вариант: отсутствует, но эта задача из "материал к прочтению"
Текст задачи: Даны три целых числа. Выбрать из них те, которые принадлежат интервалу [1,3]
###

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number= int(input("Введите третье число: "))
if 0 < first_number < 4 :
    print('Первое число валидное. Успех')
if 0 < second_number < 4:
    print('Второе число валидное. Успех')
if 0 < third_number < 4:
    print('Третье число валидное. Успех')

###
Вариант: 1
Текст задачи: написать программу, которая считывает три числа и выводит их сумму. 
Каждое число записано в отдельной строке
###

# Задача под номером 1:
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))
sum_of_number = first_number+second_number+third_number
print(f'Финальная сумма чисел: {sum_of_number}')

    








