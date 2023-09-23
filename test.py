from backward import Number

if __name__ == "__main__":
    try:
        a = Number(2)
        b = Number(3)
        c = Number(5)
        d = Number(6)
        i = Number(10)
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
        g = e * f
        print("Test 3 Passed: ",g)
    except Exception as E:
        print("Test 3 Failed",E)

    try:
        h = g / i - f * e
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

