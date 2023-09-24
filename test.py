from backward import Number

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
        print("Test 9 Passed: ",k.right_child.value)
    except Exception as E:
        print("Test 9 Failed",E)
