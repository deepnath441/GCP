# Data Collapse Plot Figure 7 (without Labels and Legends)
## Data: 'square_64.txt' contains the data for various values of c and theta averaged over 1000 ensembles

import networkx as nx
import matplotlib.pyplot as plt
import random as rnd
from itertools import combinations
import numpy as np
from scipy.interpolate import make_interp_spline
import math

############# 2D square

x=[]
y=[]

trial_neu=1.3

trial_beta=0.11

trial_1=[]
trial_2=[]
count=0.0
square_sum=0.0

### bandwidth

band=0.8
lower_band=0.1

### -------

###### The threshold values for finite sizes = the value for which fraction of giant component is 0.5

#### ------

##------
#### Square
##------

square_64_1=[]
square_64_2=[]
f_square_64=open('square_64.txt').readlines()
count_square_64=int(len(f_square_64))
square_64_thres=0.540
for i in range(1,count_square_64):
	if float(f_square_64[i].split()[3])!=1.0:
		temp_1=(float(f_square_64[i].split()[2])-float(square_64_thres))
		temp_x=temp_1*(64.0)**(1.0/(2.0*float(trial_neu)))
		temp_2=(64.0)**(float(trial_beta)/(2.0*float(trial_neu)))
		temp_y=float(temp_2)*float(f_square_64[i].split()[3])
		square_64_1.append(temp_x)
		square_64_2.append(temp_y)
	else:
		pass
	
	

square_81_1=[]
square_81_2=[]
f_square_81=open('square_81.txt').readlines()
count_square_81=int(len(f_square_81))
square_81_thres=0.537
for i in range(1,count_square_81):
	if float(f_square_81[i].split()[2])!=1.0:
		temp_1=(float(f_square_81[i].split()[2])-float(square_81_thres))
		temp_x=temp_1*(81.0)**(1.0/(2.0*float(trial_neu)))
		temp_2=(81.0)**(float(trial_beta)/(2.0*float(trial_neu)))
		temp_y=float(temp_2)*float(f_square_81[i].split()[3])
		square_81_1.append(temp_x)
		square_81_2.append(temp_y)
	else:
		pass
                       	        

square_100_1=[]
square_100_2=[]
f_square_100=open('square_100.txt').readlines()
count_square_100=int(len(f_square_100))
square_100_thres=0.535
for i in range(1,count_square_100):
	if float(f_square_100[i].split()[2])!=1.0:
		temp_1=(float(f_square_100[i].split()[2])-float(square_100_thres))
		temp_x=temp_1*(100.0)**(1.0/(2.0*float(trial_neu)))
		temp_2=(100.0)**(float(trial_beta)/(2.0*float(trial_neu)))
		temp_y=float(temp_2)*float(f_square_100[i].split()[3])
		square_100_1.append(temp_x)
		square_100_2.append(temp_y)
	else:
		pass
 

square_225_1=[]
square_225_2=[]
f_square_225=open('square_225.txt').readlines()
count_square_225=int(len(f_square_225))
square_225_thres=0.529
for i in range(1,count_square_225):
	if float(f_square_225[i].split()[2])!=1.0:
		temp_1=(float(f_square_225[i].split()[2])-float(square_225_thres))
		temp_x=temp_1*(225.0)**(1.0/(2.0*float(trial_neu)))
		temp_2=(225.0)**(float(trial_beta)/(2.0*float(trial_neu)))
		temp_y=float(temp_2)*float(f_square_225[i].split()[3])
		square_225_1.append(temp_x)
		square_225_2.append(temp_y)
	else:
		pass

##------
#### Hexagonal
##------

hexa_70_1=[]
hexa_70_2=[]
f_hexa_70=open('hexa_70.txt').readlines()
count_hexa_70=int(len(f_hexa_70))
hexa_70_thres=0.622
for i in range(1,count_hexa_70):
	if float(f_hexa_70[i].split()[2])!=1.0:
		temp_1=(float(f_hexa_70[i].split()[2])-float(hexa_70_thres))
		temp_x=temp_1*(70.0)**(1.0/(2.0*float(trial_neu)))
		temp_2=(70.0)**(float(trial_beta)/(2.0*float(trial_neu)))
		temp_y=float(temp_2)*float(f_hexa_70[i].split()[3])
		hexa_70_1.append(temp_x)
		hexa_70_2.append(temp_y)
	else:
		pass
                                
                                
hexa_96_1=[]
hexa_96_2=[]
f_hexa_96=open('hexa_96.txt').readlines()
count_hexa_96=int(len(f_hexa_96))
hexa_96_thres=0.620
for i in range(1,count_hexa_96):
	if float(f_hexa_96[i].split()[2])!=1.0:
		temp_1=(float(f_hexa_96[i].split()[2])-float(hexa_96_thres))
		temp_x=temp_1*(96.0)**(1.0/(2.0*float(trial_neu)))
		temp_2=(96.0)**(float(trial_beta)/(2.0*float(trial_neu)))
		temp_y=float(temp_2)*float(f_hexa_96[i].split()[3])
		hexa_96_1.append(temp_x)
		hexa_96_2.append(temp_y)
	else:
		pass


