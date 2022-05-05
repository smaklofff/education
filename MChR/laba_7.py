import pandas as pd
import matplotlib.pyplot as plt


def t(t, h):
    return t + h


def x(x, h, x1):
    return x + h * x1


def x1(x1, h, x2):
    return x1 + h * x2


def x2(k, x, m):
    return -k * x / m


def main():
    h = (b - a) / n
    t_, x_, x1_, x2_ = 0, -5, 0, 0
    list_t, list_x, list_x1, list_x2 = [], [], [], []
    for i in range(n):
        x1_ = x1(x1_, h, x2_)
        x2_ = x2(k, x_, m)
        x_ = x(x_, h, x1_)
        t_ = t(t_, h)

        list_t.append(t_)
        list_x.append(x_)
        list_x1.append(x1_)
        list_x2.append(x2_)
        print(t_, x_, x1_, x2_)
    create_plot(list_t, list_x, list_x1, list_x2)


def create_plot(list_t, list_x, list_x1, list_x2):
    data = pd.DataFrame({
                         'x': list_x,
                         'x1': list_x1,
                         'x2': list_x2})
    data.plot(kind='line')
    plt.show()


if __name__ == '__main__':
    k, m = 12, 10
    n, a, b = 300, -5, 5
    main()