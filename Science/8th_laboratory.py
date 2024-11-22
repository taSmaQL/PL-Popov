###
Вариант: 10
Текст задачи: 1. На отрезке [100,N](210<N<231)найти количество чисел, составленных из цифр a,b,c.
2. Составить программу, которая изменяет последовательность слов в строке на обратную
###
#1:

def task10(a,b,c,N):
    count = 0
    for i in range(100,N+1):
        number_str = str(i)
        if str(a) in number_str and str(b) in number_str and str(c) in number_str:
            if len(number_str) == 3:
                count+=1
    return count

a = 1
b = 2
c = 3

for N in range(210,231):
    result = task10(a,b,c,N)
    print(N,a,b,c,result)

#2:
x = 'ВГУИТ-ЛучшийВУЗвВоронеже'
check = ''.join(reversed(x))
print(check)
