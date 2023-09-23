from backward import Number

if __name__ == "__main__":
    a = Number(2)
    b = Number(3)
    c = Number(5)
    d = Number(6)
    print("Test 1 Passed: ",a,b)
    e = a + b
    print("Test 2 Passed: ",e)
    f = b + a
    g = e * f
    print("Test 3 Passed: ",g)
    h = g / c + f * e
    print("Test 4 Passed: ",a,b)
