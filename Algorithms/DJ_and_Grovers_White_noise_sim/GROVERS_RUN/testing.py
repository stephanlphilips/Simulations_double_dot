import sys
sys.path.append('./../../')

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
	db = double_dot_hamiltonian(19.7e9, 18.4e9, 850e9, 840e9, 0.250e9)
	# # # J = 6MHZ @ epsilon 835e9, t = 210e6
	chargingE = 850e9*np.pi*2
	detuningE = 828.6e9*np.pi*2

	# Measured T2* values
	# 2us T2* qubit 1
	B_noise_1 = me.magnetic_noise_py()
	B_noise_1.init(db.H_B_field1,1.65e-6)

	# 2us T2* qubit 2
	B_noise_2 = me.magnetic_noise_py()
	B_noise_2.init(db.H_B_field2,0.75e-6)

	# Add noise object to simulation object.
	db.add_magnetic_noise_object(B_noise_1)
	db.add_magnetic_noise_object(B_noise_2)

	# Electrical noise ++ (static with realtionchip form the J plots).
	charge_noise = me.magnetic_noise_py()
	charge_noise.init(np.zeros([6,6],dtype=np.complex),0.615e-6)
	charge_noise.add_param_matrix_dep(db.H_B_field1*0.76 + 0.26*db.H_B_field2 - 0.18*db.H_B_field1*db.H_B_field2 , (4, 4), np.array([[0,1/detuningE],[0,chargingE]], dtype=np.complex))
	charge_noise.add_param_matrix_dep(db.H_B_field1*0.37 + 0.31*db.H_B_field2, (4, 4), np.array([[0,-1/detuningE],[0,chargingE-detuningE]], dtype=np.complex))

	db.add_magnetic_noise_object(charge_noise)
	db.number_of_sim_for_static_noise(samples)


	db.mw_pulse(19.7e9,np.pi/2,4.4e7,100e-9,213e-9)
	db.mw_pulse(18.4e9,np.pi/2,4.4e7,100e-9,213e-9)

	a =36e-9

	db.awg_pulse(detuningE/np.pi/2, 224e-9, 274e-9+a, 2e-9)

	db.mw_pulse(19.7e9,np.pi/2+phaseQ1,4.4e7,320e-9,434e-9)
	db.mw_pulse(18.4e9,np.pi/2+phaseQ2,4.4e7,320e-9,434e-9)

	db.awg_pulse(detuningE/np.pi/2, 443e-9, 493e-9+a, 2e-9)
	db.mw_pulse(19.7e9,np.pi+phaseQ1,4.4e7,538e-9,652e-9)
	db.mw_pulse(18.4e9,np.pi+phaseQ2,4.4e7,538e-9,652e-9)


	db.calc_time_evolution(psi0, 0e-9, 700e-9, 70000)
	# db.plot_expect()
	# db.plot_pop()

	db.save_pop("./../GROVERS_DATA/NORMAL/pop"+state+".txt")


grovers("00", False, 500)
grovers("01", False, 500)
grovers("10", False, 500)
grovers("11", False, 500)
