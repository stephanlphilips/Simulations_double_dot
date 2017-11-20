import sys
sys.path.append('./../')
import set_noise as noise

from c_solver.double_dot_sim_class import *
import c_solver.ME_solver as me 
import numpy as np

def expected_value(t, T2_electric,right_qubit = True, num_sim=500):
	psi0= np.array(list(basis(6,0)*basis(6,0).dag()))[:,0]
	# define hamiltonian
	db = double_dot_hamiltonian(19.7e9, 18.4e9, 850e9, 840e9, 0.250e9)
	# # # J = 6MHZ @ epsilon 835e9, t = 210e6
	chargingE = 850e9*np.pi*2
	detuningE = 828.6e9*np.pi*2

	t /= 2
	db = noise.add_nuclear_and_charge_noise(db)
	
	db.number_of_sim_for_static_noise(num_sim)

	if right_qubit == True:
		db.mw_pulse(19.7e9,0,2e6,0e-9,125e-9)
	else:
		db.mw_pulse(18.4e9,0,2e6,0e-9,125e-9)



	db.awg_pulse(detuningE/np.pi/2, 125e-9, 125e-9 + t, 1e-9)

	db.mw_pulse(19.7e9,0,2e6,125e-9+t,375e-9+t)
	db.mw_pulse(18.4e9,0,2e6,125e-9+t,375e-9+t)

	db.awg_pulse(detuningE/np.pi/2, 375e-9+t, 375e-9+2*t, 1e-9)
	
	if right_qubit == True:
		db.mw_pulse(19.7e9,0,2e6,375e-9+2*t,500e-9+2*t)
	else:
		db.mw_pulse(18.4e9,0,2e6,375e-9+2*t,500e-9+2*t)


	db.calc_time_evolution(psi0, 0e-9, 500e-9+2*t, int((500e-9+2*t)*1e9*100))
	# db.plot_pop()
	# plt.show()
	# # raise

	rho =  db.get_density_matrix_final()
	db.clear()
	pop_00 = np.real(rho[0,0])
	pop_01 = np.real(rho[1,1])
	pop_10 = np.real(rho[2,2])
	pop_11 = np.real(rho[3,3])

	return np.array([pop_00, pop_01, pop_10, pop_11])
	# db.save_pop("./../GROVERS_DATA/NORMAL/pop"+state+".txt")

a= expected_value(1.69e-6, 820e-9, right_qubit=False)
print(a)
# density = 80
# pt = np.linspace(0e-6, 3e-6,density)
# data = np.zeros([density,5])

# # Qubit 1
# for i in range(density):
# 	data[i,0] = pt[i]
# 	data[i,1:] = expected_value(pt[i], 410e-9, right_qubit=False)
# 	np.savetxt('DephD410_r.txt', data)

# for i in range(density):
# 	data[i,0] = pt[i]
# 	data[i,1:] = expected_value(pt[i], 400e-9)
# 	np.savetxt('DephD400.txt', data)

# for i in range(density):
# 	data[i,0] = pt[i]
# 	data[i,1:] = expected_value(pt[i], 500e-9)
# 	np.savetxt('DephD500.txt', data)

# for i in range(density):
# 	data[i,0] = pt[i]
# 	data[i,1:] = expected_value(pt[i], 600e-9)
# 	np.savetxt('DephD600.txt', data)

# plt.plot(data[:,0],data[:,1])
# plt.plot(data[:,0],data[:,2])
# plt.plot(data[:,0],data[:,3])
# plt.plot(data[:,0],data[:,4])
# plt.show()

# np.savetxt('DephD.txt', data)

# # qubit  2
# for i in range(density):
# 	data[i,0] = pt[i]
# 	data[i,1:] = expected_value(pt[i], False)

# np.savetxt('DDeph.txt', data)
