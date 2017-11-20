import sys
sys.path.append('./../../')
from c_solver.double_dot_sim_class import *
import c_solver.ME_solver as me 

import numpy as np


def add_nuclear_and_charge_noise(sim_object):
	'''
	Adds the niose to the simulation. Configured to be:
		T2* for J oscillations  1.6 us if white, 
								1.2 us if static gaussian
	T2* qubit 1 = 1 us
	T2* qubit 2 = 0.6 us 
	''' 

	# # # J = 6MHZ @ epsilon 835e9, t = 210e6
	chargingE = 850e9*np.pi*2
	detuningE = 828.6e9*np.pi*2
	
	# T2* qubit 1 -- nuclear
	B_noise_1 = me.noise_py()
	B_noise_1.init_gauss(sim_object.H_B_field1,1.1e-6)

	# T2* qubit 2 -- nuclear
	B_noise_2 = me.noise_py()
	B_noise_2.init_gauss(sim_object.H_B_field2,0.75e-6)

	# Add noise object to simulation object.
	sim_object.add_noise_object(B_noise_1)
	sim_object.add_noise_object(B_noise_2)

	# Electrical noise ++ (static with realtionchip form the J plots). --- note here everything expressed in form of pauli matrices and not spin matrices (bi)
	charge_noise = me.noise_py()
	charge_noise.init_white(np.zeros([6,6],dtype=np.complex), 1.08e3)
	charge_noise.add_param_matrix_dep(sim_object.H_B_field1*2.4 + 0.78*sim_object.H_B_field2 + sim_object.H_B_field1*sim_object.H_B_field2, (4,4), np.array([[0,-1/detuningE],[0,chargingE]], dtype=np.complex))
	charge_noise.add_param_matrix_dep(sim_object.H_B_field1*0.45 + 0.93*sim_object.H_B_field2, (4, 4), np.array([[0,1/detuningE],[0,chargingE-detuningE]], dtype=np.complex))

	sim_object.add_noise_object(charge_noise)

	return sim_object