import networkx as nx
import matplotlib.pyplot as plt
from CommutativeSemiring import CommutativeSemiring 
from MISQuery import MISQuery
from SelectiveSemiringExtension import SelectiveSemiringExtension

def failing_graph():
    G = nx.Graph()
    G.add_nodes_from([0,1,2,3,4,5,6,7,8,9])
    G.add_edges_from([(1,2), (2,3), (1,3), (3,8), (3,6), (8,5), (4,5), (7,8), (0,7), (0,9)])
    return G

def generate_edge_case_graphs():
    graphs = {}

    # 1. Empty Graph
    graphs['empty'] = nx.Graph()

    # 2. Single Node
    graphs['single_node'] = nx.Graph()
    graphs['single_node'].add_node(1)

    # 3. Single Edge
    graphs['single_edge'] = nx.Graph()
    graphs['single_edge'].add_edge(1, 2)

    # 4. Disconnected Graph
    graphs['disconnected'] = nx.Graph()
    graphs['disconnected'].add_edges_from([(1, 2), (3, 4)])  # Two separate components

    # 5. Complete Graph
    graphs['complete'] = nx.complete_graph(5)  # All nodes are interconnected

    # 6. Star Graph
    graphs['star'] = nx.star_graph(4)  # One central node connected to all others

    # 7. Line Graph (Path Graph)
    graphs['line'] = nx.path_graph(5)  # Nodes connected in a single line

    # 8. Cycle Graph
    graphs['cycle'] = nx.cycle_graph(5)  # Nodes connected in a loop

    # 9. Binary Tree
    graphs['binary_tree'] = nx.balanced_tree(2, 3)  # Binary tree with 3 levels

    # 10. Bipartite Graph
    graphs['bipartite'] = nx.complete_bipartite_graph(3, 3)  # Two sets of nodes, all nodes in one set connect to all nodes in the other set

    # 11. Wheel Graph
    graphs['wheel'] = nx.wheel_graph(5)  # A single central hub node connected to all nodes forming a cycle

    # 12. Grid Graph
    graphs['grid'] = nx.grid_2d_graph(3, 3)  # Nodes arranged in a 3x3 grid pattern

    # 13. Tree Graph (Non-Binary)
    graphs['tree'] = nx.balanced_tree(3, 2)  # Ternary tree with 2 levels

    # 14. Ladder Graph
    graphs['ladder'] = nx.ladder_graph(5)  # Two parallel lines with rungs between them

    # 15. Circular Ladder Graph
    graphs['circular_ladder'] = nx.circular_ladder_graph(5)  # Ladder graph with ends connected to form a circle

    # 16. Barbell Graph
    graphs['barbell'] = nx.barbell_graph(5, 1)  # Two complete graphs connected by a path

    # 17. Random Graph (Erdős-Rényi model)
    graphs['random'] = nx.erdos_renyi_graph(10, 0.5)  # Random graph with 10 nodes, each edge is included with probability 0.5

    # 18. Regular Graph
    graphs['regular'] = nx.random_regular_graph(3, 10)  # Random regular graph with 10 nodes, each node has degree 3

    # 19. Multigraph
    graphs['multigraph'] = nx.MultiGraph()
    graphs['multigraph'].add_edge(1, 2)
    graphs['multigraph'].add_edge(1, 2)  # Parallel edge
    graphs['multigraph'].add_edge(2, 3)

    return graphs

def max_op(x, y): return max(x, y)

def add_op(x, y): return x + y

def mul_op(x, y): return x * y

def union_op(a, b):
    if not a:
        return b
    if not b:
        return a
    return a.union(b)

def combine_op(x, y):
    if x == frozenset({-1}):
        return frozenset()
    if y == frozenset({-1}):
        return frozenset()
    if x.issubset(y):
        return y
    if y.issubset(x):
        return x
    combined_set = set()
    for element_x in x:
        combined_set.add((element_x))
    for element_y in y:
        combined_set.add((element_y))
    return frozenset(combined_set)

def main():
    graphs = generate_edge_case_graphs()


    base_semiring = CommutativeSemiring[max_op,add_op](max_op, add_op, float('-inf'), 0, 0)
    extension_semiring_counting = CommutativeSemiring[add_op,mul_op](add_op, mul_op, 0, 1, 0)
    extension_semiring_sampling = CommutativeSemiring[union_op,combine_op](union_op, combine_op, frozenset({-1}), frozenset(), value={frozenset({1}), frozenset({2})}, samples={frozenset({2}), frozenset({1, 5, 4})})
    semiring_extension = SelectiveSemiringExtension(base_semiring, extension_semiring_counting, extension_semiring_sampling)

    mis_calculator = MISQuery(graphs['regular'], semiring_extension)
    mis = mis_calculator.calculate_mis()

    print("MIS with SCE:", mis)

    pos = nx.spring_layout(graphs['regular'])
    nx.draw(graphs['regular'], pos, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()
