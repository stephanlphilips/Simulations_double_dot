sh ./Algorithms/DJ_and_Grovers_Static_gaussian/execute_all.sh
sh ./Algorithms/DJ_and_Grovers_Static_gaussian/plot_all.sh
sh ./Algorithms/DJ_and_Grovers_White_noise_sim/execute_all.sh
sh ./Algorithms/DJ_and_Grovers_White_noise_sim/plot_all.sh
sh ./Algorithms/DJ_and_Grovers_comb/execute_all.sh
sh ./Algorithms/DJ_and_Grovers_comb/plot_all.sh

python ./Bell_State_analysis/Bell_states_white_noise_sim/simfile.py
python ./Bell_State_analysis/Bell_states_white_noise_sim/plot_stuff.py

python ./Bell_State_analysis/Bell_states_comb_noise/simfile.py
python ./Bell_State_analysis/Bell_states_comb_noise/plot_stuff.py

python ./Bell_State_analysis/Bell_states_Gaussian_Static_noise/simfile.py
python ./Bell_State_analysis/Bell_states_Gaussian_Static_noise/plot_stuff.py

