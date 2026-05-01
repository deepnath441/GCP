import matplotlib
matplotlib.use('Agg')   # no GUI

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from numpy import zeros,sqrt,ones,diff
import math
from scipy.interpolate import make_interp_spline

# -------- OPEN LOG FILE ----------
f_log = open('hexa_print_output_new.txt', 'w')

# -------- READ DATA ----------
f99 = open('theta_05_hexa.txt').readlines()
count_u99=int(len(f99))

neu=1.3

RMSD_limit=0.001

y=[]
x=[]

for u in range(1,count_u99):
    # Ensure lines aren't empty
    if not f99[u].strip(): continue 

    y.append((float(f99[u].split()[1])))

    temp_1=(-1.0)/(2.0*float(neu))
    temp=(float(f99[u].split()[0]))**temp_1
    x.append(float(temp))

# -------- INITIAL FIT ----------
fit=np.polyfit(x,y,1)
gradient=fit[0]
intercept=fit[1]

print("Initial fit:", gradient, intercept, file=f_log)

# -------- SLOPE SCAN ----------
a0 = gradient
a_center = round(a0, 3)

a_min = a_center - 0.1
a_max = a_center + 0.1
step = 0.001

results = []

best_rmsd = 1e9
best_a = 0
best_b = 0

Npts = len(x)

a = a_min
while a <= a_max + 1e-9:

    # ---- best intercept for this slope ----
    b = sum([y[i] - a*x[i] for i in range(Npts)]) / Npts

    # ---- RMSD ----
    err = sum([(y[i] - (a*x[i] + b))**2 for i in range(Npts)])
    rmsd = math.sqrt(err / Npts)

    results.append((a, b, rmsd))

    if rmsd < best_rmsd:
        best_rmsd = rmsd
        best_a = a
        best_b = b

    a += step

print("Best slope =", round(best_a,6), file=f_log)
print("Best intercept (theta_c) =", round(best_b,6), file=f_log)
print("Minimum RMSD =", round(best_rmsd,6), file=f_log)

# -------- SAVE SCAN RESULTS ----------
fscan = open('slope_scan_results_new.txt', 'w')
fscan.write("#slope\tintercept\tRMSD\n")

for a, b, r in results:
    fscan.write(f"{a:.6f}\t{b:.6f}\t{r:.6f}\n")

fscan.close()

# -------- ERROR BAR USING RMSD TOLERANCE ----------
slopes = np.array([r[0] for r in results])
intercepts = np.array([r[1] for r in results])
rmsds = np.array([r[2] for r in results])

rmin = np.min(rmsds)

# Condition: RMSD within limit of the minimum RMSD
mask = rmsds <= (rmin + RMSD_limit)

acceptable_slopes = slopes[mask]
acceptable_intercepts = intercepts[mask]

theta_min = np.min(acceptable_intercepts)
theta_max = np.max(acceptable_intercepts)

theta_error = (theta_max - theta_min) / 2.0

print("----------------------------------", file=f_log)
print("θ_c =", round(best_b,3), file=f_log)
print("θ_c range:", round(theta_min,3), round(theta_max,3), file=f_log)
print("Estimated error =", round(theta_error,3), file=f_log)
print("RMSD tolerance =", round(RMSD_limit,3), file=f_log)
print("----------------------------------", file=f_log)

# -------- SAVE FINAL RESULT ----------
f1 = open('percolation_threshold_theta_05_hexa_new.txt', 'w')
f1.write('#theta_c\t%f\t#gradient\t%f\t#error\t%f\n' % (best_b, best_a, theta_error))
f1.close()

# -------- BEST FIT LINE ----------
fit_eq=[]
for i in range(len(x)):
    fit_eq.append((best_a*x[i])+best_b)

min_x=round(min(x), 3)
max_x=round(max(x), 3)

min_y=round(min(y), 3)
max_y=round(max(y), 3)

# -------- PLOT MAIN ----------
plt.figure(figsize=(8, 6)) # Set a standard, proportional figure size

# Sort data so the connecting blue line doesn't zig-zag
sort_idx = np.argsort(x)
x_sorted = np.array(x)[sort_idx]
y_sorted = np.array(y)[sort_idx]
fit_eq_sorted = np.array(fit_eq)[sort_idx]

# --- EXTRAPOLATION LOGIC ---
# Extrapolate to x = 0 (Thermodynamic limit N -> infinity)
x_extrap = np.array([0, x_sorted[0]])
y_extrap = np.array([best_b, fit_eq_sorted[0]])

# Plot extrapolated dotted line and the intercept marker
plt.plot(x_extrap, y_extrap, color='r', linestyle=':', linewidth=3.0, label=r'Extrapolation ($N \to \infty$)')
plt.plot(0, best_b, 'go', markersize=10, label=r'$\theta_T = \theta_{th}|_{N \to \infty}$ Intercept')

# Annotate the intercept value with a bounding box and arrow
# Calculate the error as an integer at the 3rd decimal place
error_int = int(round(theta_error * 1000))

# Create the raw f-string with the parenthesis notation
annotation_text = rf"$\theta_T = {best_b:.3f}({error_int})$"

# Annotate the intercept value
bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="green", lw=1.5, alpha=0.9)
plt.annotate(annotation_text, 
             xy=(0, best_b), 
             xytext=(max(x_sorted) * 0.1, best_b), 
             ha="left", va="center", 
             fontsize=14, color="green", fontweight='bold',
             bbox=bbox_props,
             arrowprops=dict(arrowstyle="->", color="green", lw=1.5))
# ---------------------------

# Plot main lines and points with reasonable thicknesses
plt.plot(x_sorted, y_sorted, color='b', linewidth=3.0, label='Data')
plt.plot(x_sorted, y_sorted, 'o', color='b', markersize=10)
plt.plot(x_sorted, fit_eq_sorted, color='r', linewidth=3.0, label='Best Fit Line')

# Adjust x-axis limit slightly below 0 so the intercept marker is clearly visible
plt.xlim(left=-0.05 * max(x_sorted))

# Add descriptive labels (using raw strings for LaTeX formatting)
plt.xlabel(r"$N^{-1/(2\nu)}$", fontsize=16)
plt.ylabel(r"$\theta_{th}$", fontsize=16)

# Set reasonable tick font sizes and let matplotlib auto-space them
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Add a legend and a subtle grid for readability
plt.legend(fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)

# Ensure everything fits nicely without getting cut off
plt.tight_layout()

plt.savefig("theta_fit_hexa_new.png", dpi=300, bbox_inches='tight')

# -------- RMSD vs SLOPE ----------
plt.figure()
plt.plot(slopes, rmsds, 'k-')
plt.xlabel("Slope")
plt.ylabel("RMSD")
plt.savefig("rmsd_vs_slope_new.png", dpi=300, bbox_inches='tight')

# -------- CLOSE LOG FILE ----------
f_log.close()
