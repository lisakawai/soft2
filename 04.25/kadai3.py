def sum(x, y, z):
    if x>y and z>y:
        print x+z
    elif x>z and y>z:
        print x+y
    else:
        print z+y

l = map(int, raw_input().split())
sum(l[0], l[1], l[2])
