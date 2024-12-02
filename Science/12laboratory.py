'''
Вариант: 1-ое задание в блок А, 1-ое задание в блок Б
Блок А: Дано натуральные числа X,N. Вычислить выражение вида: x^n / n!
Блок Б: Вводим последо... много текста, к сожалению тут не будет самого текста
'''
# Блок А:
def fac(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def calculate_expression(x, n):
    x_power_n = x ** n 
    n_factorial = fac(n)
    result = x_power_n / n_factorial
    return result
  
x = int(input("Введите любую цифру: "))
n = int(input("Введите вторую любую цифру: "))
result = calculate_expression(x, n)
print(f"Ответ = {result}")
# Блок Б:
def find_max():
    number = int(input("Введите натуральное число (напишите 0 для завершения): "))
    if number == 0:
        return float('-inf') 
        '''
        если что -inf представляет собой специальное значение, которое
        используется для обозначения числа, меньше любого другого числа
        '''
    else:
        max_of_rest = find_max()
        return max(number, max_of_rest) 
    
max_value = find_max()
print(f"Наибольшее значение в последовательности: {max_value}")
