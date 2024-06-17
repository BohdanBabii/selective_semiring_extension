import networkx as nx
import matplotlib.pyplot as plt
from CommutativeSemiring import CommutativeSemiring 
from MISQuery import MISQuery
from SelectiveSemiringExtension import SelectiveSemiringExtension
from SemiringOperations import SemiringOperations

def generate_edge_case_graphs():
    '''
    Generates a set of edge case graphs for testing the MIS algorithm.
    
    Returns:
        dict: A dictionary of edge case graphs.
    '''
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
    graphs['disconnected'].add_edges_from([(1, 2), (3, 4)])

    # 5. Complete Graph
    graphs['complete'] = nx.complete_graph(5)

    # 6. Star Graph
    graphs['star'] = nx.star_graph(4)

    # 7. Line Graph (Path Graph)
    graphs['line'] = nx.path_graph(5)

    # 8. Cycle Graph
    graphs['cycle'] = nx.cycle_graph(5)

    # 9. Binary Tree
    graphs['binary_tree'] = nx.balanced_tree(2, 3)

    # 10. Bipartite Graph
    graphs['bipartite'] = nx.complete_bipartite_graph(3, 3)

    # 11. Wheel Graph
    graphs['wheel'] = nx.wheel_graph(5)

    # 12. Tree Graph (Non-Binary)
    graphs['tree'] = nx.balanced_tree(3, 2)

    # 13. Ladder Graph
    graphs['ladder'] = nx.ladder_graph(5) 

    # 14. Circular Ladder Graph
    graphs['circular_ladder'] = nx.circular_ladder_graph(5)

    # 15. Barbell Graph
    graphs['barbell'] = nx.barbell_graph(5, 1)

    # 16. Random Graph
    graphs['random'] = nx.erdos_renyi_graph(10, 0.5)

    # 17. Regular Graph
    graphs['regular'] = nx.random_regular_graph(3, 10)

    # 18. Failing Graph
    graphs['failing_graph'] = nx.Graph()
    graphs['failing_graph'].add_nodes_from([0,1,2,3,4,5,6,7,8,9])
    graphs['failing_graph'].add_edges_from([(1,2), (2,3), (1,3), (3,8), (3,6), (8,5), (4,5), (7,8), (0,7), (0,9)])
    
    return graphs

def main():
    # Generate the edge case graphs
    graphs = generate_edge_case_graphs()

    # Select the graph to test
    graph_name = 'failing_graph'
    graph = graphs[graph_name]

    # Define the semiring operations
    ops = SemiringOperations()

    # Define the semiring extension
    base_semiring = CommutativeSemiring[ops.max_op,ops.add_op](ops.max_op, ops.add_op, float('-inf'), 0, 0)
    extension_semiring_counting = CommutativeSemiring[ops.add_op,ops.mul_op](ops.add_op, ops.mul_op, 0, 1, 0)
    extension_semiring_sampling = CommutativeSemiring[ops.union_op,ops.combine_op](ops.union_op, ops.combine_op, frozenset({-1}), frozenset(), value=None)
    semiring_extension = SelectiveSemiringExtension(base_semiring, extension_semiring_counting, extension_semiring_sampling)

    # Calculate the MIS using the semiring extension
    mis_calculator = MISQuery(graph, semiring_extension)
    mis = mis_calculator.calculate_mis()

    # Calculate the MIS using NetworkX
    misNX = nx.maximal_independent_set(graph)

    # Print the results
    print(graph_name)
    print("MIS with SCE:", mis)
    print('MIS with NX: ', misNX)

    # Draw the graph
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()
