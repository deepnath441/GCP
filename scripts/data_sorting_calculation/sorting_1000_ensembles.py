## Raw data before ensemble average: 'square_100.txt'
## From raw data to ensemble average (desired number of ensembles)

import networkx as nx
import matplotlib.pyplot as plt
import random as rnd
from itertools import combinations
import numpy as np
from scipy.interpolate import make_interp_spline

f1=open('triangular_100.txt').readlines()
count1=int(len(f1))


f2=open('triangular_100_sorted.txt', 'w')
f2.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%('##theta', 'component', 'c', 'f_gc', 'n_gc', 'n_gc**2', 'n_gc**4', 'di_gc', 'ratio'))
#f2.write('%d\t%f\n'%(0, 1.0))
f2.close()

number_nodes = 100

theta_para = 0.01
while theta_para <= 1.0:

    theta = []
    p = []
    f_gc = []
    n_gc = []
    n_gc_2 = []
    n_gc_4 = []
    di_gc = []
    nodes = []
    edges = []
    total_comp = []

    count = 0   # NEW: ensemble counter

    for i in range(count1):

        cols = f1[i].split()

        if cols[0] == '#####' or cols[0] == '##theta':
            continue

        # float-safe comparison (IMPORTANT)
        if abs(float(cols[0]) - theta_para) < 1e-6:

            theta.append(float(cols[0]))
            p.append(float(cols[1]))
            total_comp.append(float(cols[2]))

            temp_1 = float(cols[3]) * number_nodes
            f_gc.append(float(cols[3]))
            n_gc.append(temp_1)
            n_gc_2.append(temp_1**2)
            n_gc_4.append(temp_1**4)

            di_gc.append(float(cols[4]))
            nodes.append(float(cols[6]))
            edges.append(float(cols[9]))

            count += 1

            # ✅ STOP after 100 ensembles
            if count == 1000:
                break

    # ✅ Only write if EXACTLY 100 ensembles found
    if count == 1000:

        av_theta = sum(theta)/count
        av_p = sum(p)/count
        av_comp = sum(total_comp)/count
        av_f_gc = sum(f_gc)/count
        av_n_gc = sum(n_gc)/count
        av_n_gc_2 = sum(n_gc_2)/count
        av_n_gc_4 = sum(n_gc_4)/count
        av_di_gc = sum(di_gc)/count
        av_nodes = sum(nodes)/count
        av_edges = sum(edges)/count

        ratio = av_edges / av_nodes

        with open('triangular_100_sorted.txt', 'a') as f2:
            f2.write('%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n' % (
                av_theta, av_comp, av_p, av_f_gc,
                av_n_gc, av_n_gc_2, av_n_gc_4,
                av_di_gc, ratio
            ))

    theta_para += 0.01
