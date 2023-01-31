n = int(input())
l = list(map(int, input().split(' ')))
k  = int(input())
n = len(l)
## o(n^2) sol:
# flag = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         if ((l[i] + l[j]) == k):
#             print( (l[i], l[j]) )
#             break; flag = 1
#     if flag == 1:
#         break
# if flag == 1:
#     print('not available')
## o(nlogn)
l.sort() 
i = 0; j = n-1
while i < j:
    summ = l[i] + l[j]
    if(summ < k):
        i += 1
    elif summ > k:
        j -= 1
    else :
        print((l[i], l[j]))
        break


