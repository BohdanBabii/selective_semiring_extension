from CommutativeSemiring import CommutativeSemiring

class SelectiveSemiringExtension:
    def __init__(self, base_semiring, extension_semiring):
        self.base_semiring = base_semiring
        self.extension_semiring = extension_semiring

    def __add__(self, other):
        new_base_value = self.base_semiring.aggregation_op(self.base_semiring.value, other.base_semiring.value)

        new_extension_value1 = self.extension_semiring.combination_op(self.extension_semiring.value, 1 if self.base_semiring.value == new_base_value else 0)
        new_extension_value2 = other.extension_semiring.combination_op(other.extension_semiring.value, 1 if other.base_semiring.value == new_base_value else 0)

        new_extension_value = self.extension_semiring.aggregation_op(new_extension_value1, new_extension_value2)

        return SelectiveSemiringExtension(
            CommutativeSemiring(self.base_semiring.aggregation_op, self.base_semiring.combination_op, self.base_semiring.zero, self.base_semiring.one, new_base_value),
            CommutativeSemiring(self.extension_semiring.aggregation_op, self.extension_semiring.combination_op, self.extension_semiring.zero, self.extension_semiring.one, new_extension_value)
        )

    def __mul__(self, other):
        new_base_value = self.base_semiring.combination_op(self.base_semiring.value, other.base_semiring.value)
        new_extension_value = self.extension_semiring.combination_op(self.extension_semiring.value, other.extension_semiring.value)

        return SelectiveSemiringExtension(
            CommutativeSemiring(self.base_semiring.aggregation_op, self.base_semiring.combination_op, self.base_semiring.zero, self.base_semiring.one, new_base_value),
            CommutativeSemiring(self.extension_semiring.aggregation_op, self.extension_semiring.combination_op, self.extension_semiring.zero, self.extension_semiring.one, new_extension_value)
        )

    def __repr__(self):
        return f"SelectiveSemiringExtension(base={self.base_semiring}, extension={self.extension_semiring})"
