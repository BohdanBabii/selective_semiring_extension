import networkx as nx
import matplotlib.pyplot as plt
from CommutativeSemiring import CommutativeSemiring 
from SelectiveSemiringExtension import SelectiveSemiringExtension 

def max_op(x, y):
    return max(x, y)

def add_op(x, y):
    return x + y

def mul_op(x, y):
    return x * y

def main():
    # Initialize semirings with appropriate starting values
    a1 = CommutativeSemiring(max_op, add_op, float('-inf'), 0, 1)
    a2 = CommutativeSemiring(max_op, add_op, float('-inf'), 0, 2)
    a3 = CommutativeSemiring(max_op, add_op, float('-inf'), 0, 3)

    b1 = CommutativeSemiring(add_op, mul_op, 0, 1, 1)
    b2 = CommutativeSemiring(add_op, mul_op, 0, 1, 1)
    b3 = CommutativeSemiring(add_op, mul_op, 0, 1, 1)

    c1 = SelectiveSemiringExtension(a1, b1)
    c2 = SelectiveSemiringExtension(a2, b2)
    c3 = SelectiveSemiringExtension(a2, b3)


    d1 = c1 * c2
    d2 = d1 * c3
    print(d2)


if __name__ == "__main__":
    main()
