# from sorting_algo import sorting

import operator

from sorting_algo import general_utilities
from sorting_algo import sorting
from sorting_algo import datasets


class TestBubbleSort(object):
    parameters = datasets.Parameters()
    data = datasets.SortingDataSets()

    # Tests with >= and <= on int lists
    def test_simple_int_list(self):
        sorting.bubble_sort(self.data.simpleMixedIntList1, operator.le)
        sorting.bubble_sort(self.data.simpleMixedIntList2, operator.ge)

        assert general_utilities.\
            is_list_sorted(self.data.simpleMixedIntList1, operator.le)
        assert general_utilities.\
            is_list_sorted(self.data.simpleMixedIntList2, operator.ge)

    def test_complex_generated_list_asc_desc(self):
        for length in range(1, self.parameters.lengthRangeMax):
            for minTest in range(self.parameters.minTestRange, 0):
                for maxTest in range(0, self.parameters.maxTestRange):
                    for currentOp in [operator.le, operator.ge]:
                        currentList = general_utilities.\
                            generate_random_int_list(length, minTest, maxTest)

                        sorting.bubble_sort(currentList, currentOp)
                        assert general_utilities.\
                            is_list_sorted(currentList, currentOp)


class TestInsertionSort(object):
    pass
