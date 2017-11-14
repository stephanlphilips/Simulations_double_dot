import sys
sys.path.append('./../../')
sys.path.append('./../')
import set_noise as noise

from c_solver.double_dot_sim_class import *
import c_solver.ME_solver as me 
import numpy as np

def grovers(state, show=False, samples= 1):
	if state == "00":
		phaseQ1 = np.pi/2
		phaseQ2 = np.pi/2
		file = "Grovers/Grovers1_data.txt"
	elif state == "01":
		phaseQ1 = np.pi/2
		phaseQ2 = -np.pi/2
		file = "Grovers/Grovers2_data.txt"
	elif state == "10":
		phaseQ1 = -np.pi/2
		phaseQ2 = np.pi/2
		file = "Grovers/Grovers3_data.txt"

	elif state == "11":
		phaseQ1 = -np.pi/2
		phaseQ2 = -np.pi/2
		file = "Grovers/Grovers4_data.txt"

	psi0= np.array(list(basis(6,0)*basis(6,0).dag()))[:,0]
	# define hamiltonian
	db = double_dot_hamiltonian(19.7e9, 18.4e9, 850e9, 840e9, 0*.250e9)
	# # # J = 6MHZ @ epsilon 835e9, t = 210e6
	chargingE = 850e9*np.pi*2
	detuningE = 828.6e9*np.pi*2

	if samples > 1:
		db = noise.add_nuclear_and_charge_noise(db)
		db.number_of_sim_for_static_noise(samples)


	db.mw_pulse(19.7e9,np.pi/2,2e6,100e-9,225e-9)
	db.mw_pulse(18.4e9,np.pi/2,2e6,100e-9,225e-9)

	a =35e-9

	db.awg_pulse(detuningE/np.pi/2, 225e-9, 275e-9+a, .5e-9)
	db.awg_pulse_tc(0.25e9, 223e-9, 280e-9+a, 0.05e-9)

	db.mw_pulse(19.7e9,np.pi/2+phaseQ1,2e6,320e-9,445e-9)
	db.mw_pulse(18.4e9,np.pi/2+phaseQ2,2e6,320e-9,445e-9)

	db.awg_pulse(detuningE/np.pi/2, 445e-9, 495e-9+a, .5e-9)
	db.awg_pulse_tc(0.25e9, 443e-9, 498e-9+a, 0.05e-9)
	db.mw_pulse(19.7e9,np.pi+phaseQ1,2e6,538e-9,663e-9)
	db.mw_pulse(18.4e9,np.pi+phaseQ2,2e6,538e-9,663e-9)


	db.calc_time_evolution(psi0, 0e-9, 700e-9, 70000)
	# db.plot_expect()
	# db.plot_pop()
	# plt.show()
	db.save_pop("./../GROVERS_DATA/NORMAL_tc/pop"+state+".txt")


grovers("00", False, 5000)
grovers("01", False, 5000)
grovers("10", False, 5000)
grovers("11", False, 5000)
