def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci2(n):
    b1 = 1
    b2 = 1
    sval = 1
    if n!=1 and n!=2:
        for i in range(n-2):
            b1 = b2
            b2 = sval
            sval = b1 + b2
    return sval

print(fibonacci(7))
print(fibonacci2(7))