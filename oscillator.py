import numpy as np
import matplotlib.pyplot as plt

# ============================================
# SIMPLE HARMONIC OSCILLATOR
# Equation: x'' + omega^2 * x = 0
# Solution: x(t) = A * cos(omega*t + phi)
# ============================================

# Parameters — try changing these and see what happens
omega = 2.0   # angular frequency (rad/s)
A     = 1.0   # amplitude (m)
phi   = 0.0   # initial phase (rad)
gamma1 = 0.1
gamma2 = 0.7
gamma3 = 2.0
F = 1.0
omega_d1 = 1.0   # below natural frequency
omega_d2 = 2.0   # exactly at natural frequency — RESONANCE
omega_d3 = 3.0   # above natural frequency
# Time array
t = np.linspace(0, 50, 5000)

# Solution
x = A * np.cos(omega * t + phi)
v = -A * omega * np.sin(omega * t + phi)
# for Decaying envelop 
x1 = A* np.exp(-gamma1*t)*np.cos(omega*t)
x2 = A* np.exp(-gamma2*t)*np.cos(omega*t)
x3 = A* np.exp(-gamma3*t)*np.cos(omega*t)

#Resonance 
# Amplitude of steady state response
def amplitude(omega_d):
    return F/ np.sqrt((omega**2 - omega_d**2)**2 + (0.1*omega_d)**2)

X1 = amplitude(omega_d1) * np.cos(omega_d1 * t)
X2 = amplitude(omega_d2) * np.cos(omega_d2 * t)
X3 = amplitude(omega_d3) * np.cos(omega_d3 * t)

# # Plot
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10, 26))

ax1.plot(t, x, color='royalblue', linewidth=2)
ax1.set_ylabel("Position x (m)")
ax1.set_title("Simple Harmonic Oscillator — Act 1: Pure Oscillation")
ax1.axhline(0, color='gray', linewidth=0.5)
ax1.grid(True, alpha=0.3)

ax2.plot(t, v, color='crimson', linewidth=2)
ax2.set_ylabel("Velocity v (m/s)")
ax2.set_xlabel("Time t (s)")
ax2.axhline(0, color='gray', linewidth=0.5)
ax2.grid(True, alpha=0.3)

#decaying envelope

ax3.plot(t, x1, label="Underdamped y=0.1", color='royalblue')
ax3.plot(t, x2, label="Critically damped y=0.7", color='crimson')
ax3.plot(t, x3, label="Overdamped y=2.0", color='green')
ax3.set_ylabel("Position x (m)")
ax3.set_xlabel("Time t (s)")
ax3.set_title("Act 2: Damped Oscillation")
ax3.legend(loc='upper right')
ax3.grid(True, alpha=0.3)
ax3.axhline(0, color='gray', linewidth=0.5)

# Resonance

ax4.plot(t, X1, label=f"wd=1.0 below", color='royalblue')
ax4.plot(t, X2, label=f"wd=2.0 RESONANCE", color='crimson')
ax4.plot(t, X3, label=f"wd=3.0 above", color='green')
ax4.set_ylabel("Position x (m)")
ax4.set_xlabel("Time t (s)")
ax4.set_title("Act 3: Resonance")
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout(pad = 3.0)
plt.subplots_adjust(hspace=0.7, top = 0.95)
plt.savefig("act1_pure_oscillation.png", dpi=150)
plt.show()