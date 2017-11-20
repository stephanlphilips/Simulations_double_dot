set terminal postscript eps size 5,3 enhanced color \
    font 'Helvetica,22' linewidth 2

set style line 1 lc rgb '#1074B0' lt 1 lw 1.3 pt 7 ps 0.8
set style line 2 lc rgb '#169D74' lt 1 lw 1.3 pt 7 ps 0.8
set style line 3 lc rgb '#5BB6E6' lt 1 lw 1.3 pt 7 ps 0.8
set style line 4 lc rgb '#E49D25' lt 1 lw 1.3 pt 7 ps 0.8
set style line 5 lc rgb '#F0E252' lt 1 lw 1.3 pt 7 ps 0.8
set style line 6 lc rgb '#2A707F' lt 1 lw 1.3 pt 7 ps 0.8
set style line 7 lc rgb '#7F0000' lt 1 lw 1.3 pt 7 ps 0.8
set style line 8 lc rgb '#9C06CC' lt 1 lw 1.3 pt 7 ps 0.8


set xlabel 'time (ns)'
set ylabel 'Population (%)'
set key box opaque
unset key
set yrange [-0.1:1.1]
set xrange [0 :600]
set output 'DJ1_IDEN.eps'
plot 'DJ1_data.txt' u ($1-100):2 title "00" ls 1 ,\
	'DJ1_data.txt' u ($1-100):3 title "01" ls 2,\
	'DJ1_data.txt' u ($1-100):4 title "10" ls 3,\
	'DJ1_data.txt' u ($1-100):5 title "11" ls 4,\
	'pop_Iden.txt' u ($1*1e9):2 w l notitle ls 1,\
	'pop_Iden.txt' u ($1*1e9):3 w l notitle ls 2,\
	'pop_Iden.txt' u ($1*1e9):4 w l notitle ls 3,\
	'pop_Iden.txt' u ($1*1e9):5 w l notitle ls 4
set xrange [0:700]
set output 'DJ2_CNOT.eps'
plot 'DJ2_data.txt' u ($1-100):($2) title "00" ls 1 ,\
	'DJ2_data.txt' u ($1-100):($3) title "01" ls 2,\
	'DJ2_data.txt' u ($1-100):($4) title "10" ls 3,\
	'DJ2_data.txt' u ($1-100):($5) title "11" ls 4,\
	'pop_CNOT.txt' u ($1*1e9):2 w l notitle ls 1,\
	'pop_CNOT.txt' u ($1*1e9):3 w l notitle ls 2,\
	'pop_CNOT.txt' u ($1*1e9):4 w l notitle ls 3,\
	'pop_CNOT.txt' u ($1*1e9):5 w l notitle ls 4
set xrange [0 :600]
set output 'DJ3_NOT.eps'
plot 'DJ3_data.txt' u ($1-100):($2/1.0) title "00" ls 1 ,\
	'DJ3_data.txt' u ($1-100):($3/1.0) title "01" ls 2,\
	'DJ3_data.txt' u ($1-100):($4/1.0) title "10" ls 3,\
	'DJ3_data.txt' u ($1-100):($5/1.0) title "11" ls 4,\
	'pop_NOT.txt' u ($1*1e9):2 w l notitle ls 1,\
	'pop_NOT.txt' u ($1*1e9):3 w l notitle ls 2,\
	'pop_NOT.txt' u ($1*1e9):4 w l notitle ls 3,\
	'pop_NOT.txt' u ($1*1e9):5 w l notitle ls 4

set xrange [0 :700]
set output 'DJ4_CNOT_low.eps'
plot 'DJ4_data.txt' u ($1-100):($2) title "00" ls 1 ,\
	'DJ4_data.txt' u ($1-100):($3) title "01" ls 2,\
	'DJ4_data.txt' u ($1-100):($4) title "10" ls 3,\
	'DJ4_data.txt' u ($1-100):($5) title "11" ls 4,\
	'pop_CNOT_low.txt' u ($1*1e9):2 w l notitle ls 1,\
	'pop_CNOT_low.txt' u ($1*1e9):3 w l notitle ls 2,\
	'pop_CNOT_low.txt' u ($1*1e9):4 w l notitle ls 3,\
	'pop_CNOT_low.txt' u ($1*1e9):5 w l notitle ls 4
