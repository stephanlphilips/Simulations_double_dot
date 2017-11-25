cd ./Algorithms/DJ_and_Grovers_Static_gaussian/
./execute_all.sh
./plot_all.sh

cd ./../../
echo "${PWD}"
cd ./Algorithms/DJ_and_Grovers_White_noise_sim/
./execute_all.sh
./plot_all.sh

cd ./../../
cd ./Algorithms/DJ_and_Grovers_comb/
./execute_all.sh
./plot_all.sh

cd ./../../
cd ./Bell_State_analysis/Bell_states_white_noise_sim/
python simfile.py
python plot_stuff.py

cd ./../../
cd ./Bell_State_analysis/Bell_states_comb_noise/
python simfile.py
python plot_stuff.py

cd ./../../
cd ./Bell_State_analysis/Bell_states_Gaussian_Static_noise/
python simfile.py
python plot_stuff.py

cd ./../../
