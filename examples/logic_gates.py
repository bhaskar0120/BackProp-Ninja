from backward import Number
from random import random, seed
from math import e

# Sigmoid function
def sigm(x):
    return Number(1)/(Number(1)+Number(e)**(Number(0)-x));


def OR():
    # A simple OR Gate represented by single Neuron
    train_x = [[Number(0),Number(0)],
               [Number(0),Number(1)],
               [Number(1),Number(0)],
               [Number(1),Number(1)]]
    train_y = [Number(0),Number(1),Number(1),Number(1)]

    # Model
    # Y = sigm(w1*x[0]+w2*x[1]+b)

    w1 = Number(random())
    w2 = Number(random())
    b = Number(random())

    learningRate = 5
    for _ in range(1000):
        for i in range(len(train_x)):
            Y = sigm(w1*train_x[i][0] + w2*train_x[i][1]+b)
            E = (train_y[i] - Y)**Number(2)
            E.backward()
            w1.value -= learningRate*w1.grad
            w2.value -= learningRate*w2.grad
            b.value -= learningRate*b.grad
        print(E.value)
    print("="*20)

    for i,x in enumerate(train_x):
        Y = sigm(w1*train_x[i][0] + w2*train_x[i][1]+b)
        print("{} OR {} = {:.2f} ({})".format(x[0].value,x[1].value,Y.value,train_y[i].value))

def AND():
    # A simple AND Gate represented by single Neuron
    train_x = [[Number(0),Number(0)],
               [Number(0),Number(1)],
               [Number(1),Number(0)],
               [Number(1),Number(1)]]
    train_y = [Number(0),Number(0),Number(0),Number(1)]

    # Model
    # Y = sigm(w1*x[0]+w2*x[1]+b)

    w1 = Number(random())
    w2 = Number(random())
    b = Number(random())

    learningRate = 5
    for _ in range(1000):
        for i in range(len(train_x)):
            Y = sigm(w1*train_x[i][0] + w2*train_x[i][1]+b)
            E = (train_y[i] - Y)**Number(2)
            E.backward()
            w1.value -= learningRate*w1.grad
            w2.value -= learningRate*w2.grad
            b.value -= learningRate*b.grad
        print(E.value)
    print("="*20)

    for i,x in enumerate(train_x):
        Y = sigm(w1*train_x[i][0] + w2*train_x[i][1]+b)
        print("{} AND {} = {:.2f} ({})".format(x[0].value,x[1].value,Y.value,train_y[i].value))

def XOR():
    # A simple XOR Gate represented by 3 Neurons
    train_x = [[Number(0),Number(0)],
               [Number(0),Number(1)],
               [Number(1),Number(0)],
               [Number(1),Number(1)]]
    train_y = [Number(0),Number(1),Number(1),Number(0)]

    # Model
    # Y = sigm(w5*sigm(x[0]*w1+x[1]*w3+b1) + w6*sigm(x[0]*w2+x[1]*w4+b2)) 

    w1 = Number(random())
    w2 = Number(random())
    w3 = Number(random())
    w4 = Number(random())
    w5 = Number(random())
    w6 = Number(random())
    b1 = Number(random())
    b2 = Number(random())
    b3 = Number(random())


    learningRate = 5
    for _ in range(1000):
        for i in range(len(train_x)):
            Y = sigm( w5*sigm( train_x[i][0]*w1+train_x[i][1]*w3+b1)
                    + w6*sigm( train_x[i][0]*w2+train_x[i][1]*w4+b2) + b3)
            E = (train_y[i]-Y)**Number(2)
            E.backward()
            w1.value -= learningRate*w1.grad
            w2.value -= learningRate*w2.grad
            w3.value -= learningRate*w3.grad
            w4.value -= learningRate*w4.grad
            w5.value -= learningRate*w5.grad
            w6.value -= learningRate*w6.grad
            b1.value -= learningRate*b1.grad
            b2.value -= learningRate*b2.grad
            b3.value -= learningRate*b3.grad
        print(E.value)
    print("="*20)

    for i,x in enumerate(train_x):
        Y = sigm( w5*sigm( train_x[i][0]*w1+train_x[i][1]*w3+b1) 
                 + w6*sigm( train_x[i][0]*w2+train_x[i][1]*w4+b2) + b3)
        print("{} OR {} = {:.2f} ({})".format(x[0].value,x[1].value,Y.value,train_y[i].value))



if __name__ == "__main__":
    seed(1729)
    # AND()
    # OR()
    XOR()

