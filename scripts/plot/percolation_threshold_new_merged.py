# Finite size scaling to calculate \theta_T (Figure 8)

import matplotlib
matplotlib.use('Agg')   # no GUI

import matplotlib.pyplot as plt
import numpy as np
import math

# -------- CONFIGURATION ----------
neu = 1.3
RMSD_limit = 0.001 # tolerance to calculate error term

# Define the lattices, their corresponding files, and plot colors
lattices = [
    {'name': 'Hexagonal',  'file': 'theta_05_hexa.txt',   'color': 'blue'},
    {'name': 'Square',     'file': 'theta_05_square.txt', 'color': 'red'},
    {'name': 'Triangular', 'file': 'theta_05_tri.txt',    'color': 'green'}
]

# -------- OPEN COMBINED LOG FILE ----------
f_log = open('combined_print_output.txt', 'w')

# -------- INITIALIZE FIGURES ----------
fig_main, ax_main = plt.subplots(figsize=(10, 8))
fig_rmsd, ax_rmsd = plt.subplots(figsize=(8, 6))

global_max_x = 0  

# -------- PROCESS EACH LATTICE ----------
for lat in lattices:
    print(f"=== Processing {lat['name']} Lattice ===", file=f_log)
    
    # 1. READ DATA
    try:
        lines = open(lat['file']).readlines()
    except FileNotFoundError:
        print(f"Warning: {lat['file']} not found. Skipping.", file=f_log)
        continue

    y = []
    x = []
    for line in lines[1:]: 
        if not line.strip(): continue 
        
        parts = line.split()
        y.append(float(parts[1]))
        
        temp_1 = (-1.0) / (2.0 * float(neu))
        temp = (float(parts[0]))**temp_1
        x.append(float(temp))
        
    x = np.array(x)
    y = np.array(y)
    
    global_max_x = max(global_max_x, np.max(x))

    # 2. INITIAL FIT
    fit = np.polyfit(x, y, 1)
    gradient = fit[0]
    intercept = fit[1]

    # 3. SLOPE SCAN
    a_center = round(gradient, 3)
    a_min = a_center - 0.1
    a_max = a_center + 0.1
    step = 0.001

    results = []
    best_rmsd = 1e9
    best_a, best_b = 0, 0
    Npts = len(x)

    a = a_min
    while a <= a_max + 1e-9:
        b = np.sum(y - a*x) / Npts
        err = np.sum((y - (a*x + b))**2)
        rmsd = math.sqrt(err / Npts)
        results.append((a, b, rmsd))

        if rmsd < best_rmsd:
            best_rmsd = rmsd
            best_a, best_b = a, b
        a += step

    # 4. ERROR CALCULATION
    slopes = np.array([r[0] for r in results])
    intercepts = np.array([r[1] for r in results])
    rmsds = np.array([r[2] for r in results])

    rmin = np.min(rmsds)
    mask = rmsds <= (rmin + RMSD_limit)

    acceptable_intercepts = intercepts[mask]
    theta_error = (np.max(acceptable_intercepts) - np.min(acceptable_intercepts)) / 2.0
    error_int = int(round(theta_error * 1000))

    # 5. PLOTTING - MAIN FIGURE
    sort_idx = np.argsort(x)
    x_sorted = x[sort_idx]
    y_sorted = y[sort_idx]
    fit_eq_sorted = best_a * x_sorted + best_b

    c = lat['color']
    #legend_str = rf"{lat['name']} ($\theta_T = {best_b:.3f}({error_int})$)"
    legend_str = rf"{lat['name']}"

    # Extrapolation (dotted) and intercept (triangle)
    x_extrap = np.array([0, x_sorted[0]])
    y_extrap = np.array([best_b, fit_eq_sorted[0]])
    # Extrapolation (dotted) and intercept (triangle)
    ax_main.plot(x_extrap, y_extrap, color=c, linestyle=':', linewidth=2.5)
    # Added clip_on=False to keep the full triangle visible at x=0
    ax_main.plot(0, best_b, marker='^', color=c, markersize=12, zorder=5, clip_on=False)

    # Data points and fit lines
    ax_main.plot(x_sorted, y_sorted, 'o', color=c, markersize=12)
    ax_main.plot(x_sorted, fit_eq_sorted, color=c, linewidth=2.5, label=legend_str)

    # 6. PLOTTING - RMSD FIGURE
    ax_rmsd.plot(slopes, rmsds, label=lat['name'], color=c)

# -------- FINALIZE MAIN PLOT ----------
# START X AXIS EXACTLY FROM 0.0
ax_main.set_xlim(left=0.0, right=global_max_x * 1.05)

ax_main.set_xlabel(r"$N^{-1/(2\nu)}$", fontsize=35, labelpad=15)
ax_main.set_ylabel(r"$\theta_{th}$", fontsize=35)
ax_main.tick_params(axis='both', which='major', labelsize=25)
ax_main.grid(True, linestyle='--', alpha=0.6)

# ==========================================
# FULLY CUSTOMIZABLE LEGEND
# ==========================================
ax_main.legend(
    loc='center right',             
    bbox_to_anchor=(0.9, 0.7),  
    fontsize=20,                  
    ncol=1,                       
    frameon=True,                 
    fancybox=False,               
    edgecolor='black',            
    facecolor='white',            
    framealpha=0.9,               
    shadow=False,                 
    borderpad=0.8,                
    labelspacing=0.6,             
    handlelength=2.5,             
    handletextpad=0.8,            
    markerscale=1.2               
)

fig_main.tight_layout()
fig_main.savefig("theta_fit_combined.png", dpi=300, bbox_inches='tight')

# -------- FINALIZE RMSD PLOT ----------
ax_rmsd.set_xlabel("Slope", fontsize=18)
ax_rmsd.set_ylabel("RMSD", fontsize=18)
ax_rmsd.tick_params(axis='both', which='major', labelsize=14)
ax_rmsd.grid(True, linestyle='--', alpha=0.6)
ax_rmsd.legend(fontsize=14, loc='upper center')

fig_rmsd.tight_layout()
fig_rmsd.savefig("rmsd_vs_slope_combined.png", dpi=300, bbox_inches='tight')

f_log.close()
