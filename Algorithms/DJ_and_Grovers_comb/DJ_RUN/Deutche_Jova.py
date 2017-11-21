import sys
sys.path.append('./../../')
sys.path.append('./../')
from c_solver.double_dot_sim_class import *
import c_solver.ME_solver as me 
import set_noise as noise
import numpy as np

def Deutche_Jova(func,num_sim=1000):
	psi0= np.array(list(basis(6,0)*basis(6,0).dag()))[:,0]
	# psi0= np.array(list(basis(6,0)*basis(6,0).dag()+basis(6,1)*basis(6,0).dag()+basis(6,0)*basis(6,1).dag()+basis(6,1)*basis(6,1).dag()))[:,0]/2

	# define hamiltonian
	db = double_dot_hamiltonian(18.4e9, 19.7e9, 850e9, 840e9,0.250e9)
	# # # J = 6MHZ @ epsilon 835e9, t = 210e6
	chargingE = 850e9*np.pi*2
	detuningE = 828.6e9*np.pi*2
	if num_sim >1:
		db = noise.add_nuclear_and_charge_noise(db)

		db.number_of_sim_for_static_noise(num_sim)

	db.mw_pulse(18.4e9,0,2e6,50e-9,175e-9)
	db.mw_pulse(19.7e9,np.pi,2e6,50e-9,175e-9)

	if func == 'Iden':
		phase_qb1 = 0
		phase_qb2 = 0
		extra_time = 0e-9
	if func == 'NOT':
		db.mw_pulse(19.7e9,-np.pi/2,2e6,175e-9,425e-9)
		phase_qb1 = 0
		phase_qb2 = 0
		extra_time = 50e-9

	if func == 'CNOT':
		a =35e-9
		db.mw_pulse(19.7e9,np.pi,2e6,175e-9,300e-9)
		db.awg_pulse(detuningE/np.pi/2, 310e-9, 360e-9+a, 1e-9)
		db.mw_pulse(19.7e9,-np.pi/2,2e6,405e-9,530e-9)
		phase_qb1 = -np.pi/2
		phase_qb2 = -np.pi/2
		extra_time= 155e-9 

	if func == 'CNOT_low':
		a =35e-9
		db.mw_pulse(19.7e9,0,2e6,175e-9,300e-9)
		db.awg_pulse(detuningE/np.pi/2, 310e-9, 360e-9+a, 1e-9)
		db.mw_pulse(19.7e9,-np.pi/2,2e6,405e-9,530e-9)
		phase_qb1 = np.pi/2
		phase_qb2 = np.pi/2
		extra_time= 155e-9

	db.mw_pulse(18.4e9,np.pi + phase_qb1,2e6,375e-9+extra_time,500e-9+extra_time)
	db.mw_pulse(19.7e9,0 + phase_qb2,2e6,375e-9+extra_time,500e-9+extra_time)

	db.calc_time_evolution(psi0, 0e-9, 700e-9, 70000)

	db.save_pop("./../DJ_DATA/NORMAL/pop_"+func+".txt")

	if num_sim < 1:
		db.plot_pop()
		plt.show()
	#db.save_purities("Deutche_Jova/" + func)


Deutche_Jova('Iden',5000)
Deutche_Jova('NOT',5000)
Deutche_Jova('CNOT',5000)
Deutche_Jova('CNOT_low',5000)