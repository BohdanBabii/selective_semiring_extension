from ConfirmCommutativeSemiring import ConfirmCommutativeSemiring

class CommutativeSemiring:
    def __init__(self, aggregation_op, combination_op, zero, one, value, count=1):
        self.aggregation_op = aggregation_op
        self.combination_op = combination_op
        self.zero = zero
        self.one = one
        self.value = value 
        self.verify_properties()

    def verify_properties(self):
        validator = ConfirmCommutativeSemiring(self.aggregation_op, self.combination_op, self.zero, self.one)
        validator.verify_semiring_properties()

    def verify_properties(self):
        validator = ConfirmCommutativeSemiring(self.aggregation_op, self.combination_op, self.zero, self.one)
        validator.verify_semiring_properties()

    def __add__(self, other):
        if not isinstance(other, CommutativeSemiring):
            return NotImplemented
        new_value = self.aggregation_op(self.value, other.value)
        return CommutativeSemiring(self.aggregation_op, self.combination_op, self.zero, self.one, new_value)

    def __mul__(self, other):
        if not isinstance(other, CommutativeSemiring):
            return NotImplemented
        new_value = self.combination_op(self.value, other.value)
        return CommutativeSemiring(self.aggregation_op, self.combination_op, self.zero, self.one, new_value)

    def __repr__(self):
        return f"CommutativeSemiring(value={self.value})"

    