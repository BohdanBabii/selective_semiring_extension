from CommutativeSemiring import CommutativeSemiring

class SelectiveSemiringExtension:
    def __init__(self, base_semiring, extension_counting, extension_sampling):
        """
        Initialize the SelectiveSemiringExtension class.

        Args:
            base_semiring (CommutativeSemiring): The base semiring.
            extension_counting (CommutativeSemiring): The counting extension of the semiring.
            extension_sampling (CommutativeSemiring): The sampling extension of the semiring.
        """
        self.base_semiring = base_semiring
        self.extension_counting = extension_counting
        self.extension_sampling = extension_sampling

    def __add__(self, other):
        """
        Defines the aggregation operation between three semiring extensions.

        Args:
            other (SelectiveSemiringExtension): The other semiring extension to aggregate.
        
        Returns:
            SelectiveSemiringExtension: The aggregated semiring extension.
        """
        # Aggregate the base values
        new_base_value = self.base_semiring.aggregation_op(
            self.base_semiring.value, 
            other.base_semiring.value
        )
        # Aggregate the counting components by checking if the base value is the new base value
        new_extension_counting = self.extension_counting.aggregation_op(
            self.extension_counting.combination_op(
                self.extension_counting.value, 
                1 if self.base_semiring.value == new_base_value else 0
            ), 
            other.extension_counting.combination_op(
                other.extension_counting.value, 
                1 if other.base_semiring.value == new_base_value else 0
            )
        )
        # Aggregate the sampling components by checking if the base value is the new base value
        new_extension_sampling = self.extension_sampling.aggregation_op(
            self.extension_sampling.combination_op(
                self.extension_sampling.value, 
                self.extension_sampling.one if self.base_semiring.value == new_base_value else self.extension_sampling.zero
            ), 
            other.extension_sampling.combination_op(
                other.extension_sampling.value, 
                self.extension_sampling.one if other.base_semiring.value == new_base_value else self.extension_sampling.zero
            )
        )
        # Return the new semiring extension
        return SelectiveSemiringExtension(
            CommutativeSemiring[self.base_semiring.aggregation_op, self.base_semiring.combination_op](
                self.base_semiring.aggregation_op, self.base_semiring.combination_op, 
                self.base_semiring.zero, self.base_semiring.one, new_base_value
            ),
            CommutativeSemiring[self.extension_counting.aggregation_op, self.extension_counting.combination_op](
                self.extension_counting.aggregation_op, self.extension_counting.combination_op, 
                self.extension_counting.zero, self.extension_counting.one, new_extension_counting
            ),
            CommutativeSemiring[self.extension_sampling.aggregation_op, self.extension_sampling.combination_op](
                self.extension_sampling.aggregation_op, self.extension_sampling.combination_op, 
                self.extension_sampling.zero, self.extension_sampling.one, new_extension_sampling
            )
        )

    def __mul__(self, other):
        """
        Defines the combination operation between three semiring extensions.

        Args:
            other (SelectiveSemiringExtension): The other semiring extension to combine.
        
        Returns:
            SelectiveSemiringExtension: The combined semiring extension.
        """
        # Combine the base values
        new_base_value = self.base_semiring.combination_op(
            self.base_semiring.value, other.base_semiring.value
        )
        # Combine the counting components
        new_extension_counting = self.extension_counting.combination_op(
            self.extension_counting.value, 
            other.extension_counting.value
        )
        # Combine the sampling components
        new_extension_sampling = self.extension_sampling.combination_op(
            self.extension_sampling.value, 
            other.extension_sampling.value
        )
        # Return the new semiring extension
        return SelectiveSemiringExtension(
            CommutativeSemiring[self.base_semiring.aggregation_op, self.base_semiring.combination_op](
                self.base_semiring.aggregation_op, self.base_semiring.combination_op, 
                self.base_semiring.zero, self.base_semiring.one, new_base_value
            ),
            CommutativeSemiring[self.extension_counting.aggregation_op, self.extension_counting.combination_op](
                self.extension_counting.aggregation_op, self.extension_counting.combination_op, 
                self.extension_counting.zero, self.extension_counting.one, new_extension_counting
            ),
            CommutativeSemiring[self.extension_sampling.aggregation_op, self.extension_sampling.combination_op](
                self.extension_sampling.aggregation_op, self.extension_sampling.combination_op, 
                self.extension_sampling.zero, self.extension_sampling.one, new_extension_sampling
            )
        )

    def __repr__(self):
        """
        Provide a string representation of the semiring extension.

        Returns:
            str: The string representation of the semiring extension.
        """
        return f"SelectiveSemiringExtension(MIS Size={self.base_semiring}, " \
               f"MIS Count={self.extension_counting}, MIS Sampling={self.extension_sampling})"
