def flipBulbs(x):
    count = 0
    for i in range(len(x)):
        if x[i] == count%2:
            count += 1
    return count

x = [1,0,0,1,0]
