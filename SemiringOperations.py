class SemiringOperations:
    def __init__(self):
        pass

    @staticmethod
    def max_op(x, y):
        return max(x, y)

    @staticmethod
    def add_op(x, y):
        return x + y

    @staticmethod
    def mul_op(x, y):
        return x * y

    @staticmethod
    def union_op(a, b):
        if not a:
            return b
        if not b:
            return a
        return a.union(b)

    @staticmethod
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
