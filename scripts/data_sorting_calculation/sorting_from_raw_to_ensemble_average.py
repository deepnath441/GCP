## Raw data before ensemble average: 'square_100.txt'
## From raw data to ensemble average

import networkx as nx
import matplotlib.pyplot as plt
import random as rnd
from itertools import combinations
import numpy as np
from scipy.interpolate import make_interp_spline

f1=open('square_100.txt').readlines()
count1=int(len(f1))

f2=open('square_100_sorted.txt', 'w')
f2.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%('##theta', 'component', 'c', 'f_gc', 'n_gc', 'n_gc**2', 'n_gc**4', 'di_gc', 'ratio'))
#f2.write('%d\t%f\n'%(0, 1.0))
f2.close()

theta_para=0.01
while theta_para<=1.0:
        theta=[]
        p=[]
        f_gc=[]
        n_gc=[]
        n_gc_2=[]
        n_gc_4=[]
        di_gc=[]
        nodes=[]
        edges=[]
        total_comp=[]
        #theta_para_count=0.0

        #print('initial_theta_para', theta_para)
        for i in range(count1):
                #print(f1[i].split()[0],theta_para)
                if str(f1[i].split()[0])==str('#####') or str(f1[i].split()[0])==str('##theta'):
                        pass
                else:
                        if float(f1[i].split()[0])==float('%7.5f'%(theta_para)):
                                #theta_para_count+=1.0
                                theta.append(float(f1[i].split()[0]))
                                p.append(float(f1[i].split()[1]))
                                total_comp.append(float(f1[i].split()[2]))
                                temp_1=float(f1[i].split()[3])*number_nodes
                                f_gc.append(float(f1[i].split()[3]))
                                n_gc.append(float(temp_1))
                                n_gc_2.append(float(temp_1)**2.0)
                                n_gc_4.append(float(temp_1)**4.0)
                                di_gc.append(float(f1[i].split()[4]))
                                nodes.append(float(f1[i].split()[6]))
                                edges.append(float(f1[i].split()[9]))
                        else:
                                pass
        #print(len(theta_para_count))
        if len(theta)!=0:
                av_theta=sum(theta)/float(len(theta))
                av_p=sum(p)/float(len(p))
                av_comp=sum(total_comp)/float(len(total_comp))
                av_f_gc=sum(f_gc)/float(len(f_gc))
                av_n_gc=sum(n_gc)/float(len(n_gc))
                av_n_gc_2=sum(n_gc_2)/float(len(n_gc_2))
                av_n_gc_4=sum(n_gc_4)/float(len(n_gc_4))
                av_di_gc=sum(di_gc)/float(len(di_gc))
                av_nodes=sum(nodes)/float(len(nodes))
                av_edges=sum(edges)/float(len(edges))
                ratio=float(av_edges)/float(av_nodes)
                f2=open('square_100_sorted.txt', 'a')
                f2.write('%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n'%(av_theta, av_comp, av_p, av_f_gc, av_n_gc, av_n_gc_2, av_n_gc_4, av_di_gc, ratio))
                f2.close()
        else:
                pass
        #print(theta_para)
        theta_para+=0.01
        
