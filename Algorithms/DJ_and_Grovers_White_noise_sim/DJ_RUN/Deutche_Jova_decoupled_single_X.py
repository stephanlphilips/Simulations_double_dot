import sys
sys.path.append('./../../')
sys.path.append('./../')

from c_solver.double_dot_sim_class import *
import c_solver.ME_solver as me 
import set_noise as noise

import numpy as np

def Deutche_Jova(func,num_sim=1000):
	

	psi0= np.array(list(basis(6,0)*basis(6,0).dag()))[:,0]
	# define hamiltonian
	db = double_dot_hamiltonian(19.7e9, 18.4e9, 850e9, 840e9, 0.210e9)
	# # # J = 6MHZ @ epsilon 835e9, t = 210e6
	chargingE = 850e9*np.pi*2
	detuningE = 835e9*np.pi*2
	if num_sim > 1:
		db = noise.add_nuclear_and_charge_noise(db)
		db.number_of_sim_for_static_noise(num_sim)


	db.mw_pulse(18.4e9,0,2.5e6,50e-9,150e-9)
	db.mw_pulse(19.7e9,np.pi,2.5e6,50e-9,150e-9)

	if func == 'Iden':
		phase_qb1 = 0
		phase_qb2 = 0
		extra_time = 0
	if func == 'NOT':
		db.mw_pulse(19.7e9,np.pi/2,2.5e6,150e-9,350e-9)
		phase_qb1 = 0
		phase_qb2 = 0
		extra_time = 10e-9

	if func == 'CNOT':
		a =40e-9
		db.mw_pulse(19.7e9,0,2.5e6,150e-9,250e-9)
		db.awg_pulse(detuningE/np.pi/2, 250e-9, 250e-9+a, 1e-9)
		db.mw_pulse(18.4e9,0,2.5e6,300e-9,509e-9)
		db.mw_pulse(19.7e9,0,2.5e6,300e-9,509e-9)
		db.awg_pulse(detuningE/np.pi/2, 500e-9, 500e-9+a, 1e-9)

		db.mw_pulse(19.7e9,np.pi/2,2.5e6,550e-9,650e-9)
		phase_qb1 = np.pi/2
		phase_qb2 = -np.pi/2
		extra_time= 250e-9 +a

	if func == 'CNOT_low':
		a =40e-9
		db.mw_pulse(19.7e9,np.pi,2.5e6,150e-9,250e-9)
		db.awg_pulse(detuningE/np.pi/2, 250e-9, 250e-9+a, 1e-9)
		db.mw_pulse(18.4e9,0,2.5e6,300e-9,509e-9)
		db.mw_pulse(19.7e9,0,2.5e6,300e-9,509e-9)
		db.awg_pulse(detuningE/np.pi/2, 500e-9, 500e-9+a, 1e-9)

		db.mw_pulse(19.7e9,np.pi/2,2.5e6,550e-9,650e-9)
		phase_qb1 = -np.pi/2
		phase_qb2 = np.pi/2
		extra_time= 250e-9 +a


	db.mw_pulse(18.4e9,np.pi + phase_qb1,2.5e6,350e-9+extra_time,450e-9+extra_time)
	db.mw_pulse(19.7e9,0 + phase_qb2,2.5e6,350e-9+extra_time,450e-9+extra_time)

	db.calc_time_evolution(psi0, 0e-9, 800e-9, 40000)
	# db.plot_expect()
	# db.plot_pop()
	
	# plt.show()

	db.save_pop("./../DJ_DATA/DEC_SINGLE_X/pop_"+func+"_single.txt")
	# db.save_purities("Deutche_Jova/" + func)
	# plt.figure(1)
	# plt.savefig("Deutche_Jova/"+func+"_pop.pdf")
	# plt.clf()
	# plt.figure(2)
	# plt.savefig("Deutche_Jova/"+func+"_exp.pdf")
	# plt.clf()

Deutche_Jova('Iden',5000)
Deutche_Jova('NOT',5000)
Deutche_Jova('CNOT',5000)
Deutche_Jova('CNOT_low',5000)


