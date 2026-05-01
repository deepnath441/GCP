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
set key at screen 0.38,0.9 font "Sans Serif, 30"
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
set label '(b)' at screen 0.6,0.56 font "Bold-Sans Serif, 30"
#set label '{/CMMI10 \265}_{T}' at screen 0.736,0.25 font "Bold-Sans Serif, 45" tc lt 9

plot 'square_36.txt' using 1:4 w lp pt 5 ps 2.2 lw 2 lc rgb "orange" title 'N=36', 'square_49.txt' using 1:4 w lp pt 7 ps 2.5 lw 2 lc rgb "magenta" title 'N=49', 'square_64.txt' using 1:4 w lp pt 9 ps 3 lw 2 lc rgb "brown" title 'N=64', 'square_81.txt' using 1:4 w lp pt 2 ps 3.2 lw 2 lc rgb "black" title 'N=81', 'square_100.txt' using 1:4 w lp pt 1 ps 3.2 lw 2 lc rgb "blue" title 'N=100', 'square_225.txt' using 1:4 w lp pt 3 ps 3.2 lw 2 lc rgb "red" title 'N=225'

set size 0.49, 0.55
set origin 0.46, 0.17
#set key at screen 0.45,0.13
unset xlabel
unset ylabel
unset key
set tics font "Bold-Sans Serif, 26"
set xtics offset 0, -0.5   # Moves y-labels 2 character widths to the left
#set xlabel '({/CMMI10 \274}/4)^{-1}{/CMMI10 \265}' offset 13,0.09,0 font "Sans Serif, 28"
#set xlabel offset 8,1.4
#set ylabel 'f_{gc}' offset 3,6,0 font "Sans Serif, 25"
#set ylabel 'P' offset 3,6,0 font "Sans Serif, 30"
#set ylabel offset 4,2.8
set xtics 0.31,0.03,0.37
set mxtics 3           # Splits the 0.03 interval into 3 parts (0.01 steps)
set grid mxtics        # Draws grid lines on these new minor tics
set ytics 0.1,0.3,0.7
set xrange[0.31:0.37]
set yrange[0.08:0.7]
set grid xtics lt 0 lw 1.0 lc rgb "black"
set grid ytics lt 0 lw 1.0 lc rgb "black"
#set arrow from 0.344,0.08 to 0.344,0.7 nohead filled back lw 5 lc rgb "purple"
#set arrow from 0.3425,0.08 to 0.3425,0.7 nohead filled back lw 7 lc rgb "purple"

#plot "100_0.01_time_dynamics_sorted.txt" using 1:($2/10000) w lp lw 1.0 lc rgb "red" notitle, "200_0.01_time_dynamics_sorted.txt" using 1:($2/40000) w lp lw 1.0 lc rgb "blue" notitle

plot 'square_36_small.txt' using 1:4 w lp pt 5 ps 2.5 lw 2 lc rgb "orange" notitle, 'square_49_small.txt' using 1:4 w lp pt 7 ps 2.7 lw 2 lc rgb "magenta" notitle, 'square_64_small.txt' using 1:4 w lp pt 9 ps 3.0 lw 2 lc rgb "brown" notitle, 'square_81_small.txt' using 1:4 w lp pt 2 ps 3.2 lw 2 lc rgb "black" notitle, 'square_100_small.txt' using 1:4 w lp pt 1 ps 3.2 lw 2 lc rgb "blue" notitle, 'square_225_small.txt' using 1:4 w lp pt 3 ps 3.2 lw 2 lc rgb "red" notitle

#set arrow from 0.343,0.08 to 0.344,0.7 nohead filled back lw 5 lc rgb "purple"

unset grid
unset arrow

unset multiplot
