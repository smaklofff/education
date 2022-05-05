# Вариант 3


def c(x, y):
    return 4 * y ** 2 - 6 * y * x + 7 * x ** 2


def f(x, y):
    return (3 * y - 7 * x) / (4 * y - 3 * x)


def main():
    h = (b - a) / n
    x = a
    y = 3
    print(x, y, c(x, y))
    for i in range(n):
        y += h * f(x, y)
        x += h
        print(x, y, c(x, y))


if __name__ == '__main__':
    a, b, n = 1, 2, 10
    main()