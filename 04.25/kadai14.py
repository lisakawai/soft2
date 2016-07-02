def calc1(a):
    sum1 = 0
    for i in range(len(a)):
        sum1 += a[i]
    return sum1

def calc2(a):
    sum2 = 0
    for i in range(len(a)):
        sum2 += (a[i]-ave)*(a[i]-ave)
    return sum2

print "please input list of number"
a = map(int, raw_input().split())
ave = calc1(a)/(len(a))
disp = calc2(a)/(len(a))

print "average = %.3lf, dispersion = %.3lf\n" % (ave ,disp)
