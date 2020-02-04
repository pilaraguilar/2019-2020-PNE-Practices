#exercise 1 session2

res=0
i1=0
i2=1
for i in range(1, 11):
    n= (i1) + i2
    i1 =i2
    i2 =n
    res+=1
    print(res)
