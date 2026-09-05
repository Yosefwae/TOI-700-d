import math
R=1.073
M=1.25
P_days=37.4
a_AU=0.1633
density_ratio=M/R**3
P_years=P_days/365.25
host_mass=a_AU**3/P_years**2
print(f"Relative bulk density: {density_ratio:.3f} Earth densities")
print(f"Simplified Kepler host-star mass: {host_mass:.3f} solar masses")
