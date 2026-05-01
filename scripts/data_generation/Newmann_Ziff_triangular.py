import networkx as nx
import math
import random as rnd

# Binomial coefficient
def binomial_coefficient(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

# Union-Find with path compression and union by size
class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.size = {node: 1 for node in nodes}
        self.max_size = 1
        self.num_components = len(nodes)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        self.max_size = max(self.max_size, self.size[root_x])
        self.num_components -= 1

# Output file
with open('qn_percolation_result_data.txt', 'w') as f:
    f.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %
            ('##theta', 'c', 'total_components', 'max_cluster_size', 'fraction',
             'N_Q', 'E_Q', 'E_C', 'N_C'))

count_ensemble = 0.0

for ensemble in range(500):  # Adjust ensemble count as needed
    count_ensemble += 1.0
    with open('qn_percolation_result_data.txt', 'a') as f:
        f.write('%s\t%s\t%d\n' % ('#####', 'ensemble', count_ensemble))

    theta = 0.01
    N_classical = 15
    G_classical = nx.grid_graph(dim=[N_classical, N_classical])
    N = G_classical.number_of_nodes()

    for theta_count in range(60):  # Adjust range as needed
        theta_in_pi = theta * (math.pi / 4.0)
        c = math.sin(2.0 * theta_in_pi)

        node_list = list(G_classical.nodes())
        G_quantum = nx.Graph()
        G_quantum.add_nodes_from(node_list)
        uf = UnionFind(node_list)

        for i in range(len(node_list)):
            for j in range(i + 1, len(node_list)):
                u, v = node_list[i], node_list[j]
                if nx.has_path(G_classical, u, v):
                    x1, y1 = u
                    x2, y2 = v
                    dx, dy = abs(x1 - x2), abs(y1 - y2)

                    if x1 < x2:
                        if y1 >= y2:
                            numerator, denominator = dx + dy, dx
                        else:
                            numerator_1 = min(dx, dy)
                            numerator_2 = abs(dx - dy)
                            numerator = numerator_1 + numerator_2
                            denominator = numerator_1
                    else:
                        if y2 >= y1:
                            numerator, denominator = dx + dy, dx
                        else:
                            numerator_1 = min(dx, dy)
                            numerator_2 = abs(dx - dy)
                            numerator = numerator_1 + numerator_2
                            denominator = numerator_1

                    number_of_shortest_path = binomial_coefficient(numerator, denominator)
                    shortest_path_length = numerator

                    c_parallel = [c ** shortest_path_length] * int(number_of_shortest_path)

                    temp = 1.0
                    for k in c_parallel:
                        temp *= (1.0 + math.sqrt(1.0 - k ** 2)) / 2.0

                    concurrence_1 = max(temp, 0.5)
                    concurrence = 2.0 * math.sqrt(concurrence_1 * (1.0 - concurrence_1))
                    theta_edge = math.asin(concurrence) / 2.0
                    probability = 2.0 * (math.sin(theta_edge) ** 2.0)

                    if rnd.random() <= probability:
                        G_quantum.add_edge(u, v)
                        uf.union(u, v)

        with open('qn_percolation_result_data.txt', 'a') as f:
            f.write('%f\t%f\t%d\t%d\t%f\t%d\t%d\t%d\t%d\n' % (
                theta, c, uf.num_components, uf.max_size, uf.max_size / float(N),
                G_quantum.number_of_nodes(), G_quantum.number_of_edges(),
                G_classical.number_of_edges(), G_classical.number_of_nodes()))

        theta += 0.01

