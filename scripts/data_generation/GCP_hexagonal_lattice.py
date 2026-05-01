## GCP without Newman-Ziff algorithm

import networkx as nx
#import matplotlib.pyplot as plt
import math
import random as rnd
from itertools import combinations
import numpy as np
#from math import comb

count_ensemble=0.0
#f1=open('qn_percolation_result.txt', 'w')
#f1.close()
f2=open('qn_percolation_result_data.txt', 'w')
f2.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%('##theta', 'c', 'total_number_of_components', 'fraction_of_giant_component', 'diameter_of_G_quantum', 'N_Q_G', 'N_C_G', 'E_C', 'E_Q', 'E_Q_final'))
f2.close()


for ensemble in range(1000):
    count_ensemble+=1.0
    f2=open('qn_percolation_result_data.txt', 'a')
    f2.write('%s\t%s\t%d\n'%('#####', 'ensemble', count_ensemble))
    f2.close()
    theta=0.01
    #p=0.01
    N=7
    for probability in range(100):
        theta_in_pi=theta*(math.pi/4.0)
        c=math.sin(2.0*theta_in_pi)
        #print(c)
        G_classical=nx.Graph()
        G_classical=nx.hexagonal_lattice_graph(N,N)
        G_quantum_2=nx.Graph()
        node_list_quantum=[]
        for i in G_classical.nodes:
            #G_quantum_2.add_node(i) # initially only nodes are added in quantum graph
            G_quantum_2.add_node(i)
            node_list_quantum.append(i)
        #print(G_classical.edges)
        #print(G_quantum.nodes)
        node_pair_dict_quantum=combinations(node_list_quantum,2)
        node_pair_list_quantum=list(node_pair_dict_quantum)
        # we will consider each pair and will try to evaluate the probability of having edge between them
        for node_pair in node_pair_list_quantum:
            #print(node_pair)
            if nx.has_path(G_classical,node_pair[0],node_pair[1])==True: # if there is a classical path - there will be a quantum edge
                all_shortest_path=nx.all_shortest_paths(G_classical,node_pair[0],node_pair[1]) # all possible shortest paths between that pair
                all_shortest_path_list=list(all_shortest_path)
                #numerator=abs(node_pair[0][0]-node_pair[1][0])+abs(node_pair[0][1]-node_pair[1][1])
                #denomenator=abs(node_pair[0][0]-node_pair[1][0])
                #print(all_shortest_path_list)
                #number_of_shortest_path=comb(int(numerator),int(denomenator))
                shortest_path_length=len(all_shortest_path_list[0])-1 # for all shortest paths - path length will be same - shortest
                c_for_parallel_paths=[]
                for j in all_shortest_path_list: # calcualte probability by series rule for each shortest path
                    concurrence_of_quantum_edge_series=1.0
                    for loop in range(int(shortest_path_length)):
                        temp_1=float(concurrence_of_quantum_edge_series)*float(c)
                        concurrence_of_quantum_edge_series=float(temp_1)
                    c_for_parallel_paths.append(concurrence_of_quantum_edge_series)
                #print(c_for_parallel_paths)
                temp_2=1.0
                for k in c_for_parallel_paths: # apply parallel rule for all shortest paths
                    #print(float(k))
                    temp_3=temp_2*((1.0+math.sqrt(1.0-(float(k)**2.0)))/2.0)
                    temp_2=float(temp_3)
                #print('theta, c, shortest_path_length', theta_in_pi, c, shortest_path_length)
                #print('temp_2', temp_2)
                if temp_2>0.5:
                    concurrence_of_quantum_edge_1=float(temp_2)
                else:
                    concurrence_of_quantum_edge_1=float(0.5)
                concurrence_of_quantum_edge=2.0*math.sqrt(concurrence_of_quantum_edge_1*(1.0-concurrence_of_quantum_edge_1))
                #print('concurrence_of_quantum_edge', concurrence_of_quantum_edge_1, concurrence_of_quantum_edge)
                theta_of_quantum_edge=math.asin(float(concurrence_of_quantum_edge))/2.0
                probability_of_quantum_edge=2.0*(math.sin(float(theta_of_quantum_edge))**2.0)
                r1=rnd.random()
                #print(r1)
                if r1<=probability_of_quantum_edge:
                    G_quantum_2.add_edge(node_pair[0],node_pair[1])
                else:
                    pass
                #print('_____________________')
            else:
                pass
        #print(G_quantum.edges)
        total_number_of_nodes_quantum=G_quantum_2.number_of_nodes()
        total_number_of_nodes_classical=G_classical.number_of_nodes()
        #print(total_number_of_nodes)
        G_quantum_all_components=sorted(nx.connected_components(G_quantum_2), key=len, reverse=True)
        G_quantum_giant_component=G_quantum_2.subgraph(G_quantum_all_components[0])
        #print(G_quantum_giant_component.edges)
        number_of_nodes_giant_component=G_quantum_giant_component.number_of_nodes()
        #print(number_of_nodes_giant_component)
        fraction_of_giant_component=float(number_of_nodes_giant_component)/float(total_number_of_nodes_quantum)

        total_number_of_components=len(G_quantum_all_components)
        total_number_of_edges_classical=G_classical.number_of_edges()
        total_number_of_edges_quantum=G_quantum_2.number_of_edges()
        total_number_of_edges_quantum_final=G_quantum_2.number_of_edges()
        diameter_of_G_quantum=nx.diameter(G_quantum_giant_component)
        f2=open('qn_percolation_result_data.txt', 'a')
        f2.write('%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n'%(theta, c, total_number_of_components, fraction_of_giant_component, diameter_of_G_quantum, total_number_of_nodes_quantum, total_number_of_nodes_classical, total_number_of_edges_classical, total_number_of_edges_quantum, total_number_of_edges_quantum_final))
        f2.close()
        theta+=0.01
