import sys
sys.path.append('./../')
import set_noise as my_noise

from c_solver.double_dot_sim_class import *
import c_solver.ME_solver as me 
import numpy as np
from qutip import hinton,matrix_histogram
import scipy
import os

np.set_printoptions(precision=2, linewidth=100)

def qobj_to_numpy(obj):
	return np.matrix([i[0] for i in (list(obj))])
def calc_concurrence(rho):
	rho = np.matrix(rho, dtype=np.complex)
	s = np.matrix([[0,0,0,-1], [0,0,1,0], [0,1,0,0], [-1,0,0,0]])
	R = rho*s*rho.T*s
	eig = np.sqrt(np.linalg.eigvals(R))
	max_1 = np.sort(eig)[3] - np.sum(np.sort(eig)[:3])
	if max_1 < 0:
		return 0
	else:
		return max_1

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
	if tc == True:
		db = double_dot_hamiltonian(19.7e9, 18.4e9, 850e9, 840e9, 0*0.250e9)
	else:
		db = double_dot_hamiltonian(19.7e9, 18.4e9, 850e9, 840e9, 0.250e9)

	# # # J = ~6MHZ @ epsilon 835e9, t = 210e6 // note a bit of assymetry, so you will get a tiny bit of phase
	chargingE = 850e9*np.pi*2
	detuningE = 828.6e9*np.pi*2

	# Number of simulation to average.
	num_sim = 500
	if noise == True:
		db = my_noise.add_nuclear_and_charge_noise(db)		
		db.number_of_sim_for_static_noise(num_sim)

	# Do MW on both qubits.
	if state == 0 or state == 3:
		db.mw_pulse(19.7e9,np.pi/2,2e6,0e-9,125e-9)
	else:
		db.mw_pulse(19.7e9,-np.pi/2,2e6,0e-9,125e-9)

	db.mw_pulse(18.4e9,np.pi/2,2e6,0e-9,125e-9)

	# If decoupled is used
	if dec == True:

		# implement tunnel coupling pulse.
		if tc == True:
			a = 49e-9
		else:
			a = 40e-9
		db.awg_pulse(detuningE/np.pi/2, 125e-9, 125e-9+a, 1e-9)
		if tc == True:
			db.awg_pulse_tc(0.25e9, 123e-9, 127e-9+a, 0.05e-9)

		db.mw_pulse(18.4e9,0,2e6,200e-9,450e-9)
		db.mw_pulse(19.7e9,0,2e6,200e-9,450e-9)
		db.awg_pulse(detuningE/np.pi/2, 450e-9, 450e-9+a, 1e-9)
		if tc == True:
			db.awg_pulse_tc(0.25e9, 448e-9, 452e-9+a, 0.05e-9)

		if state == 1 or state == 3: 
			db.mw_pulse(19.7e9, 0 ,2e6,500e-9,625e-9)
		else:
			db.mw_pulse(19.7e9, np.pi,2e6,500e-9,625e-9)

		db.calc_time_evolution(psi0, 0e-9, 625e-9, int((625e-9)*1e9*100))

	else:
		if tc == True:
			a = 91e-9
		else:
			a = 85e-9
		db.awg_pulse(detuningE/np.pi/2, 130e-9, 130e-9+a, 1e-9)
		if tc == True:
			db.awg_pulse_tc(0.25e9, 125e-9, 135e-9+a, 0.05e-9)


		if state == 1 or state == 3: 
			db.mw_pulse(19.7e9, 0 ,2e6,235e-9,360e-9)
		else:
			db.mw_pulse(19.7e9, np.pi,2e6,235e-9,360e-9)

		db.calc_time_evolution(psi0, 0e-9, 365e-9, int((625e-9)*1e9*100))

	rho =  db.get_density_matrix_final()[:4,:4]
	rho_full =  db.get_density_matrix_final()
	
	C = calc_concurrence(rho)
	bell_states = ['00','01','11','10']
	Bell = bell_state(bell_states[state])
	Bell.dims= [[4],[1]]

	F = (Bell.dag()*Qobj(rho)*Bell)[0,0]

	fig, ax = hinton(rho , ['00', '01', '10', '11'], ['00', '01', '10', '11'])
	plt.savefig('Bell_' + str(state) + '_hinton_dec_' +str(dec) + '_noise_' + str(noise) + "_tc_" + str(tc) + '.png')
	fig, ax = matrix_histogram(rho , ['00', '01', '10', '11'], ['00', '01', '10', '11'])
	plt.savefig('Bell_' + str(state) + '_hist_dec_' +str(dec) + '_noise_' + str(noise) + "_tc_" + str(tc) + '.png')
	np.savetxt('Bell_' + str(state) + "_dec_" + str(dec) + '_noise_' +str(noise) + '_tc_' + str(tc) + '_DM.txt', rho_full, header='density matrix data, 00,01,10,11,0S,S0')
	np.savetxt('Bell_' + str(state) + "_dec_" + str(dec) + '_noise_' +str(noise) + '_tc_' + str(tc) + '_FID.txt', np.array([F,C]), header = 'State overlap -- Concurrence')
	db.clear()


for state in [0,1,2,3]:
	for dec in [True, False]:
		for noise in [False, True]:
			for tc in [True, False]:
				path = "./Bell{}/dec_{}/".format(str(state), str(dec))
				if not os.path.exists(path):
				    os.makedirs(path)
				os.chdir(path)
				genertate_bell_state(state,noise, tc, dec)
				os.chdir('../../')


# plt.show()

