from ConfirmCommutativeSemiring import ConfirmCommutativeSemiring
from typing import Callable, TypeVar, Generic, Any

AGG = TypeVar('AGG', bound=Callable[[int, int], int])
COMB = TypeVar('COMB', bound=Callable[[int, int], int])

class CommutativeSemiring(Generic[AGG, COMB]):
    def __init__(self, aggregation_op: AGG, combination_op: COMB, zero, one, value, samples={frozenset({1, 4, 3}), frozenset({1, 5, 4})}):
        self.aggregation_op = aggregation_op
        self.combination_op = combination_op
        self.zero = zero
        self.one = one
        self.value = value 
        self.samples = samples
        self.combination_opsamples = samples
        #self.verify_properties()

    def verify_properties(self):
        validator = ConfirmCommutativeSemiring(self.aggregation_op, self.combination_op, self.zero, self.one)
        validator.verify_semiring_properties()

    def verify_properties(self):
        validator = ConfirmCommutativeSemiring(self.aggregation_op, self.combination_op, self.zero, self.one, samples=self.samples)
        validator.verify_semiring_properties()

    def __add__(self, other: 'CommutativeSemiring[AGG, COMB]') -> 'CommutativeSemiring[AGG, COMB]':
        if self.combination_op is not other.combination_op or self.aggregation_op is not other.aggregation_op:
            raise TypeError("Cannot add or multiply on different semirings!")
        new_value = self.aggregation_op(self.value, other.value)
        return CommutativeSemiring(self.aggregation_op, self.combination_op, self.zero, self.one, new_value)

    def __mul__(self, other: 'CommutativeSemiring[AGG, COMB]') -> 'CommutativeSemiring[AGG, COMB]':
        if self.combination_op is not other.combination_op or self.aggregation_op is not other.aggregation_op:
            raise TypeError("Cannot add or multiply on different semirings!")
        new_value = self.combination_op(self.value, other.value)
        return CommutativeSemiring(self.aggregation_op, self.combination_op, self.zero, self.one, new_value)

    def __repr__(self):
        return f"CommutativeSemiring(value={self.value})"

    