hexa_126_1=[]
hexa_126_2=[]
f_hexa_126=open('hexa_126.txt').readlines()
count_hexa_126=int(len(f_hexa_126))
hexa_126_thres=0.616
for i in range(1,count_hexa_126):
	if float(f_hexa_126[i].split()[2])!=1.0:
		temp_1=(float(f_hexa_126[i].split()[2])-float(hexa_126_thres))
		temp_x=temp_1*(126.0)**(1.0/(2.0*float(trial_neu)))
		temp_2=(126.0)**(float(trial_beta)/(2.0*float(trial_neu)))
		temp_y=float(temp_2)*float(f_hexa_126[i].split()[3])
		hexa_126_1.append(temp_x)
		hexa_126_2.append(temp_y)
	else:
		pass
		
		
hexa_240_1=[]
hexa_240_2=[]
f_hexa_240=open('hexa_240.txt').readlines()
count_hexa_240=int(len(f_hexa_240))
hexa_240_thres=0.613
for i in range(1,count_hexa_240):
	if float(f_hexa_240[i].split()[2])!=1.0:
		temp_1=(float(f_hexa_240[i].split()[2])-float(hexa_240_thres))
		temp_x=temp_1*(240.0)**(1.0/(2.0*float(trial_neu)))
		temp_2=(240.0)**(float(trial_beta)/(2.0*float(trial_neu)))
		temp_y=float(temp_2)*float(f_hexa_240[i].split()[3])
		hexa_240_1.append(temp_x)
		hexa_240_2.append(temp_y)
	else:
		pass

##------
#### Triangular
##------
	

tri_64_1=[]
tri_64_2=[]
f_tri_64=open('triangular_64.txt').readlines()
count_tri_64=int(len(f_tri_64))
tri_64_thres=0.504
for i in range(1,count_tri_64):
	if float(f_tri_64[i].split()[3])!=1.0:
		temp_1=(float(f_tri_64[i].split()[2])-float(tri_64_thres))
		temp_x=temp_1*(64.0)**(1.0/(2.0*float(trial_neu)))
		temp_2=(64.0)**(float(trial_beta)/(2.0*float(trial_neu)))
		temp_y=float(temp_2)*float(f_tri_64[i].split()[3])
		tri_64_1.append(temp_x)
		tri_64_2.append(temp_y)
	else:
		pass


tri_81_1=[]
tri_81_2=[]
f_tri_81=open('triangular_81.txt').readlines()
count_tri_81=int(len(f_tri_81))
tri_81_thres=0.5
for i in range(1,count_tri_81):
	if float(f_tri_81[i].split()[3])!=1.0:
		temp_1=(float(f_tri_81[i].split()[2])-float(tri_81_thres))
		temp_x=temp_1*(81.0)**(1.0/(2.0*float(trial_neu)))
		temp_2=(81.0)**(float(trial_beta)/(2.0*float(trial_neu)))
		temp_y=float(temp_2)*float(f_tri_81[i].split()[3])
		tri_81_1.append(temp_x)
		tri_81_2.append(temp_y)
	else:
		pass
	

tri_100_1=[]
tri_100_2=[]
f_tri_100=open('triangular_100.txt').readlines()
count_tri_100=int(len(f_tri_100))

tri_100_thres=0.495
for i in range(1,count_tri_100):
	if float(f_tri_100[i].split()[3])!=1.0:
		temp_1=(float(f_tri_100[i].split()[2])-float(tri_100_thres))
		temp_x=temp_1*(100.0)**(1.0/(2.0*float(trial_neu)))
		temp_2=(100.0)**(float(trial_beta)/(2.0*float(trial_neu)))
		temp_y=float(temp_2)*float(f_tri_100[i].split()[3])
		tri_100_1.append(temp_x)
		tri_100_2.append(temp_y)
	else:
		pass
		
tri_225_1=[]
tri_225_2=[]
f_tri_225=open('triangular_225.txt').readlines()
count_tri_225=int(len(f_tri_225))
tri_225_thres=0.488
for i in range(1,count_tri_225):
	if float(f_tri_225[i].split()[3])!=1.0:
		temp_1=(float(f_tri_225[i].split()[2])-float(tri_225_thres))
		temp_x=temp_1*(225.0)**(1.0/(2.0*float(trial_neu)))
		temp_2=(225.0)**(float(trial_beta)/(2.0*float(trial_neu)))
		temp_y=float(temp_2)*float(f_tri_225[i].split()[3])
		tri_225_1.append(temp_x)
		tri_225_2.append(temp_y)
	else:
		pass
	


#fit=np.polyfit(x,y,1.7)
#gradient=fit[0]
#intercept=fit[1]
#print(gradient,intercept)

#fit_eq=[]



##average_theta_threshold_value=0.370819

