from CommutativeSemiring import CommutativeSemiring
from SelectiveSemiringExtensionSampling import SelectiveSemiringExtensionSampling
import itertools

class MISQuerySampling:
    def __init__(self, graph, semiring_extension):
        self.graph = graph
        self.semiring_extension = semiring_extension
        self.nodes_list = list(self.graph.nodes())

    def calculate_mis(self):
        combinations = list(itertools.product([0, 1], repeat=len(self.graph.nodes())))
        zero_base = CommutativeSemiring[self.semiring_extension.base_semiring.aggregation_op,self.semiring_extension.base_semiring.combination_op](
            self.semiring_extension.base_semiring.aggregation_op,
            self.semiring_extension.base_semiring.combination_op,
            self.semiring_extension.base_semiring.zero,
            self.semiring_extension.base_semiring.one,
            float('-inf')
        )
        zero_extension_counting = CommutativeSemiring[self.semiring_extension.extension_counting.aggregation_op,self.semiring_extension.extension_counting.combination_op](
            self.semiring_extension.extension_counting.aggregation_op,
            self.semiring_extension.extension_counting.combination_op,
            self.semiring_extension.extension_counting.zero,
            self.semiring_extension.extension_counting.one,
            0
        )
        zero_extension_sampling = CommutativeSemiring[self.semiring_extension.extension_sampling.aggregation_op,self.semiring_extension.extension_sampling.combination_op](
            self.semiring_extension.extension_sampling.aggregation_op,
            self.semiring_extension.extension_sampling.combination_op,
            self.semiring_extension.extension_sampling.zero,
            self.semiring_extension.extension_sampling.one,
            frozenset()
        )

        best_result = SelectiveSemiringExtensionSampling(zero_base, zero_extension_counting, zero_extension_sampling)

        for combination in combinations:
            value = 0
            ele = frozenset()

            best_base = CommutativeSemiring(
                self.semiring_extension.base_semiring.aggregation_op,
                self.semiring_extension.base_semiring.combination_op,
                self.semiring_extension.base_semiring.zero,
                self.semiring_extension.base_semiring.one,
                0 
            )

            best_sample = CommutativeSemiring(
                self.semiring_extension.extension_sampling.aggregation_op,
                self.semiring_extension.extension_sampling.combination_op,
                self.semiring_extension.extension_sampling.zero,
                self.semiring_extension.extension_sampling.one,
                frozenset()
            )

            for i, j in self.graph.edges():
                if combination[i-1] == 1 and combination[j-1] == 1:
                    value = float('-inf')
                    break

            if value != float('-inf'):
                for i in range(len(combination)):
                    value = combination[i]

                    current_base = CommutativeSemiring(
                            self.semiring_extension.base_semiring.aggregation_op,
                            self.semiring_extension.base_semiring.combination_op,
                            self.semiring_extension.base_semiring.zero,
                            self.semiring_extension.base_semiring.one,
                            value
                    )

                    best_base = best_base * current_base

                    if combination[i]:
                        ele = self.semiring_extension.extension_sampling.combination_op(ele, frozenset({i+1}))


                best_sample = CommutativeSemiring(
                        self.semiring_extension.extension_sampling.aggregation_op,
                        self.semiring_extension.extension_sampling.combination_op,
                        self.semiring_extension.extension_sampling.zero,
                        self.semiring_extension.extension_sampling.one,
                        {ele}
                )

            zero_extension_counting = CommutativeSemiring(
                self.semiring_extension.extension_counting.aggregation_op,
                self.semiring_extension.extension_counting.combination_op,
                self.semiring_extension.extension_counting.zero,
                self.semiring_extension.extension_counting.one,
                1
            )

            current_extension = SelectiveSemiringExtensionSampling(best_base, zero_extension_counting, best_sample)
            
            best_result = best_result + current_extension

        return best_result