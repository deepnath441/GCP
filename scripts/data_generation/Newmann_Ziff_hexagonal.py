import networkx as nx
import math
import random as rnd
import concurrent.futures


class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}
        self.size = {node: 1 for node in nodes}
        self.max_size = 1
        self.num_components = len(nodes)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return

        # Union by rank
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.max_size = max(self.max_size, self.size[root_x])
        else:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
            self.max_size = max(self.max_size, self.size[root_y])
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1

        self.num_components -= 1


def compute_concurrence(c, l, num_paths):
    c_series = c ** l
    sqrt_term = math.sqrt(max(1.0 - c_series ** 2, 0.0))
    temp_2 = ((1.0 + sqrt_term) / 2.0) ** num_paths
    concurrence = max(temp_2, 0.5)
    concurrence_final = 2.0 * math.sqrt(concurrence * (1.0 - concurrence))
    theta_edge = math.asin(concurrence_final) / 2.0
    return 2.0 * (math.sin(theta_edge) ** 2)


def run_single_ensemble(ensemble_id, N=10):
    G_classical = nx.hexagonal_lattice_graph(N, N)
    nodes = list(G_classical.nodes)
    path_lengths = dict(nx.all_pairs_shortest_path_length(G_classical))

    buffer = []
    buffer.append(f"#####\tensemble\t{ensemble_id + 1}")
    theta = 0.01

    for _ in range(70):
        theta_in_pi = theta * (math.pi / 4.0)
        c = math.sin(2.0 * theta_in_pi)

        uf = UnionFind(nodes)
        G_quantum = nx.Graph()
        G_quantum.add_nodes_from(nodes)

        for i in range(len(nodes)):
            u = nodes[i]
            for j in range(i + 1, len(nodes)):
                v = nodes[j]
                if v not in path_lengths[u]:
                    continue

                l = path_lengths[u][v]
                try:
                    num_paths = sum(1 for _ in nx.all_shortest_paths(G_classical, u, v))
                except nx.NetworkXNoPath:
                    continue

                prob_edge = compute_concurrence(c, l, num_paths)

                if rnd.random() <= prob_edge:
                    G_quantum.add_edge(u, v)
                    uf.union(u, v)

        total_nodes = len(nodes)
        fraction_giant = uf.max_size / total_nodes

        buffer.append('%f\t%f\t%d\t%f\t%d\t%d\t%d\t%d' % (
            theta, c, uf.num_components, fraction_giant,
            G_quantum.number_of_nodes(), G_quantum.number_of_edges(),
            G_classical.number_of_edges(), G_classical.number_of_nodes()))

        theta += 0.01

    return '\n'.join(buffer)


def run_ensemble_parallel(num_ensembles=500, output_file='qn_percolation_result_data.txt'):
    header = (
        '##theta\tc\ttotal_number_of_components\tfraction_of_giant_component\t'
        'N_Q\tE_Q\tE_C\tN_C'
    )
    with open(output_file, 'w') as f:
        f.write(header + '\n')

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(run_single_ensemble, range(num_ensembles)))

    with open(output_file, 'a') as f:
        f.write('\n'.join(results) + '\n')


if __name__ == '__main__':
    run_ensemble_parallel()

