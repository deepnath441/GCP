# General Concurrence Percolation on Quantum Networks

This repository contains Python implementations of General Concurrence Percolation (GCP) for entanglement percolation on two-dimensional quantum networks, based on:

Nath, D., & Roy, S. (2025).  
General Concurrence Percolation on Quantum Networks.  
[arXiv:2501.11004](https://arxiv.org/abs/2501.11004)

---

## 📄 Published Description

Quantum networks consist of nodes connected by entangled states, which enable long-distance quantum communication. However, in realistic scenarios, these states are typically non-maximally entangled due to decoherence and noise, making reliable communication challenging.

This work introduces **General Concurrence Percolation (GCP)**, a protocol that helps in establishing maximal entanglement across a network using local operations and classical communication (LOCC). Unlike existing approaches, GCP:

- Exploits **only shortest paths** between nodes  
- Preserves the **the intermediate nodes**  
- Generates **effective long-range entanglement links**  
- Produces a **dense effective network of entangled states**  

Through extensive Monte Carlo simulations and finite-size scaling analysis on square, triangular, and hexagonal lattices, it is shown that GCP:

- Achieves **lower percolation thresholds** than CEP, QEP, and ConPT  
- Belongs to the **standard percolation universality class**  
- Enables more efficient long-distance quantum communication  

---

## 📂 Contents of This Repository

### Quantum Network Construction, GCP, Shortest Path Analysis, Monte Carlo Simulations
Implemented in 'scripts/data_generation/.'

### Finite-Size Scaling Analysis, Data Collapse, Plotting and Visualization
Implemented in 'scripts/plot/.'

### Sorting the data, Finite-size percolation threshold calculation
Implemented in 'scripts/data_sorting_calculation/.'

## 🧠 Key Concepts

- Quantum Networks  
- Entanglement Percolation  
- Concurrence  
- LOCC (Local Operations and Classical Communication)  
- Entanglement Swapping and Distillation  
- Percolation Threshold
- Data Collapse 
- Finite-Size Scaling  
- Critical Exponents  
- Universality Class  

---

## 🚀 Reproducibility

All results presented in the paper can be reproduced using the scripts provided in this repository.

### Workflow:
1. Generate lattice-based quantum networks  
2. Compute shortest paths and concurrence values  
3. Perform entanglement swapping and distillation  
4. Run Monte Carlo simulations  
5. Analyze percolation behavior  
6. Generate plots and scaling results  

---

## 📊 Main Result

GCP achieves significantly lower percolation thresholds compared to existing protocols.
GCP belongs to the universality class of ordinary percolation theory.

---

## 📎 Notes

- All simulations are performed over large ensembles for statistical accuracy  
- Data collapse has been performed to calculate the associated critical exponents
- Finite-size scaling is used to estimate the value of the percolation threshold in the thermodynamic limit
