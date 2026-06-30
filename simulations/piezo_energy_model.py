# PiRo Piezoelectric Energy Model (Simplified)

import numpy as np

# Parameters (simplified assumptions)
t = np.linspace(0, 10, 200)

force = 5 * np.sin(2 * np.pi * 0.5 * t) + 2 * np.random.randn(200)  # N (fluid-induced force)
d = 2e-12  # piezoelectric coefficient (C/N)

# Charge generated
Q = d * force  # Coulombs

# Voltage approximation (assume small capacitance)
C = 1e-6  # Farads
V = Q / C

# Power estimation (very simplified)
frequency = 2  # Hz (wave motion)
energy_per_cycle = 0.5 * C * V**2
power = energy_per_cycle * frequency

print("Max Voltage:", np.max(V))
print("Max Power (W):", np.max(power))

import matplotlib.pyplot as plt

plt.plot(t, power)
plt.title("PiRo Piezoelectric Power Output vs Force")
plt.xlabel("Force (N)")
plt.ylabel("Power (W)")
plt.grid()
plt.show()
