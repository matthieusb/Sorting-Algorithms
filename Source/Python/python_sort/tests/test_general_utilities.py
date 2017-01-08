# -*- coding: utf-8 -*-
# flake8:noqa: e122


import operator
import pytest

from sorting_algo import general_utilities


class TestIsSorted(object):
    emptyList = []

    simpleSortedAscIntList = [1, 2, 3, 4]
    simpleMixedIntList = [4, 2, 3, 5, 1]

    simpleSortedAscStringList = ["a", "ab", "abc", "b", "c",]
    simpleMixedStringList = ["kayak", "zoulou", "test", "a", "mix"]

    def test_is_list_sorted_empty(self):
        assert not general_utilities.is_list_sorted(
        self.emptyList, operator.le)

    def test_is_list_sorted_simple(self):
        assert general_utilities.is_list_sorted(
        self.simpleSortedAscIntList, operator.le)

        # Same test with a reversed version of the list
        assert general_utilities.is_list_sorted(
        self.simpleSortedAscIntList[::-1], operator.ge)

        assert not general_utilities.is_list_sorted(
        self.simpleMixedIntList, operator.le)

    def test_is_list_sorted_strings(self):
        assert general_utilities.is_list_sorted(
        self.simpleSortedAscStringList, operator.le
        )

        assert not general_utilities.is_list_sorted(
        self.simpleMixedStringList, operator.le
        )

class TestGenerateRandomList(object):
    lengthRangeMax = 10
    minTestRange = -15
    maxTestRange = 15

    def test_is_empty_generated(self):
        assert not general_utilities.generate_random_int_list(0, 0, 0)
        assert not general_utilities.generate_random_int_list_sorted(0, 0, 0, operator.ge)

    # Tests if good length and elements between min and max
    def test_is_correctly_generated(self):
        for length in range(1, self.lengthRangeMax):
            for minTest in range(self.minTestRange, 0):
                for maxTest in range(0, self.maxTestRange):
                    resultList = general_utilities.generate_random_int_list(length, minTest, maxTest)

                    assert len(resultList) == length
                    assert all(minTest<=x<=maxTest for x in resultList)

    # Same than before + checks if sorted
    def test_is_correctly_generated_sorted(self):
        for length in range(1, self.lengthRangeMax):
            for minTest in range(self.minTestRange, 0):
                for maxTest in range(0, self.maxTestRange):
                    resultList = general_utilities.generate_random_int_list_sorted(length, minTest, maxTest, operator.ge)

                    assert len(resultList) == length
                    assert all(minTest<=x<=maxTest for x in resultList)
                    assert general_utilities.is_list_sorted(resultList, operator.le)


class TestSwapElements(object):
    listToSwap = [1, 2, 3, 4]

    def test_is_correctly_swapped(self):
        assert general_utilities.swap_list_elements(self.listToSwap, 0, 1)
        assert self.listToSwap[0] == 2 and self.listToSwap[1] == 1

    # Test all cases where function might be called incorrectly
    def test_incorrect_swap_params(self):
        assert not general_utilities.swap_list_elements([], 0, 1)

        assert not general_utilities.swap_list_elements(self.listToSwap, -1, 10)

        assert not general_utilities.swap_list_elements(self.listToSwap, 1, 10)
