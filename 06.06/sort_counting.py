# -*- coding: utf-8 -*-
import time

def counting_sort(num):
    max_num = max(num)
    count = [0] * (max_num + 1)               # 度数分布のリストをゼロで初期化
    for a in num:
        count[a] += 1             # 出現回数の計算
    i = 0
    for a in range(max_num + 1):            # 値の最大値まで繰り返す
        for c in range(count[a]): # 値の出現回数だけ繰り返して元のリストに値をコピーする
            num[i] = a
            i += 1
 

if __name__ == '__main__':
    f = open('counting.txt', 'w') 

    num = []
    for line in open('rand.txt', 'r'):
        itemList = line.split()
        for item in itemList:
            num.append( int(item) )
    

    for n in xrange(2,5001):
        num_calc = num[0:n]

        begin = time.time()
        counting_sort(num_calc)
        end = time.time()
        f.write('{} {}\n'.format(n, (end - begin)))

        #print num_calc
    f.close()