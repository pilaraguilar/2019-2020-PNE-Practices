


res=0
i1=0
i2=1
def fibo(n):
    a, b = 0,1
    while a < n:
        a, b = b, a+b

    return a
    print()
print(fibo(10))
