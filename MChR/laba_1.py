from random import randint


def get_intervals(change_input, left_restriction, right_restriction):
    if change_input.lower() in ['автоматический', '1']:
        a, b, c, d = randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10)
    else:
        a, b, c, d = input('Введите коэф-ты a, b, c, d через пробел:').split()
    print(f'Текущее уравнение:\n{a}*x^3+{b}*x^2+{c}*x+{d}\n')

    func_result_current, func_result_past = 0, 0
    intervals = []
    x = left_restriction
    while x < right_restriction:
        x += 0.25
        func_result_past = func_result_current
        func_result_current = get_y(a, b, c, d, x)
        if func_result_current == 0:
            intervals.append((x - 0.25, x + 0.25))
        if func_result_current < 0 < func_result_past:
            intervals.append((x - 0.25, x))
        elif func_result_current > 0 > func_result_past:
            intervals.append((x - 0.25, x))

    print('Полученные интервалы:')
    for i in range(len(intervals)):
        print(intervals[i])
    for X, y in get_roots(intervals, a, b, c, d):
        print(f'Значение функции в точке x={X} равно {y}')


def get_y(a, b, c, d, x):
    return a * (x ** 3) + b * (x ** 2) + c * x + d


def get_roots(answers, a, b, c, d):
    roots = []
    for x1, x2 in answers:
        F1 = get_y(a, b, c, d, x1)
        F3, X = 1, 1
        A, B = x1, x2
        while abs(F3) >= 0.001 and abs(A - B) >= 0.001:
            X = (A + B) / 2
            F3 = get_y(a, b, c, d, X)
            if F1 * F3 < 0:
                B = X
            else:
                A = X
                F1 = F3
        roots.append((X, F3))
    return roots


if __name__ == '__main__':
    get_intervals(input('Варианты выбора коэф. для уравнения:\n'
                        '1) автоматический\n'
                        '2) ручной\n'), -11, 11)