
from decimal import Decimal

# Получение данных
n = int(input('Введите количество уравнений:'))
a = [[0] * (n+1)] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
print('Исходная матрица коэф.:\n' + str(a))

# Деление разрешающего уравнения на разрешающий элемент             'Введите коэф. для первого уравнения через пробел:'
for k in range(n):
    a[k] = list(map(lambda x: Decimal(str(x)) / Decimal(str(a[k][k])), a[k]))
    for i in range(k + 1, n):
        a[i] = list(map(lambda x1, x2: Decimal(str(x1)) - Decimal(str(x2)) * Decimal(str(a[i][k])), a[i], a[k]))

# Исключение очередного неизвестного
x = [0] * n
x[n - 1] = Decimal(str(a[n - 1][n]))
for i in range(n - 2, -1, -1):
    x[i] = Decimal(str(a[i][n])) - sum(list(map(lambda x1, x2: Decimal(str(x1)) * Decimal(str(x2)), a[i][:n], x)))

# Вывод
for i in x:
    print(format(i, '.3f'))

# Проверка
for i in range(len(x)):
    if sum(list(map(lambda x1, x2: Decimal(str(x1))*Decimal(str(x2)), x, a[i][:n]))) == a[i][n:][0]:
        print(f'{i+1}-е уравнение в системе решено правильно')
'''
1 1 2 3 1
1 2 3 -1 -4
3 -1 -1 -2 -4
2 3 -1 -1 -6

'''
