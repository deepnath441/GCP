## 'triangular_100.txt' --> N=100; Raw data (contains values associated with all ensembles, i.e., before average)
## This script considers raw data and calculate the value of \theta_{th} for which fraction of the giant component = 0.5
## For square and triangular lattices

import networkx as nx
import matplotlib.pyplot as plt
import random as rnd
from itertools import combinations
import numpy as np
from scipy.interpolate import make_interp_spline

#f1=open('square_100.txt').readlines()
f1=open('triangular_100.txt').readlines()
count1=int(len(f1))

#f2=open('percolation_threshold_square_100.txt', 'w')
f2=open('percolation_threshold_tri_100.txt', 'w')
f2.write('%s\t%s\t%s\t%s\t%s\n'%('####fraction_of_giant_component', 'percolation_threshold_c', 'percolation_threshold_theta', 'c_round_off', 'theta_round_off'))
#f2.write('%d\t%f\n'%(0, 1.0))
f2.close()


f_GC=[]
p=[]
theta=[]
for i in range(count1):
        if str(f1[i].split()[0])=='##theta':
                pass
        elif str(f1[i].split()[0])=='#####':
                pass
        else:
                #fraction_of_giant_component_formatted=float("%.1f"%float(f1[i].split()[4])) # for N=225 as the file structure is different
                fraction_of_giant_component_formatted=float("%.1f"%float(f1[i].split()[3])) # for other N
                print(fraction_of_giant_component_formatted)
                if fraction_of_giant_component_formatted==0.5: 
                        f_GC.append(fraction_of_giant_component_formatted)
                        p.append(float(f1[i].split()[1]))
                        theta.append(float(f1[i].split()[0]))
                else:
                        pass

print(sum(f_GC),
float(len(f_GC)))
av_f_GC=sum(f_GC)/float(len(f_GC))
av_p=sum(p)/float(len(p))
av_theta=sum(theta)/float(len(theta))
#f2=open('percolation_threshold_square_100.txt', 'a')
f2=open('percolation_threshold_tri_100.txt', 'a')
f2.write('%f\t%f\t%f\t%.3f\t%.3f\n'%(av_f_GC, av_p, av_theta, av_p, av_theta))
f2.close()

