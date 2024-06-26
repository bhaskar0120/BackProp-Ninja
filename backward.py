import math
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
            self.left_child.backward(factor=factor*self.left_derivative())
            self.right_child.backward(factor=factor*self.right_derivative())


    def __add__(self,b):
        return Additive(value=self.value+b.value,functional=True,left_child=self,right_child=b)
    def __sub__(self,b):
        return Subtractive(value=self.value-b.value,functional=True,left_child=self,right_child=b)
    def __mul__(self,b):
        return Multiplicative(value=self.value*b.value,functional=True,left_child=self,right_child=b)
    def __truediv__(self,b):
        return Divisive(value=self.value/b.value,functional=True,left_child=self,right_child=b)
    def __pow__(self,b):
        return Exponential(value=self.value**b.value,functional=True,left_child=self,right_child=b)
    def __str__(self):
        return "(%s %s %s)"%(self.left_child.__str__(), self.symbol, self.right_child.__str__())


class Additive(Node):
    def __init__(self,value=float(),functional=False,left_child=None,right_child=None):
        Node.__init__(self,value,functional,left_child,right_child)
        self.symbol = '+'
    def left_derivative(self):
        return 1.0
    def right_derivative(self):
        return 1.0
    def copy(self):
        return Additive(value=self.value,functional=True,left_child=self.left_child.copy(),right_child=self.right_child.copy())
    def calculate(self):
        self.right_child.calculate()
        self.left_child.calculate()
        self.value += self.left_child.value+self.right_child.value

class Subtractive(Node):
    def __init__(self,value=float(),functional=False,left_child=None,right_child=None):
        Node.__init__(self,value,functional,left_child,right_child)
        self.symbol = '-'
    def left_derivative(self):
        return 1.0
    def right_derivative(self):
        return -1.0
    def copy(self):
        return Subtractive(value=self.value,functional=True,left_child=self.left_child.copy(),right_child=self.right_child.copy())
    def calculate(self):
        self.right_child.calculate()
        self.left_child.calculate()
        self.value += self.left_child.value-self.right_child.value

class Multiplicative(Node):
    def __init__(self,value=float(),functional=False,left_child=None,right_child=None):
        Node.__init__(self,value,functional,left_child,right_child)
        self.symbol = '*'
    def left_derivative(self):
        return self.right_child.value
    def right_derivative(self):
        return self.left_child.value
    def copy(self):
        return Multiplicative(value=self.value,functional=True,left_child=self.left_child.copy(),right_child=self.right_child.copy())
    def calculate(self):
        self.right_child.calculate()
        self.left_child.calculate()
        self.value += self.left_child.value*self.right_child.value

class Divisive(Node):
    def __init__(self,value=float(),functional=False,left_child=None,right_child=None):
        Node.__init__(self,value,functional,left_child,right_child)
        self.symbol = '/'
    def left_derivative(self):
        return 1/self.right_child.value if self.right_child.value != 0.0 else math.inf
    def right_derivative(self):
        return -self.left_child.value/(self.right_child.value)**2 if self.right_child.value != 0.0 else -math.copysign(math.inf,self.left_child.value)
    def copy(self):
        return Divisive(value=self.value,functional=True,left_child=self.left_child.copy(),right_child=self.right_child.copy())
    def calculate(self):
        self.right_child.calculate()
        self.left_child.calculate()
        self.value += self.left_child.value/self.right_child.value if self.right_child.value != 0.0 else math.copysign(math.inf,self.left_child.value)

class Exponential(Node):
    def __init__(self,value=float(),functional=False,left_child=None,right_child=None):
        Node.__init__(self,value,functional,left_child,right_child)
        self.symbol = '**'
    def left_derivative(self):
        return self.right_child.value*self.left_child.value**(self.right_child.value-1)
    def right_derivative(self):
        return math.log(self.left_child.value)*self.left_child.value**self.right_child.value if self.left_child.value > 0 else -math.inf
    def copy(self):
        return Exponential(value=self.value,functional=True,left_child=self.left_child.copy(),right_child=self.right_child.copy())
    def calculate(self):
        self.right_child.calculate()
        self.left_child.calculate()
        self.value += self.left_child.value**self.right_child.value

class Number(Node):
    def __init__(self,value):
        Node.__init__(self)
        self.value += value
    def __str__(self):
        return "%f"%self.value
    def copy(self):
        return Number(value=self.value)
    def calculate(self):
        return;
