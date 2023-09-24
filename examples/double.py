def main():
    from backward import Number
    from random import random, seed
    seed(1203)
    train_x = [Number(2),Number(3),Number(6),Number(7)]
    train_y = [Number(4),Number(6),Number(12),Number(14)]

    # Model
    # y = m*x+b
    m = Number(random())
    b = Number(random())

    # for i in E = E + (train_y - m*train_x+b)**2

    E = Number(0)
    for i in range(4):
        E = E + (train_y[i] - m*train_x[i]+b)**Number(2)
    for i in range(1000):
        E.calculate()
        print(E.value)
        E.backward()
        m.value -= 0.0001*m.grad
        b.value -= 0.0001*b.grad
    print(m,b)


if __name__ == "__main__":
    main()


