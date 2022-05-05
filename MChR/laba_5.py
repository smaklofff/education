def f(x1):
    return 3 * x1


def main(n, x, s, h):
    for i in range(n):
        s = s + f(x) + 4 * f(x + h) + f(x + 2 * h)
        x = x + 2 * h
    return s * h / 3


if __name__ == '__main__':
    n, a, b = 10, 1, 3
    print(round(main(n, a, 0, (b - a) / (2 * n))))
