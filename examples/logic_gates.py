def OR():
    from backward import Number
    from random import random
    from math import e
    # A simple OR Gate represented by single Neuron
    train_x = [[Number(0),Number(0)],
               [Number(0),Number(1)],
               [Number(1),Number(0)],
               [Number(1),Number(1)]]
    train_y = [Number(0),Number(1),Number(1),Number(1)]

    # model sigmoid 
    # E = (y-w1**3*x1-w2**3*x2-b)**2

    w1 = Number(random())
    w2 = Number(random())
    b = Number(random())

    learningRate = 5
    for _ in range(1000):
        for i in range(len(train_x)):
            S = w1*train_x[i][0] + w2*train_x[i][1]+b
            Y = Number(1)/(Number(1) + Number(e)**(Number(0)-S))
            E = (train_y[i] - Y)**Number(2)
            E.backward()
            w1.value -= learningRate*w1.grad
            w2.value -= learningRate*w2.grad
            b.value -= learningRate*b.grad
            print(E.value)
    print(w1,w2,b)

def AND():
    from backward import Number
    from random import random
    from math import e
    # A simple OR Gate represented by single Neuron
    train_x = [[Number(0),Number(0)],
               [Number(0),Number(1)],
               [Number(1),Number(0)],
               [Number(1),Number(1)]]
    train_y = [Number(0),Number(0),Number(0),Number(1)]

    # model sigmoid 
    # E = (y-w1**3*x1-w2**3*x2-b)**2

    w1 = Number(random())
    w2 = Number(random())
    b = Number(random())

    learningRate = 5
    for _ in range(1000):
        for i in range(len(train_x)):
            S = w1*train_x[i][0] + w2*train_x[i][1]+b
            Y = Number(1)/(Number(1) + Number(e)**(Number(0)-S))
            E = (train_y[i] - Y)**Number(2)
            E.backward()
            w1.value -= learningRate*w1.grad
            w2.value -= learningRate*w2.grad
            b.value -= learningRate*b.grad
            print(E.value)
    print(w1,w2,b)

if __name__ == "__main__":
    OR()


    
