def rotate(a):
    b = a[0]
    a.append(b)
    a.pop(0)
    print a


print "please input list"
a = raw_input().split()
rotate(a)
