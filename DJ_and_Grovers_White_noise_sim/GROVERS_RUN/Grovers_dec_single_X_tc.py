import sys
sys.path.append("./../../")
sys.path.append('./../')
import set_noise as noise

from c_solver.double_dot_sim_class import *
import c_solver.ME_solver as me 
import numpy as np
def grovers(state, show=False, samples= 1):
	if state == "00":
		phaseQ1 = np.pi
		phaseQ2 = np.pi
		file = "Grovers/Grovers1_data.txt"
	elif state == "01":
		phaseQ1 = 0
		phaseQ2 = np.pi
		file = "Grovers/Grovers2_data.txt"
	elif state == "10":
		phaseQ1 = np.pi
		phaseQ2 = 0
		file = "Grovers/Grovers3_data.txt"

	elif state == "11":
		phaseQ1 = 0
		phaseQ2 = 0
		file = "Grovers/Grovers4_data.txt"


	psi0= np.array(list(basis(6,0)*basis(6,0).dag()))[:,0]

	# # define hamiltonian
	db = double_dot_hamiltonian(18.4e9, 19.7e9, 850e9, 840e9, 0*0.250e9)
	# # # J = 6MHZ @ epsilon 835e9, t = 210e6
	chargingE = 850e9*np.pi*2
	detuningE = 828.6e9*np.pi*2

	if samples > 1:
		db = noise.add_nuclear_and_charge_noise(db)
		db.number_of_sim_for_static_noise(samples)

	# YY
	db.mw_pulse(18.4e9,np.pi/2,2.5e6,100e-9,199e-9)
	db.mw_pulse(19.7e9,np.pi/2,2.5e6,100e-9,199e-9)

	a =49e-9

	# CPHASE
	db.awg_pulse(detuningE/np.pi/2, 200e-9, 200e-9+a, 1e-9)
	db.awg_pulse_tc(0.25e9, 195e-9, 205e-9+a, 0.05e-9)
	db.mw_pulse(18.4e9,0,2.5e6,250e-9,449e-9)
	db.mw_pulse(19.7e9,0,2.5e6,250e-9,449e-9)
	db.awg_pulse(detuningE/np.pi/2, 450e-9, 450e-9+a, 1e-9)
	db.awg_pulse_tc(0.25e9, 445e-9, 455e-9+a, 0.05e-9)

	# YY
	db.mw_pulse(18.4e9,np.pi+phaseQ1,2.5e6,500e-9,599e-9)
	db.mw_pulse(19.7e9,np.pi+phaseQ2,2.5e6,500e-9,599e-9)

	# CPHASE
	db.awg_pulse(detuningE/np.pi/2, 600e-9, 600e-9+a, 1e-9)
	db.awg_pulse_tc(0.25e9, 595e-9, 605e-9+a, 0.05e-9)
	db.mw_pulse(18.4e9,np.pi/2,2.5e6,650e-9,849e-9)
	db.mw_pulse(19.7e9,np.pi/2,2.5e6,650e-9,849e-9)
	db.awg_pulse(detuningE/np.pi/2, 850e-9, 850e-9+a, 1e-9)
	db.awg_pulse_tc(0.25e9, 845e-9, 855e-9+a, 0.05e-9)

	# YY
	db.mw_pulse(18.4e9,-np.pi/2+phaseQ2,2.5e6,900e-9,999e-9)
	db.mw_pulse(19.7e9,-np.pi/2+phaseQ1,2.5e6,900e-9,999e-9)


	db.calc_time_evolution(psi0, 0e-9, 1000e-9, 100000)

	
	db.save_pop("./../GROVERS_DATA/DEC_SINGLE_X_tc/pop"+state+"_single.txt")
	# db.save_purities("Grovers/pur" + state)
	# plt.figure(1)

	if show == True:
		db.plot_expect()
		db.plot_pop()
		plt.show()


grovers("00", False, 5000)
grovers("01", False, 5000)
grovers("10", False, 5000)
grovers("11", False, 5000)
