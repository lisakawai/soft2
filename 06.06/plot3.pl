#plot.pl
set grid
set key left top
set ytics 0.001
set xlabel "n"
set ylabel "time(s)"
plot 'hash1.txt' using 1:2 w l t 'hash size = 5000' lc rgb 'red'
replot 'hash2.txt' using 1:2 w l t 'hash size = 1000' lc rgb 'blue'
set terminal png
set output 'plot3.png'
replot 'hash3.txt' using 1:2 w l t 'hash size = 100' lc rgb 'green'
pause(-1)