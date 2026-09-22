import numpy as np
import matplotlib.pyplot as plt

# Prerequisites
tol = 1e-6
max_iter = 100

# We declare f(x)
def f(x):
    return x**3 + x - 1

# We declare g(x) 
def g(x):
    return np.cbrt(1.0 - x) # cube root
    
# 1. Fixed-Point Iteration Method function
def GEM(x0):
    x_k = [x0]
    err = []
    for i in range(max_iter):
        x_next = g(x0)
        x_k.append(x_next)
        err.append(np.abs(x_next - x0)) 
        
        if np.abs(x_next - x0) < tol:
            break
        x0 = x_next
        
    return x_k, err

# 2. 
x_k, errors = GEM(1e-15)

iterations = range(len(errors))

plt.plot(iterations, errors, label='errors')
plt.xlabel('loops')
plt.ylabel('errors')
plt.title('GEM Method for f(x)= x^3 + x - 1 and g(x)=(1-x)^(1/3)')
plt.grid()
plt.legend()
plt.show()

# 3. 
e_k2 = errors[- 1]
e_k1 = errors[- 2]
e_k  = errors[- 3]

p_k = (np.log(e_k2 / e_k1) / np.log(e_k1 / e_k)) 
C_k = e_k2 / ((e_k1)**p_k)

print('pk = ', p_k)
print('Ck = ', C_k)