# feature to be deployed to master by pull request

import numpy as np
import scipy.constants as sc

h_no_bar = sc.h
print('-------------------------------------------------------------------')

print('Here we are going to learn what happens with the *bar constants')
print('- First h bar:')
print('--- h is the Planck constant')

print('--- h bar is equals to',h_no_bar/(2*np.pi))

h_bar = sc.hbar

print('--- this is Scipy result:',h_bar)

print('-------------------------------------------------------------------')

print('- Now Lambda bar:')
lambda_green = 520e-9
print('--- for green light Lambda is arround', lambda_green/1e-9,'nm →',lambda_green,'m')
print('--- so, Lambda bar will be', lambda_green/(2*np.pi),'m')
