'''find the number of digits in a given factorial'''

def fib(n):
    if n == 1:
        return 1
    else:
        return n * fib(n-1)

x = fib(10)
count = 0
while(x>0):
    x = x // 10
    count += 1
print(count)
