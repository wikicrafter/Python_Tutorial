print("factorial counter")
x = int(input("input x ="))
y = int(input("input y ="))

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product



for n in range(x, y): # testing
    print(n, factorialFun(n))
    