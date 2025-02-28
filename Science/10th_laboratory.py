'''
Вариант: Отсутствует
Текст задач: Для заданий из практической работы №9 для своего варианта. 
Организовать ввод данных (матриц) из файла (имя: ФИО_группа_vvod.txt) 
и вывод результатов в файл (имя: ФИО_группа_vivod.txt).
'''
def is_monota(row):
    if len(row) <= 1:
        return True
    incr = row[1] >= row[0]  
    for i in range(1, len(row)):
        if incr and row[i] < row[i - 1]:
            return False
        elif not incr and row[i] > row[i - 1]:
            return False
    return True

def find_max(matrix):
    max_element = float('-inf') 
    for row in matrix:
        if is_monota(row):  
            current_max = max(row) 
            max_element = max(max_element, current_max)
    return max_element

matrix = []
with open(r'C:\Users\user\Desktop\KP_Y242_vvod.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        matrix.append(row)

max_element = find_max(matrix)

with open('KP_Y242_vivod.txt', 'w') as file:
    if max_element == float('-inf'):
        file.write("Нет монотонных строк в матрице.\n")
    else:
        file.write(str(max_element))
