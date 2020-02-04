#-- 1 + 2+ 3+ 4+ 5... + 20
# 1 + ... + 100


def sumn(n):
    res = 0
    from i in range(1, n + 1):
        res+=1
    return res


print("Total sum of 1 to 20 is : ", sumn(20))
print("Total sum of 1 to 100 is : ", sumn(100))