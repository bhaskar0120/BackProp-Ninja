from backward import Number

if __name__ == "__main__":
    try:
        a = Number(2)
        b = Number(3)
        c = Number(5)
        d = Number(6)
        print("Test 1 Passed: ",a,b)
    except(Exception):
        print("Test 1 Failed")

    try:
        e = a + b
        print("Test 2 Passed: ",e)
    except(Exception):
        print("Test 2 Failed")

    try:
        f = b + a
        g = e * f
        print("Test 3 Passed: ",g)
    except(Exception):
        print("Test 3 Failed")

    try:
        h = g / c + f * e
        print("Test 4 Passed: ",a,b)
    except(Exception):
        print("Test 4 Failed")

