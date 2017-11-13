import sys
sys.path.append('./../')
import set_noise as my_noise

from c_solver.double_dot_sim_class import *
import c_solver.ME_solver as me 
import numpy as np
from qutip import hinton,matrix_histogram

np.set_printoptions(precision=2, linewidth=100)

def genertate_bell_state(state, noise, tc, dec):
	'''
	state [int]:
		0 : |00> + |11>
		1 : |00> - |11>
		2 : |01> - |10>
		3 : |01> + |10>
	noise [boolean]:
		add noise to the exp
	tc [boolean]:
		turn tunnelcoupling completely off when you do single qubit gates
	dec [boolean]: # not yet implemented.
		enable decoupled gate
	'''

	# Start in |00>
	psi0= np.array(list(basis(6,0)*basis(6,0).dag()))[:,0]

	# define hamiltonian
	db = double_dot_hamiltonian(19.7e9, 18.4e9, 850e9, 840e9, 0*0.250e9)

	# # # J = ~6MHZ @ epsilon 835e9, t = 210e6 // note a bit of assymetry, so you will get a tiny bit of phase
	chargingE = 850e9*np.pi*2
	detuningE = 828.6e9*np.pi*2


	db.mw_pulse(19.7e9,np.pi/2,2e6,0e-9,125e-9)
	# db.awg_pulse_tc(0.25e9, -10e-9, 127e-9, 0.05e-9)

	db.mw_pulse(19.7e9,0,2e6,125e-9,375e-9)
	db.mw_pulse(18.4e9,0,2e6,125e-9,375e-9)

	db.mw_pulse(19.7e9,-np.pi/2,2e6,375e-9,500e-9)
	# db.awg_pulse_tc(0.25e9, 375e-9, 5000e-9, 0.05e-9)



	db.calc_time_evolution(psi0, 0e-9, 500e-9, int((625e-9)*1e9*100))

	

	db.plot_pop()
	plt.show()
	print(np.abs(db.get_unitary()))
	print(np.angle(db.get_unitary(), deg=True))


genertate_bell_state(0,noise = False, tc = True, dec = True)

# for noise in [True, False]:
# 	for tc in [True, False]:
# 		for dec in [True, False]:
# 			for state in [0,1,2,3]:
# 				genertate_bell_state(state,noise, tc, dec)


plt.show()