#!/bin/bash


echo "plotting in eps format + converting to png ..."


cd ./DJ_DATA/NORMAL/
gnuplot plot.gnu
./convert_to_png.sh
cd ./../../
cd ./DJ_DATA/DEC_DOUBLE_X/
gnuplot plot_dec.gnu
./convert_to_png.sh
cd ./../../

echo "DJ Done!"

cd ./GROVERS_DATA/NORMAL/
gnuplot plot.gnu
./convert_to_png.sh
cd ./../../
cd ./GROVERS_DATA/DEC_SINGLE_X/
gnuplot plot_decoupled.gnu
./convert_to_png.sh
cd ./../../

echo "Grovers Done!"
