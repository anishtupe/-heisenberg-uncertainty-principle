import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


hbar = 1 


def gaussian_position(x, sigma_x):
    return (1/(sigma_x * np.sqrt(2 * np.pi))) * np.exp(-x**2 / (2 * sigma_x**2))


def gaussian_momentum(p, sigma_p):
    return (1/(sigma_p * np.sqrt(2 * np.pi))) * np.exp(-p**2 / (2 * sigma_p**2))


sigma_x = 1
sigma_p = hbar / (2 * sigma_x)  


x = np.linspace(-5, 5, 400)
p = np.linspace(-5, 5, 400)
X, P = np.meshgrid(x, p)

psi_x = gaussian_position(X, sigma_x)
psi_p = gaussian_momentum(P, sigma_p)


fig = plt.figure(figsize=(14, 7))

 
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, P, psi_x, cmap='viridis')
ax1.set_title('Position Probability Density')
ax1.set_xlabel('Position x')
ax1.set_ylabel('Arbitrary Axis')
ax1.set_zlabel('Probability Density')


ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, P, psi_p, cmap='plasma')
ax2.set_title('Momentum Probability Density')
ax2.set_xlabel('Arbitrary Axis')
ax2.set_ylabel('Momentum p')
ax2.set_zlabel('Probability Density')

plt.tight_layout()
plt.show()