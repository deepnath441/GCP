import networkx as nx
import matplotlib.pyplot as plt
import random as rnd
from itertools import combinations
import numpy as np
from scipy.interpolate import make_interp_spline

f1=open('square_225.txt').readlines()
count1=int(len(f1))

#number_nodes=81.0

f2=open('square_225_sorted.txt', 'w')
f2.write('%s\t%s\t%s\t%s\n'%('##theta', 'component', 'c', 'f_gc'))
#f2.write('%d\t%f\n'%(0, 1.0))
f2.close()

time=0.01
while time<=0.7:
        theta=[]
        p=[]
        f_gc=[]
        total_comp=[]
        #time_count=0.0

        #print('initial_time', time)
        for i in range(count1):
                #print(f1[i].split()[0],time)
                if str(f1[i].split()[0])==str('#####') or str(f1[i].split()[0])==str('##theta'):
                        pass
                else:
                        if float(f1[i].split()[0])==float('%7.5f'%(time)):
                                #time_count+=1.0
                                theta.append(float(f1[i].split()[0]))
                                p.append(float(f1[i].split()[1]))
                                total_comp.append(float(f1[i].split()[2]))
                                #temp_1=float(f1[i].split()[3])*number_nodes
                                f_gc.append(float(f1[i].split()[4]))
                                
                        else:
                                pass
        #print(len(time_count))
        if len(theta)!=0:
                av_theta=sum(theta)/float(len(theta))
                av_p=sum(p)/float(len(p))
                av_comp=sum(total_comp)/float(len(total_comp))
                av_f_gc=sum(f_gc)/float(len(f_gc))
                
                f2=open('square_225_sorted.txt', 'a')
                f2.write('%f\t%f\t%f\t%f\n'%(av_theta, av_comp, av_p, av_f_gc))
                f2.close()
        else:
                pass
        #print(time)
        time+=0.01
        
