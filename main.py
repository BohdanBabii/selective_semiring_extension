import networkx as nx
import matplotlib.pyplot as plt
from CommutativeSemiring import CommutativeSemiring 
from SelectiveSemiringExtension import SelectiveSemiringExtension 
from MISQuery import MISQuery

def max_op(x, y):
    return max(x, y)

def add_op(x, y):
    return x + y

def mul_op(x, y):
    return x * y

def main():

    F = nx.connected_watts_strogatz_graph(12, 3, 0.1)
    base_semiring = CommutativeSemiring(max_op, add_op, float('-inf'), 0, 0)
    extension_semiring = CommutativeSemiring(add_op, mul_op, 0, 1, 1)
    semiring_extension = SelectiveSemiringExtension(base_semiring, extension_semiring)

    mis_calculator = MISQuery(F, semiring_extension)
    mis = mis_calculator.calculate_mis()
    print("MIS with SCE:", mis)

    pos = nx.spring_layout(F)
    nx.draw(F, pos, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()
