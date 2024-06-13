class ConfirmCommutativeSemiring:
    def __init__(self, aggregation_op, combination_op, zero, one, samples):
        """Initializes a validator for semiring properties with given operations and neutral elements."""
        self.aggregation_op = aggregation_op
        self.combination_op = combination_op
        self.zero = zero
        self.one = one
        self.samples = samples
        self.verify_semiring_properties()

    def verify_commutative(self):
        """Checks that the aggregation operation is commutative over the set of samples."""
        for a in self.samples:
            for b in self.samples:
                assert self.aggregation_op(a, b) == self.aggregation_op(b, a), "Commutative property fails"

    def verify_monoid(self, ):
        """Verifies monoid properties (identity and associativity) for both operations over the samples."""
        for a in self.samples:
            assert self.aggregation_op(a,self.zero) == a, "Identity fails"
            assert self.combination_op(a,self.one) == a, "Identity fails"
            assert self.aggregation_op(a,self.zero) == a, "Identity fails"
            assert self.combination_op(a,self.one) == a, "Identity fails"
            for b in self.samples:
                for c in self.samples:
                    assert  self.aggregation_op(a,self.aggregation_op(b,c)) == self.aggregation_op(self.aggregation_op(a,b),c) , "Associative property fails"
                    assert  self.combination_op(a,self.combination_op(b,c)) == self.combination_op(self.combination_op(a,b),c), "Associative property fails"

    def verify_distributive_property(self):
        """Ensures the distributive property holds between the operations across the samples."""
        for a in self.samples:
            for b in self.samples:
                for c in self.samples:
                    assert self.combination_op(a, self.aggregation_op(b, c)) == \
                           self.aggregation_op(self.combination_op(a, b), self.combination_op(a, c)), \
                           "Distributive property fails"

    def verify_semiring_properties(self):
        """Coordinates the verification of all semiring properties."""
        self.verify_commutative()
        self.verify_monoid()
        self.verify_distributive_property()