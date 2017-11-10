import sys
sys.path.append('./../../')
from c_solver.double_dot_sim_class import *
import c_solver.ME_solver as me 

import numpy as np

def test_t2(noise_type):
	# define hamiltonian
	db = double_dot_hamiltonian(18.4e9, 19.7e9, 850e9, 840e9, 0*0.250e9)
	# # # J = 6MHZ @ epsilon 835e9, t = 210e6
	chargingE = 850e9*np.pi*2
	detuningE = 828.6e9*np.pi*2



	# Add noise to qubit 1
	B_noise_1 = me.noise_py()

	if noise_type == 'pink':
		B_noise_1.init_pink(db.H_B_field1,1e7,1)
	if noise_type == 'white':
		B_noise_1.init_white(db.H_B_field1,4e3)
	if noise_type == 'static_gauss':
		B_noise_1.init_gauss(db.H_B_field1,30e-9*np.sqrt(2))

	# Add noise object to simulation object.
	db.add_noise_object(B_noise_1)

	# Init wavefuntion
	psi0 = np.array(list(basis(6,0)*basis(6,0).dag()+basis(6,2)*basis(6,0).dag()+basis(6,0)*basis(6,2).dag()+basis(6,2)*basis(6,2).dag()))[:,0]/2

	# 5000 simulations to average.
	db.number_of_sim_for_static_noise(5000)
	db.calc_time_evolution(psi0, 0e-9, 100e-9, 500)
	db.plot_expect()

	x =  np.linspace(0, 100e-9, 500)
	if noise_type == 'white':
		y = np.exp(-x/31e-9)
		plt.plot(x*1e9,y, label='fit')
		plt.savefig('White_noise.png')
	if noise_type == 'static_gauss':
		y = np.exp(-(x/31e-9)**2)
		plt.plot(x*1e9,y, label='fit')
		plt.savefig('Static_gauss_noise.png')
	if noise_type == 'pink':
		y = np.exp(-(x/27e-9)**2)
		plt.plot(x*1e9,y, label='fit')
		plt.savefig('Pink_noise.png')
	plt.show()

test_t2('pink')
test_t2('static_gauss')
test_t2('white')

