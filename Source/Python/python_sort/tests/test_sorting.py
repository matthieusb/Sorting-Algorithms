# from sorting_algo import sorting
# flake8:noqa: e122

import operator

from sorting_algo import general_utilities
from sorting_algo import sorting


class TestBubbleSort(object):

    def test_simple_int_list(self):
        simpleMixedIntList = [4, 2, 3, 5, 1]

        sorting.bubble_sort(simpleMixedIntList, operator.le)

        print simpleMixedIntList

        assert general_utilities.is_list_sorted(
        simpleMixedIntList,operator.le)


class TestInsertionSort(object):
    pass
