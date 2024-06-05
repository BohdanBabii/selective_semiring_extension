class ConfirmCommutativeSemiring:
    def __init__(self, aggregation_op, combination_op, zero, one):
        self.aggregation_op = aggregation_op
        self.combination_op = combination_op
        self.zero = zero
        self.one = one
        self.samples = range(10)
        self.verify_semiring_properties()

    def verify_commutative(self):
        for a in self.samples:
            for b in self.samples:
                assert self.aggregation_op(a, b) == self.aggregation_op(b, a), "Commutative property fails"

    def verify_monoid(self, ):
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
        for a in self.samples:
            for b in self.samples:
                for c in self.samples:
                    assert self.combination_op(a, self.aggregation_op(b, c)) == \
                           self.aggregation_op(self.combination_op(a, b), self.combination_op(a, c)), \
                           "Distributive property fails"

    def verify_semiring_properties(self):
        assert len(set(self.samples)) >= 2, "Too few samples to verify properties"
        self.verify_commutative()
        self.verify_monoid()
        self.verify_monoid()
        self.verify_distributive_property()