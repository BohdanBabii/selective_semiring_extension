class ConfirmCommutativeSemiring:
    def __init__(self, aggregation_op, combination_op, zero, one, samples):
        """
        Initializes the ConfirmCommutativeSemiring class.

        Args:
            aggregation_op (Callable): The aggregation operation.
            combination_op (Callable): The combination operation.
            zero (int): The zero element.
            one (int): The one element.
            samples (list): The list of samples.
        """
        self.aggregation_op = aggregation_op
        self.combination_op = combination_op
        self.zero = zero
        self.one = one
        self.samples = samples

    def verify_commutative(self):
        """
        Verifies the commutative property.

        Raises:
            ValueError: If the commutative property fails.
        """
        for a in self.samples:
            for b in self.samples:
                assert self.aggregation_op(a, b) == self.aggregation_op(b, a), "Commutative property fails"

    def verify_monoid(self, ):
        """
        Verifies monoid properties (identity and associativity).

        Raises:
            ValueError: If any monoid property validation fails.
        """
        for a in self.samples:
            assert self.aggregation_op(a,self.zero) == a, "Identity fails"
            assert self.combination_op(a,self.one) == a, "Identity fails"
            assert self.aggregation_op(a,self.zero) == a, "Identity fails"
            assert self.combination_op(a,self.one) == a, "Identity fails"
            for b in self.samples:
                for c in self.samples:
                    assert  self.aggregation_op(a,self.aggregation_op(b,c)) == \
                            self.aggregation_op(self.aggregation_op(a,b),c) , "Associative property fails"
                    assert  self.combination_op(a,self.combination_op(b,c)) == \
                            self.combination_op(self.combination_op(a,b),c), "Associative property fails"

    def verify_distributive_property(self):
        """
        Verifies the distributive property.
        """
        for a in self.samples:
            for b in self.samples:
                for c in self.samples:
                    assert self.combination_op(a, self.aggregation_op(b, c)) == \
                           self.aggregation_op(self.combination_op(a, b), self.combination_op(a, c)), \
                           "Distributive property fails"

    def verify_semiring_properties(self):
        """
        Verifies the semiring properties.
        
        Raises:
            ValueError: If any semiring property validation fails.
        """
        try:
            self._verify_commutative()
            self._verify_monoid()
            self._verify_distributive_property()
        except AssertionError as e:
            raise ValueError(str(e))