#theta=0.2

#zeta=[]
#diff_c=[]
#c=0.01

#c_thres=0.6
#pc_square=0.33754
#for i in range(99):
#        if c<c_thres:
#                diff_c.append(abs(c-c_thres))
#                #zeta.append(((abs(c-c_thres)/c_thres))**(-trial_neu))
                #fit_eq.append(((gradient*c)+intercept))
#                zeta.append(((abs(c-c_thres)))**(-trial_neu))
#                c+=0.01

#print(c)
        
#print(k,d)




#plt.yscale("log")
#plt.xscale("log")

fig, ax=plt.subplots()

#plt.yticks(np.arange(10, 1000))


#plt.yscale("log")
#plt.xscale("log")

plt.xticks(fontsize=35)
plt.yticks(fontsize=35)
#ax.set_ylabel('$P(c,N)$', fontsize=16)
#ax.set_xlabel('$(c-c_{th})N**(1/d\neu)$', fontsize=16, loc='center')
#plt.ylim(0.3,10**4)
#plt.xlim([10**(-2),10**(-1)])
plt.xlim([-1,1])

plt.xticks(np.arange(-1, 1.1, 1)) #square 1
plt.yticks(np.arange(0, 1.3, 1.2)) #square 1

#plt.xlegend('c')


#first_legend = ax.legend(handles=[line1,line2,line3,line4], loc='upper left', title='Hexagonal', fontsize=10)
#first_legend = ax.legend(handles=[line1,line2,line4], loc='upper left', title='Hexagonal', fontsize=15)
#ax.add_artist(first_legend)
#plt.legend(loc='upper left', title='Hexagonal')

#s1,=plt.plot(square_25_1, square_25_2, 's', color='blue', label='n=25')
###s2,=plt.plot(square_36_1, square_36_2, 's', color='blue', label='n=36', markersize=6)
###s3,=plt.plot(square_49_1, square_49_2, 'd', color='blue', label='n=49', markersize=6)
s4,=plt.plot(square_64_1, square_64_2, 'o', color='blue', label='n=64', markersize=6)
s5,=plt.plot(square_81_1, square_81_2, 'v', color='blue', label='n=81', markersize=6)
s6,=plt.plot(square_100_1, square_100_2, '^', color='blue', label='n=100', markersize=6)
s7,=plt.plot(square_225_1, square_225_2, 'x', color='blue', label='n=225', markersize=6)

#second_legend = ax.legend(handles=[s1,s2,s3,s4,s5,s6], loc='upper center', title='Square', fontsize=15)
#second_legend = ax.legend(handles=[s2,s3,s4,s5,s6], loc='upper center', title='Square', fontsize=10)
#ax.add_artist(second_legend)

#second_legend = ax.legend(handles=[line5,line6,line7,line8,line9,line10], loc='upper center', title='Square')
#ax.add_artist(second_legend)

#line11,=plt.plot(tri_25_1, tri_25_2, '^', color='magenta', label='n=25')
###line12,=plt.plot(tri_36_1, tri_36_2, 's', color='magenta', label='n=36', markersize=6)
###line13,=plt.plot(tri_49_1, tri_49_2, 'd', color='magenta', label='n=49', markersize=6)
line14,=plt.plot(tri_64_1, tri_64_2, 'o', color='magenta', label='n=64', markersize=6)
line15,=plt.plot(tri_81_1, tri_81_2, 'v', color='magenta', label='n=81', markersize=6)
line16,=plt.plot(tri_100_1, tri_100_2, '^', color='magenta', label='n=100', markersize=6)
line17,=plt.plot(tri_225_1, tri_225_2, 'x', color='magenta', label='n=225', markersize=6)

###line1,=plt.plot(hexa_48_1, hexa_48_2, 's', color='red', label='n=48', markersize=6)
line2,=plt.plot(hexa_70_1, hexa_70_2, 'd', color='red', label='n=70', markersize=6)
line3,=plt.plot(hexa_96_1, hexa_96_2, 'o', color='red', label='n=96', markersize=6)
line4,=plt.plot(hexa_126_1, hexa_126_2, 'v', color='red', label='n=126', markersize=6)
line5,=plt.plot(hexa_240_1, hexa_240_2, '^', color='red', label='n=126', markersize=6)

#third_legend = ax.legend(handles=[line11,line12,line13,line14,line15,line16], loc='upper right', title='Triangular', fontsize=15)
#third_legend = ax.legend(handles=[line12,line13,line14,line15,line16], loc='upper right', title='Triangular', fontsize=10)
#ax.add_artist(third_legend)

#plt.plot(diff_c, fit_eq, color='green')
#plt.plot(diff_c, zeta, color='black')
#line17,=plt.plot(trial_1, trial_2, color='black', label='\u03BD=0.51(5)', linewidth=3.0)

#fourth_legend = ax.legend(handles=[line17], loc='lower left', fontsize=15)
#ax.add_artist(fourth_legend)

plt.show()
        

