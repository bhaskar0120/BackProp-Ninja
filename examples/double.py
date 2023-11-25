def main():
    from backward import Number
    from random import random


    train_x = [Number(2),Number(3),Number(6),Number(7)]
    train_y = [Number(4),Number(6),Number(12),Number(14)]

    # Model
    # y = m*x+b
    m = Number(random())
    b = Number(random())


    learningRate = 0.01
    for _ in range(1000):
        for i in range(len(train_x)):
            E = (train_y[i] - m*train_x[i] - b)**Number(2)
            print(E.value)
            E.backward()
            m.value -= learningRate*m.grad
            b.value -= learningRate*b.grad
    print(m,b)


if __name__ == "__main__":
    main()


