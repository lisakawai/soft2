x = [4,50,3,10,88,39,2,15]

for i in range(1,len(x)):
    j = i
    while (j > 0) and (x[j-1] > x[j]) :
        tmp = x[j-1]
        x[j-1] = x[j]
        x[j] = tmp
        j -= 1
    
print x