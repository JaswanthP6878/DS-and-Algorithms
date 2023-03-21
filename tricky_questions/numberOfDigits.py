from math import log10
num  = int(input())
sum1 = 0
for i in range(1,num+1):
    sum1 += log10(i)
print(sum1)