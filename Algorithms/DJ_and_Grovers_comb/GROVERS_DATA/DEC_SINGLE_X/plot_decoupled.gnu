set terminal postscript eps size 5,3 enhanced color \
    font 'Helvetica,24' linewidth 2

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
set output 'Grovers_dec_00.eps'
# set key box opaque
set yrange [-0.1:1.1]
set xrange [0:1100]
plot 'pop00_single.txt' u ($1*1e9):2 w l title '00' ls 1,\
	'pop00_single.txt' u ($1*1e9):4 w l title '10' ls 2,\
	'pop00_single.txt' u ($1*1e9):3 w l title '01' ls 3,\
	'pop00_single.txt' u ($1*1e9):5 w l title '11' ls 4,\
	'Grovers1_data_dec.txt' u ($1*1e9+1050):4 w p notitle ls 1 ,\
	'Grovers1_data_dec.txt' u ($1*1e9+1050):5 w p notitle ls 2,\
	'Grovers1_data_dec.txt' u ($1*1e9+1050):6 w p notitle ls 3,\
	'Grovers1_data_dec.txt' u ($1*1e9+1050):7 w p notitle ls 4
	
set output 'Grovers_dec_01.eps'
plot 'pop01_single.txt' u ($1*1e9):2 w l title '00' ls 1,\
	'pop01_single.txt' u ($1*1e9):4 w l title '10' ls 2,\
	'pop01_single.txt' u ($1*1e9):3 w l title '01' ls 3,\
	'pop01_single.txt' u ($1*1e9):5 w l title '11' ls 4,\
	'Grovers2_data_dec.txt' u ($1*1e9+1050):4 w p notitle ls 1 ,\
	'Grovers2_data_dec.txt' u ($1*1e9+1050):5 w p notitle ls 2,\
	'Grovers2_data_dec.txt' u ($1*1e9+1050):6 w p notitle ls 3,\
	'Grovers2_data_dec.txt' u ($1*1e9+1050):7 w p notitle ls 4

set output 'Grovers_dec_10.eps'
plot 'pop10_single.txt' u ($1*1e9):2 w l title '00' ls 1,\
	'pop10_single.txt' u ($1*1e9):4 w l title '10' ls 2,\
	'pop10_single.txt' u ($1*1e9):3 w l title '01' ls 3,\
	'pop10_single.txt' u ($1*1e9):5 w l title '11' ls 4,\
	'Grovers3_data_dec.txt' u ($1*1e9+1050):4 w p notitle ls 1 ,\
	'Grovers3_data_dec.txt' u ($1*1e9+1050):5 w p notitle ls 2,\
	'Grovers3_data_dec.txt' u ($1*1e9+1050):6 w p notitle ls 3,\
	'Grovers3_data_dec.txt' u ($1*1e9+1050):7 w p notitle ls 4


set output 'Grovers_dec_11.eps'
plot 'pop11_single.txt' u ($1*1e9):2 w l title '00' ls 1,\
	'pop11_single.txt' u ($1*1e9):4 w l title '10' ls 2,\
	'pop11_single.txt' u ($1*1e9):3 w l title '01' ls 3,\
	'pop11_single.txt' u ($1*1e9):5 w l title '11' ls 4,\
	'Grovers4_data_dec.txt' u ($1*1e9+1050):4 w p notitle ls 1 ,\
	'Grovers4_data_dec.txt' u ($1*1e9+1050):5 w p notitle ls 2,\
	'Grovers4_data_dec.txt' u ($1*1e9+1050):6 w p notitle ls 3,\
	'Grovers4_data_dec.txt' u ($1*1e9+1050):7 w p notitle ls 4
