#-- 1 + 2+ 3+ 4+ 5... + 20
# 1 + ... + 100

res20=0

for i in range(1, 21):
    res20 +=i

res100=0

for i in range(1, 101):
    res100 +=i



print("Total sum of 1 to 20 is : ", res20)
print("Total sum of 1 to 100 is : ", res100)