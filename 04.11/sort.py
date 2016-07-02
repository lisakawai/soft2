def partition(a,n):
    p=a[0]
    m=0

    for i in range(0,n):
        if a[i]<p:
            pre=a[0]
            a[0]=a[i]
            m+=1

            for j in range(1,i+1):
                temp=a[j]
                a[j]=pre
                pre=temp
    return m

NUM=20

def sort(a,n):
    if n<=1:
        return
    c=partition(a,n)
    sort(a,c)

    b=a[c+1:]

    sort(b,n-c-1)

    a[c+1:]=b[:]

def main():
   data=[20,62,17,38,76,92,59,11,93,88,79,50,89,67,75,26,83,22,13,48]
   sort(data,NUM)   

   print data

   print "\n";

   return 0

main()
