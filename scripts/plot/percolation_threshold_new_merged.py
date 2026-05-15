import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import math

# -------- CONFIGURATION ----------
neu = 1.3
#neu = 1.7, 0.9
RMSD_limit = 0.001

lattices = [
    {'name': 'Square',     'file': 'theta_05_square.txt', 'color': 'red'},
    {'name': 'Triangular', 'file': 'theta_05_tri.txt',    'color': 'green'},
    {'name': 'Hexagonal',  'file': 'theta_05_hexa.txt',   'color': 'blue'},
]

f_log = open('combined_print_output.txt', 'w')

# -------- OUTPUT FILE ----------
out = open(f"fit_results_nu_{neu}.txt", "w")
out.write("Lattice\tSlope\tIntercept\n")

# -------- CREATE 3 SUBPLOTS ----------
#fig, axes = plt.subplots(3, 1, figsize=(6, 18))
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

for idx, lat in enumerate(lattices):

    ax = axes[idx]

    print(f"=== Processing {lat['name']} Lattice ===", file=f_log)

    try:
        lines = open(lat['file']).readlines()
    except FileNotFoundError:
        print(f"Warning: {lat['file']} not found. Skipping.", file=f_log)
        continue

    y, x = [], []

    for line in lines[1:]:
        if not line.strip():
            continue

        parts = line.split()
        y.append(float(parts[1]))
        x.append((float(parts[0]))**((-1.0)/(2.0*neu)))

    x = np.array(x)
    y = np.array(y)

    # -------- FIT (CLEAN VERSION) ----------
    best_a, best_b = np.polyfit(x, y, 1)

    # -------- WRITE OUTPUT ----------
    out.write(f"{lat['name']}\t{best_a:.6f}\t{best_b:.6f}\n")

    # -------- SORT ----------
    sort_idx = np.argsort(x)
    x_sorted = x[sort_idx]
    y_sorted = y[sort_idx]

    fit_eq_sorted = best_a * x_sorted + best_b

    c = lat['color']

    # -------- EXTRAPOLATION ----------
    x_extrap = np.array([0, x_sorted[0]])
    y_extrap = np.array([best_b, fit_eq_sorted[0]])

    ax.plot(x_extrap, y_extrap, color=c, linestyle=':', linewidth=2.5)
    ax.plot(0, best_b, marker='^', color=c, markersize=18,
            zorder=5, clip_on=False)

    # -------- DATA + FIT ----------
    ax.plot(x_sorted, y_sorted, 'o', color=c, markersize=15)
    ax.plot(x_sorted, fit_eq_sorted, color=c, linewidth=2.5,
            label=lat['name'])

    # -------- AXIS ----------
    ax.set_xlim(left=0.0, right=max(x_sorted)*1.05)

    ax.set_xlabel(r"$N^{-1/(2\nu)}$", fontsize=32, labelpad=10)
    if idx == 0:
        ax.set_ylabel(r"$\theta_{th}$", fontsize=32)

    ax.tick_params(axis='both', labelsize=22)
    ax.tick_params(axis='x', pad=10)
    ax.grid(True, linestyle='--', alpha=0.6)

    # -------- LEGEND (ONE PER PANEL) ----------
    ax.legend(loc='lower right', fontsize=30, frameon=True)
    
    panel_labels = ['(a)', '(b)', '(c)']

    ax.text(0.15, 0.7, panel_labels[idx],
        transform=ax.transAxes,
        fontsize=30,
        fontweight='bold')

ytick_ranges = [
    (0.34, 0.37, 0.01),   # for (a) Square
    (0.30, 0.33, 0.01),   # for (b) Triangular
    (0.40, 0.43, 0.01)    # for (c) Hexagonal
]

#xtick_ranges = [
#    (0.0, 0.2, 0.1),   # for (a) Square
#    (0.0, 0.2, 0.1),   # for (b) Triangular
#    (0.0, 0.2, 0.1)    # for (c) Hexagonal
#]

# -------- SAVE ----------
for idx, ax in enumerate(axes):
    start, end, step = ytick_ranges[idx]
    ax.set_yticks(np.arange(start, end + step, step))
    
#for idx, ax in enumerate(axes):
#    start, end, step = xtick_ranges[idx]
#    ax.set_xticks(np.arange(start, end + step, step))

#for ax in axes:
#    xmin, xmax = ax.get_xlim()
#    ax.set_xticks(np.linspace(xmin, xmax, 4))

for ax in axes:
    ax.set_xticks([0.0, 0.1, 0.2])

fig.tight_layout()
fig.savefig(f"theta_fit_three_panel_nu_{neu}.png", dpi=300, bbox_inches='tight')

f_log.close()
out.close()
