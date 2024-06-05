from itertools import combinations
from CommutativeSemiring import CommutativeSemiring
from SelectiveSemiringExtension import SelectiveSemiringExtension

class MISQuery:
    def __init__(self, graph, semiring_extension):
        self.graph = graph
        self.semiring_extension = semiring_extension

    def is_independent_set(self, subset):
        """Check if the given subset of vertices forms an independent set."""
        for v in subset:
            for u in subset:
                if v != u and self.graph.has_edge(v, u):
                    return False
        return True
    
    def generate_all_subsets(self):
        """Generate all subsets of the graph's nodes."""
        return (subset for r in range(len(self.graph.nodes()) + 1) 
                          for subset in combinations(self.graph.nodes(), r))

    def calculate_mis(self):
        """Calculate the maximum independent set using the selective semiring extension."""
        zero_base = CommutativeSemiring(
            self.semiring_extension.base_semiring.aggregation_op,
            self.semiring_extension.base_semiring.combination_op,
            self.semiring_extension.base_semiring.zero,
            self.semiring_extension.base_semiring.one,
            float('-inf')
        )
        zero_extension = CommutativeSemiring(
            self.semiring_extension.extension_semiring.aggregation_op,
            self.semiring_extension.extension_semiring.combination_op,
            self.semiring_extension.extension_semiring.zero,
            self.semiring_extension.extension_semiring.one,
            1
        )
        best_result = SelectiveSemiringExtension(zero_base, zero_extension)

        all_subsets = self.generate_all_subsets()
        
        for subset in all_subsets:
            if self.is_independent_set(subset):
                temp_base = CommutativeSemiring(
                    self.semiring_extension.base_semiring.aggregation_op,
                    self.semiring_extension.base_semiring.combination_op,
                    self.semiring_extension.base_semiring.zero,
                    self.semiring_extension.base_semiring.one,
                    value=len(subset) 
                )
                temp_extension = CommutativeSemiring(
                    self.semiring_extension.extension_semiring.aggregation_op,
                    self.semiring_extension.extension_semiring.combination_op,
                    self.semiring_extension.extension_semiring.zero,
                    self.semiring_extension.extension_semiring.one
                )
                current_extended = SelectiveSemiringExtension(temp_base, temp_extension)
            
                best_result = best_result + current_extended 
        
        return best_result
