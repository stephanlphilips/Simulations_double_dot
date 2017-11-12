from c_solver.double_dot_sim_class import *
import c_solver.ME_solver as me 
import numpy as np
def grovers(state, show=False, samples= 1):
	if state == "00":
		phaseQ1 = 0
		phaseQ2 = 0
		file = "Grovers/Grovers1_data.txt"
	elif state == "01":
		phaseQ1 = np.pi
		phaseQ2 = 0
		file = "Grovers/Grovers2_data.txt"
	elif state == "10":
		phaseQ1 = 0
		phaseQ2 = np.pi
		file = "Grovers/Grovers3_data.txt"

	elif state == "11":
		phaseQ1 = np.pi
		phaseQ2 = np.pi
		file = "Grovers/Grovers4_data.txt"


	psi0= np.array(list(basis(6,0)*basis(6,0).dag()))[:,0]

	# # define hamiltonian
	db = double_dot_hamiltonian(18.4e9, 19.7e9, 850e9, 840e9, 0.210e9)
	# # # J = 6MHZ @ epsilon 835e9, t = 210e6
	chargingE = 850e9*np.pi*2
	detuningE = 835e9*np.pi*2

	# Measured T2* values
	# 1.7us T2* qubit 1, 0.5us if detuned
	B_noise_1 = me.magnetic_noise_py()
	B_noise_1.init(db.H_B_field1,1.65e-6)
	# B_noise_1.add_param_dep((4, 4), np.array([[0,-((1.7e-6/0.5e-6) -1)/detuningE],[0,chargingE]], dtype=np.complex))

	# 0.7us T2* qubit 2, 0.5us if detuned
	B_noise_2 = me.magnetic_noise_py()
	B_noise_2.init(db.H_B_field2,0.75e-6)
	# B_noise_2.add_param_dep((4, 4), np.array([[0,-((0.7e-6/0.5e-6) -1)/detuningE],[0,chargingE]], dtype=np.complex))

	# Add noise object to simulation object.
	db.add_magnetic_noise_object(B_noise_1)
	db.add_magnetic_noise_object(B_noise_2)

	# Electrical noise ++ (static with realtionchip form the J plots).
	charge_noise = me.magnetic_noise_py()
	charge_noise.init(np.zeros([6,6],dtype=np.complex),0.615e-6)
	charge_noise.add_param_matrix_dep(db.H_B_field1*0.66 + 0.19*db.H_B_field2 + 0.15*db.H_B_field1*db.H_B_field2 , (4, 4), np.array([[0,1/detuningE],[0,chargingE]], dtype=np.complex))

	db.add_magnetic_noise_object(charge_noise)

	db.number_of_sim_for_static_noise(samples)

	# YY
	db.mw_pulse(18.4e9,np.pi/2,5e7,100e-9,199e-9)
	db.mw_pulse(19.7e9,np.pi/2,5e7,100e-9,199e-9)

	a =49e-9

	# CPHASE
	db.mw_pulse(18.4e9,0,5e7,200e-9,399e-9)
	db.mw_pulse(19.7e9,0,5e7,200e-9,399e-9)
	db.awg_pulse(detuningE/np.pi/2, 400e-9, 400e-9+a, 1e-9)
	db.mw_pulse(18.4e9,0,5e7,450e-9,649e-9)
	db.mw_pulse(19.7e9,0,5e7,450e-9,649e-9)
	db.awg_pulse(detuningE/np.pi/2, 650e-9, 650e-9+a, 1e-9)

	# YY
	db.mw_pulse(18.4e9,np.pi+phaseQ1,5e7,700e-9,799e-9)
	db.mw_pulse(19.7e9,np.pi+phaseQ2,5e7,700e-9,799e-9)

	# CPHASE
	db.mw_pulse(18.4e9,np.pi/2,5e7,800e-9,999e-9)
	db.mw_pulse(19.7e9,np.pi/2,5e7,800e-9,999e-9)
	db.awg_pulse(detuningE/np.pi/2, 1000e-9, 1000e-9+a, 1e-9)
	db.mw_pulse(18.4e9,np.pi/2,5e7,1050e-9,1249e-9)
	db.mw_pulse(19.7e9,np.pi/2,5e7,1050e-9,1249e-9)
	db.awg_pulse(detuningE/np.pi/2, 1250e-9, 1250e-9+a, 1e-9)

	# YY
	db.mw_pulse(18.4e9,-np.pi/2+phaseQ2,5e7,1300e-9,1399e-9)
	db.mw_pulse(19.7e9,-np.pi/2+phaseQ1,5e7,1300e-9,1399e-9)


	db.calc_time_evolution(psi0, 0e-9, 1400e-9, 1400*50)

	db.plot_expect()
	db.plot_pop()
	db.save_pop("Grovers/pop"+state+"_double.txt")
	db.save_purities("Grovers/pur" + state)
	plt.figure(1)
	states_averages= np.loadtxt(file)

	if show == True:
		plt.show()


grovers("00", False, 5000)
grovers("01", False, 5000)
grovers("10", False, 5000)
grovers("11", False, 5000)
