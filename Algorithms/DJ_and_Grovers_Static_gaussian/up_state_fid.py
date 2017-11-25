import sys
sys.path.append('./../../')
sys.path.append('./../')
from c_solver.double_dot_sim_class import *
import c_solver.ME_solver as me 
import set_noise as noise
import numpy as np


psi0= np.array(list(basis(6,0)*basis(6,0).dag()))[:,0]
db = double_dot_hamiltonian(18.4e9, 19.7e9, 850e9, 840e9,0*0.250e9)
db = noise.add_nuclear_and_charge_noise(db)
db.number_of_sim_for_static_noise(5000)

db.mw_pulse(19.7e9,0,2e6,0e-9,250e-9)
db.calc_time_evolution(psi0, 0e-9, 250e-9, 25000)

rho = np.diagonal(db.get_density_matrix_final()[:4,:4])
print(rho)

DM1 = db.get_unitary()
np.savetxt('DM1.txt', DM1)

psi0= np.array(list(basis(6,0)*basis(6,0).dag()))[:,0]
db = double_dot_hamiltonian(18.4e9, 19.7e9, 850e9, 840e9,0.250e9)
db = noise.add_nuclear_and_charge_noise(db)
db.number_of_sim_for_static_noise(5000)

db.mw_pulse(18.4e9,0,2e6,0e-9,250e-9)
db.calc_time_evolution(psi0, 0e-9, 250e-9, 25000)

rho = np.diagonal(db.get_density_matrix_final()[:4,:4])
print(rho)

DM2 = db.get_unitary()
np.savetxt('DM1.txt', DM2)

# db.plot_pop()
# plt.show()