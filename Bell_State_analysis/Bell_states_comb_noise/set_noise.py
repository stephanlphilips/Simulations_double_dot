import sys
sys.path.append('./../../../')
from c_solver.double_dot_sim_class import *
import c_solver.ME_solver as me 

import numpy as np



def add_nuclear_and_charge_noise(sim_object, T2_gauss=1.2e-6, T2_white=0.7e3):
	# Adds the noise. Charge noise is taken so T2* of J oscillations is 1.6us.

	# # # J = 6MHZ @ epsilon 835e9, t = 210e6
	chargingE = 850e9*np.pi*2
	detuningE = 828.6e9*np.pi*2
	
	# T2* qubit 1 -- nuclear
	B_noise_1 = me.noise_py()
	B_noise_1.init_gauss(sim_object.H_B_field1,1.12e-6)

	# T2* qubit 2 -- nuclear
	B_noise_2 = me.noise_py()
	B_noise_2.init_gauss(sim_object.H_B_field2,0.75e-6)

	# Add noise object to simulation object.
	sim_object.add_noise_object(B_noise_1)
	sim_object.add_noise_object(B_noise_2)

	# Electrical noise ++ (static with realtionchip form the J plots). --- note here everything expressed in form of pauli matrices and not spin matrices (bi)
	# Gaussian noise
	charge_noise1 = me.noise_py()
	charge_noise1.init_gauss(np.zeros([6,6],dtype=np.complex),T2_gauss)
	charge_noise1.add_param_matrix_dep(2.4*sim_object.H_B_field1 + 0.78*sim_object.H_B_field2 + sim_object.H_B_field1*sim_object.H_B_field2 , (4, 4), np.array([[0,1/detuningE],[0,chargingE]], dtype=np.complex))
	charge_noise1.add_param_matrix_dep(0.45*sim_object.H_B_field1 + 0.93*sim_object.H_B_field2, (4, 4), np.array([[0,-1/detuningE],[0,chargingE-detuningE]], dtype=np.complex))

	sim_object.add_noise_object(charge_noise1)
	
	# White noise
	charge_noise2 = me.noise_py()
	charge_noise2.init_white(np.zeros([6,6],dtype=np.complex), T2_white)
	charge_noise2.add_param_matrix_dep(sim_object.H_B_field1*2.4 + 0.78*sim_object.H_B_field2 + sim_object.H_B_field1*sim_object.H_B_field2, (4,4), np.array([[0,-1/detuningE],[0,chargingE]], dtype=np.complex))
	charge_noise2.add_param_matrix_dep(sim_object.H_B_field1*0.45 + 0.93*sim_object.H_B_field2, (4, 4), np.array([[0,1/detuningE],[0,chargingE-detuningE]], dtype=np.complex))
	sim_object.add_noise_object(charge_noise2)



	return sim_object

def test_t2():
	# T2*= 1 us (qubit 2)
	psi0= np.array(list(basis(6,0)*basis(6,0).dag()+basis(6,2)*basis(6,0).dag()+basis(6,0)*basis(6,2).dag()+basis(6,2)*basis(6,2).dag()))[:,0]/2
	# T2*= 0.6 us (qubit 2)
	# psi0= np.array(list(basis(6,0)*basis(6,0).dag()+basis(6,1)*basis(6,0).dag()+basis(6,0)*basis(6,1).dag()+basis(6,1)*basis(6,1).dag()))[:,0]/2

	# define hamiltonian
	db = double_dot_hamiltonian(18.4e9, 19.7e9, 850e9, 840e9, 0*0.250e9)
	# # # J = 6MHZ @ epsilon 835e9, t = 210e6
	chargingE = 850e9*np.pi*2
	detuningE = 828.6e9*np.pi*2

	db = add_nuclear_and_charge_noise(db)
	db.number_of_sim_for_static_noise(2000)
	db.calc_time_evolution(psi0, 0e-9, 1000e-9, 500)
	db.plot_expect()
	db.plot_pop()
	
	plt.show()

test_t2()