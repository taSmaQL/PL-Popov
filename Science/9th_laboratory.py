###
Вариант: 10
Текст задач: 1. Найти максимальный среди всех элементов тех строк заданной матрицы, которые упорядочены(либо по возрастанию, либо по убыванию)
2. Расположить столбцы матрицы D[M,N] в порядке возрастания элементов k-й строки (1 <= k <= M)
###
# 1:
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
matrix = [
  [1, 2, 3, 4],
  [5, 4, 3, 2],  
  [6, 7, 8, 9],
  [10, 9, 8, 7]  
]
max_element = find_max(matrix)
print(f"Максимальный элемент в монотонных строках: {max_element}")

# 2:
def sort_matrix(D, k):
  M, N = len(D), len(D[0])
  if not 1 <= k <= M:
    raise ValueError("Неверный номер строки k.")
  sorted_indices = sorted(range(N), key=lambda j: D[k - 1][j])
  sorted_D = [[D[i][j] for j in sorted_indices] for i in range(M)]
  return sorted_D
# Пример:
D = [[1, 4, 2], [3, 5, 6], [7, 8, 9]]
k = 2  
sorted_D = sort_matrix(D, k)
print(sorted_D)
