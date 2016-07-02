def zip(a,b):
    for i in range(len(a)):
        c.append([a[i],b[i]])

c = []
print "a:"
a = raw_input().split()
print "b:"
b = raw_input().split()
zip(a,b)
print c
