set encoding iso_8859_1
set multiplot
#set xtics offset 0,graph -0.02
#set border 4095 lw 3
set lmargin 9
set bmargin 3
set size 0.94,0.9
set origin 0.05, 0.09
#set logscale x 10
#set logscale y 100
set tics font "Bold-Sans Serif, 28"
set xtics offset 0, -0.5   # Moves y-labels 2 character widths to the left
#set xtics offset 0,graph -0.015
#set xtics font "Sans Serif, 15"
#set ytics 0,0.4,0.8
#set ytics 0,0.002,0.008
#set ytics 0,2,8
set ytics 0,0.25,1
set xtics 0,0.25,1

set xlabel "({/CMMI10 \274}/4)^{-1}{/CMMI10 \265}" offset 0,-2.5,0 font "Sans Serif, 36"
#set ylabel "f({/CMMI10 \144})" offset 2,5,0 font "Sans Serif, 22"
#set ylabel "f_{gc}" offset 2,8.5,0 font "Sans Serif, 30"
set ylabel "P" offset -5,0,0 font "Sans Serif, 40"
#set key at screen 0.8,0.7 font "Sans Serif, 25"
#set label '{/CMMI10 \276}=4.73{\305}' offset 5.5,-1.3 font "Bold-Sans Serif, 14"
set key at screen 0.4,0.89 font "Sans Serif, 30"
#set yrange[0:0.8]
#set yrange[0:0.008]
set yrange[0:1]
#set yrange[0:8]
set xrange[0:1]
#set arrow from 10, graph 0 to 1, graph 1 nohead
#set arrow from 10,0 to 10,1 nohead
#set arrow from 2.56,-0.15 to 2.56,0.1 nohead

#set arrow from 10,0 to 10,5 nohead
#set arrow from 1.45,-0.05 to 1.45,0.1 nohead

#set arrow from 10,0 to 10,0.2 nohead
#set arrow from 1.45,-0.05 to 1.45,0.1 nohead
set label '(a)' at screen 0.17,0.35 font "Bold-Sans Serif, 30"
set label '(b)' at screen 0.63,0.56 font "Bold-Sans Serif, 30"
#set label '{/CMMI10 \265}_{T}' at screen 0.75,0.28 font "Bold-Sans Serif, 45" tc lt 9

plot 'hexa_48.txt' using 1:4 w lp pt 5 ps 2.2 lw 2 lc rgb "magenta" title 'N=48', 'hexa_70.txt' using 1:4 w lp pt 7 ps 2.5 lw 2 lc rgb "brown" title 'N=70', 'hexa_96.txt' using 1:4 w lp pt 9 ps 3.0 lw 2 lc rgb "blue" title 'N=96', 'hexa_126.txt' using 1:4 w lp pt 1 ps 3.2 lw 2 lc rgb "black" title 'N=126', 'hexa_240.txt' using 1:4 w lp pt 2 ps 3.2 lw 2 lc rgb "red" title 'N=240'

set size 0.435, 0.55
set origin 0.51, 0.16
#set key at screen 0.45,0.13
unset xlabel
unset ylabel
unset key
set tics font "Bold-Sans Serif, 26"
set xtics offset 0, -0.5   # Moves y-labels 2 character widths to the left
#set xlabel '({/CMMI10 \274}/4)^{-1}{/CMMI10 \265}' offset 20,0.09,0 font "Sans Serif, 28"
#set xlabel offset 8,1.4
#set ylabel 'f_{gc}' offset 3,6,0 font "Sans Serif, 25"
#set ylabel 'P' offset 3,6,0 font "Sans Serif, 30"
#set ylabel offset 4,2.8
set xtics 0.38,0.03,0.44
set mxtics 3           # Splits the 0.03 interval into 3 parts (0.01 steps)
set grid mxtics        # Draws grid lines on these new minor tics
set ytics 0.1,0.3,0.7
set xrange[0.38:0.44]
set yrange[0.08:0.7]
set grid xtics lt 0 lw 1.0 lc rgb "black"
set grid ytics lt 0 lw 1.0 lc rgb "black"
#set arrow from 0.4098,0.08 to 0.4102,0.7 nohead filled back lw 5 lc rgb "purple"
#set arrow from 0.4092,0.08 to 0.4092,0.7 nohead filled back lw 7 lc rgb "purple"

#plot "100_0.01_time_dynamics_sorted.txt" using 1:($2/10000) w lp lw 1.0 lc rgb "red" notitle, "200_0.01_time_dynamics_sorted.txt" using 1:($2/40000) w lp lw 1.0 lc rgb "blue" notitle

plot 'hexa_48_small.txt' using 1:4 w lp pt 5 ps 2.2 lw 2 lc rgb "magenta" notitle, 'hexa_70_small.txt' using 1:4 w lp pt 7 ps 2.5 lw 2 lc rgb "brown" notitle, 'hexa_96_small.txt' using 1:4 w lp pt 9 ps 3.0 lw 2 lc rgb "blue" notitle, 'hexa_126_small.txt' using 1:4 w lp pt 1 ps 3.2 lw 2 lc rgb "black" notitle, 'hexa_240_small.txt' using 1:4 w lp pt 2 ps 3.2 lw 2 lc rgb "red" notitle

unset grid
unset arrow

unset multiplot
