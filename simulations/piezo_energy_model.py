# PiRo Piezoelectric Energy Model (Simplified)

import numpy as np
import matplotlib.pyplot as plt
import os
os.makedirs("results", exist_ok=True)

t = np.linspace(0, 10, 200)

force = 5 * np.sin(2 * np.pi * 0.5 * t) + 2 * np.random.randn(200)
d = 2e-12

Q = d * force
C = 1e-6
V = Q / C

frequency = 2
energy_per_cycle = 0.5 * C * V**2
power = energy_per_cycle * frequency

efficiency = 0.1
power_real = power * efficiency

print("Max Voltage:", np.max(V))
print("Max Power (W):", np.max(power_real))

plt.plot(t, power_real)
plt.title("PiRo Piezoelectric Power Output Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Power (W)")
plt.grid()
plt.savefig("results/power_output.png", dpi=300)
plt.show()

dt = t[1] - t[0]
# energy per step
energy_in = power_real * dt

# supercapacitor storage simulation
loss_factor = 0.98  # small continuous leakage
stored_energy = np.zeros_like(energy_in)

for i in range(1, len(energy_in)):
    stored_energy[i] = stored_energy[i-1] * loss_factor + energy_in[i]

plt.figure()
plt.plot(t, stored_energy)
plt.title("PiRo Supercapacitor Energy Storage Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Stored Energy (J)")
plt.grid()
plt.savefig("results/energy_storage.png", dpi=300)
plt.show()
