def fibon(n):

    if n in [0, 1]:
        return n
    n1 = 0
    n2 = 0
    n = 0

    for i in range(2, n + 1):
        n = n1 + n2
        n1 = n2
        n2 = n

    return n


def sumf(n):
    f = 0
    for i in range(n + 1):
        f += fibon(i)
    return f


print("Sum of the First 5 terms of the Fibonacci series: ", sumf(5))
print("Sum of the First 10 terms of the Fibonaci series: ", sumf(10))
