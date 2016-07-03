#plot.pl
set grid
set key left top
set ytics 0.025
set xlabel "n"
set ylabel "time(s)"
plot 'counting.txt' using 1:2 w l t 'counting sort' lc rgb 'red'
replot 'heap.txt' using 1:2 w l t 'heap sort' lc rgb 'blue'
replot 'merge.txt' using 1:2 w l t 'merge sort' lc rgb 'green'
set terminal png
set output 'plot.png'
replot 'quick.txt' using 1:2 w l t 'quick sort' lc rgb 'yellow'
pause(-1)