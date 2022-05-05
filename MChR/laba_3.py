a = [[5, 2, 3, 17], [3, 6, 2, 6], [2, 4, 8, 24]]

check = True
for i in range(len(a)):
    # Проверка условия по строкам
    if a[i][i] >= sum(a[i]) - a[i][i] or a[i][i] >= list(map(sum, zip(*a)))[i] - a[i][i]:
        print(f'Условия для {i + 1} уравнения выполняются')
    else:
        check = False

x0, x1 = [], [100000000000] * 3
if check:
    for i in range(len(a)):
        a[i] = list(map(lambda k1: k1 / a[i][i], a[i]))
        x0.append(a[i][-1])

    while max(list(map(lambda k1, k2: abs(k1 - k2), x0, x1))) >= 0.001:
        x1 = x0.copy()
        for i in range(len(x1)):
            sm = 0
            for j in range(len(x1)):
                if i != j:
                    sm += a[i][j] * x1[j]
            x0[i] = a[i][-1] - sm
    print(list(map(round, x0)))