# from sorting_algo import sorting

import operator

from sorting_algo import general_utilities
from sorting_algo import sorting
from sorting_algo import datasets


class TestEmptyListSort(object):
    data = datasets.SortingDataSets()

    def test_bubbleSort_emptyList(self):
        assert not general_utilities.\
            is_list_sorted(sorting.bubble_sort(
                self.data.emptyList, operator.le
                ), operator.le)

    def test_insertionSort_emptyList(self):
        assert not general_utilities.\
            is_list_sorted(sorting.insertion_sort(
                    self.data.emptyList, operator.le
                    ), operator.le)


class TestBubbleSort(object):
    parameters = datasets.Parameters()
    data = datasets.SortingDataSets()

    # Tests with >= and <= on int lists
    def test_bubbleSort_simple_int_list(self):
        assert general_utilities.\
            is_list_sorted(sorting.bubble_sort(
                self.data.simpleMixedIntList1, operator.le
                ), operator.le)

        assert general_utilities.\
            is_list_sorted(sorting.bubble_sort(
                self.data.simpleMixedIntList2, operator.ge
                ), operator.ge)

    def test_bubbleSort_complex_generated_list_asc_desc(self):
        for length in range(1, self.parameters.lengthRangeMax):
            for minTest in range(self.parameters.minTestRange, 0):
                for maxTest in range(0, self.parameters.maxTestRange):
                    for currentOp in [operator.le, operator.ge]:
                        currentList = general_utilities.\
                            generate_random_int_list(length, minTest, maxTest)
                        # Test for each length/minTest/maxTest/currentOp
                        assert general_utilities.\
                            is_list_sorted(sorting.bubble_sort(
                                currentList, currentOp
                                ), currentOp)


class TestInsertionSort(object):
    parameters = datasets.Parameters()
    data = datasets.SortingDataSets()

    def test_insertionSort_simple_int_list(self):
        assert general_utilities.\
            is_list_sorted(sorting.insertion_sort(
                self.data.simpleMixedIntList1, operator.le
                ), operator.le)

        assert general_utilities.\
            is_list_sorted(sorting.insertion_sort(
                self.data.simpleMixedIntList2, operator.ge
                ), operator.ge)

    def test_insertionSort_complex_generated_list_asc_desc(self):
        for length in range(1, self.parameters.lengthRangeMax):
            for minTest in range(self.parameters.minTestRange, 0):
                for maxTest in range(0, self.parameters.maxTestRange):
                    for currentOp in [operator.le, operator.ge]:
                        currentList = general_utilities.\
                            generate_random_int_list(length, minTest, maxTest)
                        # Test for each length/minTest/maxTest/currentOp
                        assert general_utilities.\
                            is_list_sorted(sorting.insertion_sort(
                                currentList, currentOp
                                ), currentOp)
