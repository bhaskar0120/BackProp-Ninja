from backward import Number
class Matrix:
    def __init__(self,n,m):
        self.n = n
        self.m = m
        self.mat = [Number(0) for i in range(n*m)]

    def __add__(self,b):
        if not (self.n == b.n and self.m == b.m):
            raise TypeError("Incompatible types for addition")
        t = Matrix(self.n,self.m)
        for i in range(self.n*self.m):
                t[i] = self.mat[i] + b.mat[j]
        return t

    def __sub__(self):
        if not (self.n == b.n and self.m == b.m):
            raise TypeError("Incompatible types for subtraction")
        t = Matrix(self.n,self.m)
        for i in range(self.n*self.m):
            t[i] = self.mat[i] - b.mat[i]
        return t

    def __getitem__(self,tup):
        if not (type(tup) == tuple and len(tup) == 2):
            raise TypeError("Subscript must be tuple of length 2")
        x,y = tup
        if (x< 0 or x >= self.n or y < 0 or y >= self.m):
            raise IndexError("Matrix index out of bounds")
        return self.mat[x*self.n+y]

    def __setitem__(self,tup,val):
        if not (type(tup) == tuple and len(tup) == 2):
            raise TypeError("Subscript must be tuple of length 2")
        x,y = tup
        if (x< 0 or x >= self.n or y < 0 or y >= self.m):
            raise IndexError("Matrix index out of bounds")
        self.mat[x*self.n+y] = val

    def __mult__(self,b):
        if not self.m == b.n:
            raise TypeError("Incompatible types for multiplication")
        t = Matrix(self.n,b.m)
        for i in range(self.n):
            for k in range(self.n):
                for j in range(self.m):
                    t.mat[i*self.n+j] = t.mat[i*self.n+j] + self.mat[i*self.n+k]*b.mat[k*b.n+j]

    def __iter__(self):
        for x in self.mat:
                yield x
