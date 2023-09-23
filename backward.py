class Node:
    def __init__(self,value=float(),functional=False,left_child=None,right_child=None):
        self.grad = float()
        self.value = value
        self.functional = functional 
        self.left_child = left_child
        self.right_child = right_child
        self.symbol = ''
    def left_derivative(self):
        return 0
    def right_derivative(self):
        return 0
    def backward(self,factor=1):
        self.grad = factor
        if self.functional:
            self.left_child.backward(factor=self.left_derivative())
            self.right_child.backward(factor=self.right_derivative())
    def __add__(self,b):
        return Additive(value=self.value+b.value,functional=True,left_child=self,right_child=b)
    def __str__(self):
        return "(%s %s %s)"%(self.left_child.__str__(), self.symbol, self.right_child.__str__())


class Additive(Node):
    def __init__(self,value=float(),functional=False,left_child=None,right_child=None):
        Node.__init__(self,value,functional,left_child,right_child)
        self.symbol = '+'
    def left_derivative(self):
        return 1
    def right_derivative(self):
        return 1

class Number(Node):
    def __init__(self,value):
        Node.__init__(self)
        self.value = value
    def __str__(self):
        return "%f"%self.value




