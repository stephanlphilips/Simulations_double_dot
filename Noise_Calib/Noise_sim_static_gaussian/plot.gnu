set terminal postscript eps size 4.5,2.7 enhanced color \
    font 'Helvetica,18' linewidth 2


set style line 1 lc rgb '#5BB6E6' lt 1 lw 2 pt 7 ps 0.4
set style line 2 lc rgb '#E49D25' lt 1 lw 2 pt 5 ps 0.4
set style line 3 lc rgb '#1074B0' lt 3 lw 2
set style line 4 lc rgb '#169D74' lt 3 lw 2
set style line 5 lc rgb '#F0E252' lt 1 lw 2 pt 7 ps 0.01
set style line 6 lc rgb '#2A707F' lt 1 lw 2 pt 7 ps 0.01
set style line 7 lc rgb '#7F0000' lt 1 lw 2 pt 7 ps 0.01
set style line 8 lc rgb '#9C06CC' lt 1 lw 2 pt 7 ps 0.01


set output "DephD410_r.eps"

set xlabel 'time (us)'
set ylabel 'Probablility amplitude (%)'
set yrange[0:1]
set xrange[0:3]
tau = 1.2e-6
omega = 3e6
phi = -2.1

f(x) = 2.7182818284590452353**(-(x*1e-6)/tau)*sin(2*3.14*omega*(x*1e-6) + phi)/2 +0.5

f(x) = 2.7182818284590452353**(-1*((x*1e-6)/tau)**2/2)*sin(2*3.14*omega*(x*1e-6) + phi)/2 +0.5


# fit f(x) 'DephD410_r.txt' u ($1*1e6):5 via tau, omega, phi
set samples 500
set xrange [0:]
plot 'DephD410_r.txt' u ($1*1e6):2 w lp ls 1 title '00',\
	 'DephD410_r.txt' u ($1*1e6):3 w lp ls 2 title '01',\
	 'DephD410_r.txt' u ($1*1e6):4 w lp ls 3 title '10',\
	 'DephD410_r.txt' u ($1*1e6):5 w lp ls 4 title '11',\
	 f(x) w l ls 5 title 'fit'
# plot f(x) w l ls 5 title 'fit'