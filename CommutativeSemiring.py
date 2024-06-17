from typing import Callable, TypeVar, Generic

# Define the type variables
AGG = TypeVar('AGG', bound=Callable[[int, int], int])
COMB = TypeVar('COMB', bound=Callable[[int, int], int])

class CommutativeSemiring(Generic[AGG, COMB]):
    def __init__(self, aggregation_op: AGG, combination_op: COMB, zero, one, value):
        '''
        Initializes the CommutativeSemiring class.

        Args:
            aggregation_op (AGG): The aggregation operation.
            combination_op (COMB): The combination operation.
            zero (int): The zero element.
            one (int): The one element.
            value (int): The value of the semiring.
        '''
        self.aggregation_op = aggregation_op
        self.combination_op = combination_op
        self.zero = zero
        self.one = one
        self.value = value 

    def __add__(self, other: 'CommutativeSemiring[AGG, COMB]') -> 'CommutativeSemiring[AGG, COMB]':
        '''
        Defines the addition operation between two semirings.
        Args:
            other (CommutativeSemiring): The other semiring to add.

        Returns:
            CommutativeSemiring: The result of the addition.
        '''
        # Confirm that the semirings are of the same type
        if self.combination_op is not other.combination_op or self.aggregation_op is not other.aggregation_op:
            raise TypeError("Cannot add or multiply on different semirings!")
        # Perform the aggregation operation
        new_value = self.aggregation_op(self.value, other.value)
        return CommutativeSemiring[self.aggregation_op, self.combination_op](self.aggregation_op, self.combination_op, self.zero, self.one, new_value)

    def __mul__(self, other: 'CommutativeSemiring[AGG, COMB]') -> 'CommutativeSemiring[AGG, COMB]':
        # Confirm that the semirings are of the same type
        if self.combination_op is not other.combination_op or self.aggregation_op is not other.aggregation_op:
            raise TypeError("Cannot add or multiply on different semirings!")
        # Perform the combination operation
        new_value = self.combination_op(self.value, other.value)
        return CommutativeSemiring[self.aggregation_op, self.combination_op](self.aggregation_op, self.combination_op, self.zero, self.one, new_value)

    def __repr__(self):
        '''
        Returns the string representation of the CommutativeSemiring class.

        Returns:
            str: The string representation of the CommutativeSemiring class.
        '''
        return f"CommutativeSemiring(value={self.value})"

    