import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import math

# -------- CONFIG ----------
nu_values = [0.9, 1.3, 1.7]
RMSD_limit = 0.001

# -------- OPEN LOG FILE ----------
f_log = open('square_print_output_new.txt', 'w')
print("nu\tSlope\tIntercept(theta_T)\tError\tRMSD", file=f_log)

# -------- READ DATA ----------
lines = open('theta_05_square.txt').readlines()

# -------- LOOP OVER NU VALUES ----------
for neu in nu_values:

    y = []
    x = []

    for line in lines[1:]:
        if not line.strip():
            continue

        parts = line.split()
        y.append(float(parts[1]))

        temp = (float(parts[0])) ** ((-1.0) / (2.0 * neu))
        x.append(temp)

    x = np.array(x)
    y = np.array(y)

    # -------- INITIAL FIT ----------
    fit = np.polyfit(x, y, 1)
    gradient = fit[0]

    # -------- SLOPE SCAN ----------
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

    # -------- ERROR ----------
    slopes = np.array([r[0] for r in results])
    intercepts = np.array([r[1] for r in results])
    rmsds = np.array([r[2] for r in results])

    rmin = np.min(rmsds)
    mask = rmsds <= (rmin + RMSD_limit)

    acceptable_intercepts = intercepts[mask]

    theta_error = (np.max(acceptable_intercepts) - np.min(acceptable_intercepts)) / 2.0

    # -------- PRINT RESULTS ----------
    print(f"{neu}\t{best_a:.6f}\t{best_b:.6f}\t{theta_error:.6f}\t{best_rmsd:.6f}", file=f_log)

    # ==========================================================
    #  ONLY PLOT FOR nu = 1.3
    # ==========================================================
    if abs(neu - 1.3) < 1e-6:

        sort_idx = np.argsort(x)
        x_sorted = x[sort_idx]
        y_sorted = y[sort_idx]
        fit_eq_sorted = best_a * x_sorted + best_b

        # -------- MAIN PLOT ----------
        plt.figure(figsize=(8, 6))

        x_extrap = np.array([0, x_sorted[0]])
        y_extrap = np.array([best_b, fit_eq_sorted[0]])

        plt.plot(x_extrap, y_extrap, 'r:', linewidth=3, label=r'Extrapolation')
        plt.plot(0, best_b, 'go', markersize=10, label=r'$\theta_T$')

        plt.plot(x_sorted, y_sorted, 'bo', markersize=8)
        plt.plot(x_sorted, fit_eq_sorted, 'r-', linewidth=2, label='Fit')

        error_int = int(round(theta_error * 1000))
        plt.annotate(rf"$\theta_T = {best_b:.3f}({error_int})$",
                     xy=(0, best_b),
                     xytext=(max(x_sorted)*0.1, best_b),
                     arrowprops=dict(arrowstyle="->"))

        plt.xlabel(r"$N^{-1/(2\nu)}$", fontsize=16)
        plt.ylabel(r"$\theta_{th}$", fontsize=16)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)

        plt.tight_layout()
        plt.savefig("theta_fit_square_new.png", dpi=300)

        # -------- RMSD PLOT ----------
        plt.figure()
        plt.plot(slopes, rmsds, 'k-')
        plt.xlabel("Slope")
        plt.ylabel("RMSD")
        plt.savefig("rmsd_vs_slope_new.png", dpi=300)

# -------- CLOSE LOG ----------
f_log.close()
