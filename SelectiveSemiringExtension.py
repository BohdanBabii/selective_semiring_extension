from CommutativeSemiring import CommutativeSemiring

class SelectiveSemiringExtension:
    
    def __init__(self, base_semiring, extension_counting, extension_sampling):
        """Initialize with a base, extension semiring for counting and extensions semiring for sampling."""
        self.base_semiring = base_semiring
        self.extension_counting = extension_counting
        self.extension_sampling = extension_sampling

    def __add__(self, other):
        """Defines the aggregation operation between three semiring extensions."""

        new_base_value = self.base_semiring.aggregation_op(self.base_semiring.value, other.base_semiring.value)

        new_extension_counting_1 = self.extension_counting.combination_op(self.extension_counting.value, 1 if self.base_semiring.value == new_base_value else 0)
        new_extension_counting_2 = other.extension_counting.combination_op(other.extension_counting.value, 1 if other.base_semiring.value == new_base_value else 0)
        new_extension_counting = self.extension_counting.aggregation_op(new_extension_counting_1, new_extension_counting_2)

        new_extension_sampling_1 = self.extension_sampling.combination_op(self.extension_sampling.value, self.extension_sampling.one if self.base_semiring.value == new_base_value else self.extension_sampling.zero)
        new_extension_sampling_2 = other.extension_sampling.combination_op(other.extension_sampling.value, self.extension_sampling.one if other.base_semiring.value == new_base_value else self.extension_sampling.zero)
        new_extension_sampling = self.extension_sampling.aggregation_op(new_extension_sampling_1, new_extension_sampling_2)

        return SelectiveSemiringExtension(
            CommutativeSemiring(self.base_semiring.aggregation_op, self.base_semiring.combination_op, self.base_semiring.zero, self.base_semiring.one, new_base_value),
            CommutativeSemiring(self.extension_counting.aggregation_op, self.extension_counting.combination_op, self.extension_counting.zero, self.extension_counting.one, new_extension_counting),
            CommutativeSemiring(self.extension_sampling.aggregation_op, self.extension_sampling.combination_op, self.extension_sampling.zero, self.extension_sampling.one, new_extension_sampling)
        )

    def __mul__(self, other):
        """Defines the combination operation between three semiring extensions."""

        new_base_value = self.base_semiring.combination_op(self.base_semiring.value, other.base_semiring.value)

        new_extension_counting = self.extension_counting.combination_op(self.extension_counting.value, other.extension_counting.value)

        new_extension_sampling = self.extension_sampling.combination_op(self.extension_sampling.value, other.extension_sampling.value)

        return SelectiveSemiringExtension(
            CommutativeSemiring(self.base_semiring.aggregation_op, self.base_semiring.combination_op, self.base_semiring.zero, self.base_semiring.one, new_base_value),
            CommutativeSemiring(self.extension_counting.aggregation_op, self.extension_counting.combination_op, self.extension_counting.zero, self.extension_counting.one, new_extension_counting),
            CommutativeSemiring(self.extension_sampling.aggregation_op, self.extension_sampling.combination_op, self.extension_sampling.zero, self.extension_sampling.one, new_extension_sampling)
        )

    def __repr__(self):
        """Provide a string representation of the semiring extension."""
        return f"SelectiveSemiringExtension(MIS Size={self.base_semiring}, MIS Count={self.extension_counting}, MIS Sampling={self.extension_sampling})"
