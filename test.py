from backward import Number
from matrix import Matrix

if __name__ == "__main__":
    try:
        a = Number(2)
        b = Number(3)
        c = Number(5)
        d = Number(6)
        g = Number(10)
        i = Number(12)
        print("Test 1 Passed: ",a,b)
    except Exception as E:
        print("Test 1 Failed",E)

    try:
        e = a + b
        print("Test 2 Passed: ",e)
    except Exception as E:
        print("Test 2 Failed",E)

    try:
        f = c + d
        print("Test 3 Passed: ",f)
    except Exception as E:
        print("Test 3 Failed",E)

    try:
        h = e / i - f * g
        print("Test 4 Passed: ",a,b)
    except Exception as E:
        print("Test 4 Failed",E)

    try:
        e.backward()
        print("Test 5 Passed: ",a.grad,b.grad)
    except Exception as E:
        print("Test 5 Failed",E)

    try:
        h.backward()
        print("Test 6 Passed: ",a.grad,b.grad,c.grad,d.grad,e.grad,f.grad,g.grad,i.grad)
    except Exception as E:
        print("Test 6 Failed",E)

    try:
        h = a**b
        h.backward()
        print("Test 7 Passed: ",a.grad,b.grad)
    except Exception as E:
        print("Test 7 Failed",E)

    try:
        k = h.copy()
        k.right_child.value = 0
        print("Test 8 Passed: ",h.right_child.value,k.right_child.value)
    except Exception as E:
        print("Test 8 Failed",E)

    try:
        k.calculate()
        print("Test 9 Passed: ",k)
    except Exception as E:
        print("Test 9 Failed",E)


    # Test for matrix class
    try:
        mat1 = Matrix(3,3)
        mat2 = Matrix(3,3)
        print("Test 10 Passed: ",mat1,mat2)
    except Exception as E:
        print("Test 10 Failed",E)

    try:
        mat1[0,0] = Number(1)
        mat1[0,1] = Number(2)
        mat1[0,2] = Number(3)
        mat1[1,0] = Number(4)
        mat1[1,1] = Number(5)
        mat1[1,2] = Number(6)
        mat1[2,0] = Number(7)
        mat1[2,1] = Number(8)
        mat1[2,2] = Number(9)
                            
        mat2[0,0] = Number(1)
        mat2[0,1] = Number(2)
        mat2[0,2] = Number(3)
        mat2[1,0] = Number(4)
        mat2[1,1] = Number(5)
        mat2[1,2] = Number(6)
        mat2[2,0] = Number(7)
        mat2[2,1] = Number(8)
        mat2[2,2] = Number(9)
        print("Test 11 Passed: ",mat1, mat2)
    except Exception as E:
        print("Test 11 Failed",E)

    try:
        mat3 = mat1 + mat2
        print("Test 12 Passed: ",mat3)
    except Exception as E:
        print("Test 12 Failed",E)

    try:
        mat4 = mat1 - mat2
        print("Test 13 Passed: ",mat4)
    except Exception as E:
        print("Test 13 Failed",E)

    try:
        mat5 = mat1 * mat2
        print("Test 14 Passed: ",mat5)
    except Exception as E:
        print("Test 14 Failed",E)

    try:
        val1 = mat1[0,0]
        print("Test 15 Passed: ",val1)
    except Exception as E:
        print("Test 15 Failed",E)

        
