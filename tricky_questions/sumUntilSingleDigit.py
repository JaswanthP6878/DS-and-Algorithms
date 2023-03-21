num = int(input())
sum1 = 0
print((num-1)%9 + 1)

''''''
i = 2
while i*i <= size:
    if hashList[i]:
        for j in range(i*i, size, 1):
            hashList[i] = 0
    i += 1