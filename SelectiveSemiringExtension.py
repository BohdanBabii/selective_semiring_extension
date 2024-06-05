from CommutativeSemiring import CommutativeSemiring

class SelectiveSemiringExtension:
    def __init__(self, base_semiring, extension_semiring):
        self.base_semiring = base_semiring
        self.extension_semiring = extension_semiring

    def __add__(self, other):
        # Aggregation operation combines two semiring extensions by aggregating their values and counts.
        new_value = self.base_semiring.value + other.base_semiring.value
        if self.base_semiring.value == new_value:
            new_count = self.extension_semiring.value
        elif other.base_semiring.value == new_value:
            new_count = other.extension_semiring.value
        else:
            new_count = self.extension_semiring.value + other.extension_semiring.value

        return SelectiveSemiringExtension(
            CommutativeSemiring(self.base_semiring.aggregation_op, self.base_semiring.combination_op, self.base_semiring.zero, self.base_semiring.one, new_value),
            CommutativeSemiring(self.extension_semiring.aggregation_op, self.extension_semiring.combination_op, self.extension_semiring.zero, self.extension_semiring.one, new_count)
        )

    def __mul__(self, other):
        # Combination operation multiplies two semiring extensions by combining their values.
        new_value = self.base_semiring.value * other.base_semiring.value
        new_count = self.extension_semiring.value * other.extension_semiring.value

        return SelectiveSemiringExtension(
            CommutativeSemiring(self.base_semiring.aggregation_op, self.base_semiring.combination_op, self.base_semiring.zero, self.base_semiring.one, new_value),
            CommutativeSemiring(self.extension_semiring.aggregation_op, self.extension_semiring.combination_op, self.extension_semiring.zero, self.extension_semiring.one, new_count)
        )

    def __repr__(self):
        return f"SelectiveSemiringExtension(base={self.base_semiring}, extension={self.extension_semiring})"
