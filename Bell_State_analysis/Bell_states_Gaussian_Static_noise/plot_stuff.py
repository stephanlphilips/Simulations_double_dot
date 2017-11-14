import numpy as np
import qutip as qt
import h5py 
import matplotlib.pyplot as plt
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

def calc_overlap(rho,state):
	bell_states = ['00','01','11','10']
	Bell = qt.bell_state(bell_states[state])
	Bell.dims= [[4],[1]]

	return (Bell.dag()*qt.Qobj(rho)*Bell)[0,0]

def convert_matlab_mat_to_numpy(mat):
	return np.array([convert_line_to_complex(k) for k in mat])

def convert_line_to_complex(line):
	return [complex(k) for k in line.replace(' ','').replace('\n', '').replace('i', 'j').split(',')]

def save_fig(state, figname):
	fig, ax = qt.hinton(state , ['00', '01', '10', '11', ], ['00', '01', '10', '11', ])
	plt.savefig('state_hinton_' + str(figname)+ '.png' )
	fig, ax = qt.matrix_histogram(state , ['00', '01', '10', '11',], ['00', '01', '10', '11', ])
	plt.savefig('state_hist_' + str(figname)+ '.png' )
	np.savetxt('state_' + str(figname), state, header='density matrix data, 00,01,10,11')

b2 =  convert_matlab_mat_to_numpy(open('B1.txt'))
b1 =  convert_matlab_mat_to_numpy(open('B2.txt'))
b0 =  convert_matlab_mat_to_numpy(open('B3.txt'))
b3 =  convert_matlab_mat_to_numpy(open('B4.txt'))

Bell_states = [b0,b1,b2,b3]

for i in range(4):
	path = "./Bell{}/exp/".format(str(i))
	if not os.path.exists(path):
	    os.makedirs(path)
	os.chdir(path)
	save_fig(Bell_states[i], i)
	C = calc_concurrence(Bell_states[i])
	F = calc_overlap(Bell_states[i], i)
	np.savetxt('Bell_' + str(i) + '_FID.txt', np.array([F,C]), header = 'State overlap -- Concurrence')

	os.chdir('../../')


