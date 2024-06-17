import itertools
import random
from CommutativeSemiring import CommutativeSemiring
from SelectiveSemiringExtension import SelectiveSemiringExtension


class MISQuery:
    def __init__(self, graph, semiring_extension):
        '''
        Initializes the MISQuery class.

        Args:
            graph (nx.Graph): Graph on which MIS is calculated.
            semiring_extension (SelectiveSemiringExtension): The semiring extension to use for the query.
        '''
        self.graph = graph
        self.semiring_extension = semiring_extension
        self.nodes_list = list(self.graph.nodes())


    def random_set(self, all_sets: set[frozenset]) -> frozenset:
        """
        Returns a random set from a collection of sets.
        
        Args:
            all_sets (Set[frozenset]): The collection of frozensets to choose from.

        Returns:
            frozenset: A randomly chosen set from the collection.
        """
        if not all_sets:
            return frozenset()
        return random.choice(list(all_sets))


    def calculate_mis(self):
        '''
        Calculates the maximum independent set of the graph using the provided semiring extension.

        Returns:
            SelectiveSemiringExtension: The size, the count and a random sample of the maximum independent set.
        '''

        combinations = list(itertools.product([0, 1], repeat=len(self.graph.nodes()))) # Generate all possible combinations of 0 and 1 for the nodes

        # Initialize the zero elements of the semirings
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

        # Initialize the default best result
        best_result = SelectiveSemiringExtension(zero_base, zero_extension_counting, zero_extension_sampling)

        # Iterate over all possible combinations of nodes
        for combination in combinations:
            is_valid = True
            current_element = frozenset()

            # Initialize the best base and sample
            best_base = CommutativeSemiring[self.semiring_extension.base_semiring.aggregation_op,self.semiring_extension.base_semiring.combination_op](
                self.semiring_extension.base_semiring.aggregation_op,
                self.semiring_extension.base_semiring.combination_op,
                self.semiring_extension.base_semiring.zero,
                self.semiring_extension.base_semiring.one,
                0 
            )

            best_sample = CommutativeSemiring[self.semiring_extension.extension_sampling.aggregation_op, self.semiring_extension.extension_sampling.combination_op](
                self.semiring_extension.extension_sampling.aggregation_op,
                self.semiring_extension.extension_sampling.combination_op,
                self.semiring_extension.extension_sampling.zero,
                self.semiring_extension.extension_sampling.one,
                frozenset()
            )

            # Check if the combination is valid
            for i, j in self.graph.edges():
                if combination[i - 1] == 1 and combination[j - 1] == 1:
                    is_valid = False
                    break
            
            # If the combination is valid, calculate the base and sample
            if is_valid:
                for i, selected in enumerate(combination):
                    if selected:
                        current_base = CommutativeSemiring[self.semiring_extension.base_semiring.aggregation_op,self.semiring_extension.base_semiring.combination_op](
                                self.semiring_extension.base_semiring.aggregation_op,
                                self.semiring_extension.base_semiring.combination_op,
                                self.semiring_extension.base_semiring.zero,
                                self.semiring_extension.base_semiring.one,
                                selected
                        )
                        # Update the base
                        best_base *= current_base
                        # Update the sample
                        element = frozenset({0}) if i == len(combination) - 1 else frozenset({i + 1})
                        current_element = self.semiring_extension.extension_sampling.combination_op(current_element, element)
                # Update the best sample
                best_sample = CommutativeSemiring[self.semiring_extension.extension_sampling.aggregation_op, self.semiring_extension.extension_sampling.combination_op](
                        self.semiring_extension.extension_sampling.aggregation_op,
                        self.semiring_extension.extension_sampling.combination_op,
                        self.semiring_extension.extension_sampling.zero,
                        self.semiring_extension.extension_sampling.one,
                        {current_element}
                )
            
            # Initialize the counting semiring
            zero_extension_counting = CommutativeSemiring[self.semiring_extension.extension_counting.aggregation_op, self.semiring_extension.extension_counting.combination_op](
                self.semiring_extension.extension_counting.aggregation_op,
                self.semiring_extension.extension_counting.combination_op,
                self.semiring_extension.extension_counting.zero,
                self.semiring_extension.extension_counting.one,
                1
            )
            # Create the current extension
            current_extension = SelectiveSemiringExtension(best_base, zero_extension_counting, best_sample)
            # Update the best result
            best_result += current_extension

        # Sample a random set from the best result
        best_result.extension_sampling.value = self.random_set(best_result.extension_sampling.value)

        return best_result