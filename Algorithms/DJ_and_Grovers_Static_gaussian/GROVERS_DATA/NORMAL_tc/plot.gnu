set terminal postscript eps size 6,4 enhanced color \
    font 'Helvetica,18' linewidth 2

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
set output 'Grovers00.eps'
set key box opaque
set yrange [-0.1:1.1]
set xrange [0:720]
plot 'Grovers1_data.txt' u ($1-200):2:($6) w errorbars title "00" ls 1 ,\
	'Grovers1_data.txt' u ($1-200):3:($7) w errorbars title "01" ls 2,\
	'Grovers1_data.txt' u ($1-200):4:($8) w errorbars title "10" ls 3,\
	'Grovers1_data.txt' u ($1-200):5:($9) w errorbars title "11" ls 4,\
	'pop00.txt' u ($1*1e9):2 w l notitle ls 1,\
	'pop00.txt' u ($1*1e9):3 w l notitle ls 2,\
	'pop00.txt' u ($1*1e9):4 w l notitle ls 3,\
	'pop00.txt' u ($1*1e9):5 w l notitle ls 4

set output 'Grovers01.eps'
plot 'Grovers3_data.txt' u ($1-200):2:($6) w errorbars title "00" ls 1 ,\
	'Grovers3_data.txt' u ($1-200):3:($7) w errorbars title "01" ls 2,\
	'Grovers3_data.txt' u ($1-200):4:($8) w errorbars title "10" ls 3,\
	'Grovers3_data.txt' u ($1-200):5:($9) w errorbars title "11" ls 4,\
	'pop01.txt' u ($1*1e9):2 w l notitle ls 1,\
	'pop01.txt' u ($1*1e9):3 w l notitle ls 2,\
	'pop01.txt' u ($1*1e9):4 w l notitle ls 3,\
	'pop01.txt' u ($1*1e9):5 w l notitle ls 4,\

set output 'Grovers10.eps'
plot 'Grovers2_data.txt' u ($1-200):2:($6) w errorbars title "00" ls 1 ,\
	'Grovers2_data.txt' u ($1-200):3:($7) w errorbars title "01" ls 2,\
	'Grovers2_data.txt' u ($1-200):4:($8) w errorbars title "10" ls 3,\
	'Grovers2_data.txt' u ($1-200):5:($9) w errorbars title "11" ls 4,\
	'pop10.txt' u ($1*1e9):2 w l notitle ls 1,\
	'pop10.txt' u ($1*1e9):3 w l notitle ls 2,\
	'pop10.txt' u ($1*1e9):4 w l notitle ls 3,\
	'pop10.txt' u ($1*1e9):5 w l notitle ls 4,\


set output 'Grovers11.eps'
plot 'Grovers4_data.txt' u ($1-200):2:($6) w errorbars title "00" ls 1 ,\
	'Grovers4_data.txt' u ($1-200):3:($7) w errorbars title "01" ls 2,\
	'Grovers4_data.txt' u ($1-200):4:($8) w errorbars title "10" ls 3,\
	'Grovers4_data.txt' u ($1-200):5:($9) w errorbars title "11" ls 4,\
	'pop11.txt' u ($1*1e9):2 w l notitle ls 1,\
	'pop11.txt' u ($1*1e9):3 w l notitle ls 2,\
	'pop11.txt' u ($1*1e9):4 w l notitle ls 3,\
	'pop11.txt' u ($1*1e9):5 w l notitle ls 4,\

