## Scans the current folder for files containing the values of \theta_{th}
## provide a new file containing N vs \theta_{th}

import glob
import re

# -------- FIND FILES ----------
files = glob.glob("percolation_threshold_hexa_*.txt") #### for hexagonal lattices
#files = glob.glob("percolation_threshold_square_*.txt") #### for square lattices
#files = glob.glob("percolation_threshold_tri_*.txt") #### for triangular lattices

data = []   # to store (N, theta, c)

# -------- PROCESS FILES ----------
for fname in files:

    # Extract N from filename
    match = re.search(r'hexa_(\d+)', fname)
    #match = re.search(r'square_(\d+)', fname)
    #match = re.search(r'tri_(\d+)', fname)
    if not match:
        continue
    N = int(match.group(1))

    with open(fname, "r") as f:
        lines = f.readlines()

    # Find header
    header = None
    for line in lines:
        if "theta_round_off" in line and "c_round_off" in line:
            header = line.split()
            break

    if header is None:
        continue

    # Get column indices
    try:
        theta_idx = header.index("theta_round_off")
        c_idx = header.index("c_round_off")
    except ValueError:
        continue

    # Read data
    for line in lines:
        if line.startswith("#") or line.strip() == "":
            continue

        parts = line.split()
        if len(parts) <= max(theta_idx, c_idx):
            continue

        theta_val = float(parts[theta_idx])
        c_val = float(parts[c_idx])

        data.append((N, theta_val, c_val))

# -------- SORT BY N ----------
data.sort(key=lambda x: x[0])

# -------- WRITE OUTPUT ----------
#this file contains theta, c values (rounded off) for which the fraction of giant component = 0.5
with open("theta_05_hexa.txt", "w") as out: #### for hexagonal lattices
#with open("theta_05_square.txt", "w") as out: #### for square lattices
#with open("theta_05_tri.txt", "w") as out: #### for triangular lattices
    out.write("#N\ttheta_round_off\tc_round_off\n")
    
    for N, theta_val, c_val in data:
        out.write(f"{N}\t{theta_val:.3f}\t{c_val:.3f}\n")

print("File 'theta_05_hexa.txt' created (sorted by N).") #### for hexagonal lattices
#print("File 'theta_05_square.txt' created (sorted by N).") #### for square lattices
#print("File 'theta_05_tri.txt' created (sorted by N).") #### for triangular lattices
