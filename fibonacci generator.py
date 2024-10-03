def fib():
    a = 1
    b = 1
    while True:
        f = a + b
        a = b
        b = f
        yield f

fib_gen = fib()

for i in range(10):
    print(next(fib_gen))

    