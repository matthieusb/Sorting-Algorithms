# -*- coding: utf-8 -*-

import general_utilities


def bubble_sort(listToSort, operator):
    """Sorts the given list using bubble algorithm and given operator

    :param listToSort: The list to check
    :type listToSort: :class:`list`
    :param operator: operator.le for asc, operator.ge for desc
    :type operator: :class:`operator`
    """
    lengthMinusOne = len(listToSort) - 1

    swappedFlag = True
    i = 0
    while i < lengthMinusOne and swappedFlag:
        swappedFlag = False
        j = 0
        while j < lengthMinusOne:
            if operator(listToSort[j + 1], listToSort[j]):
                general_utilities.swap_list_elements(listToSort, j, j + 1)
                swappedFlag = True
            j = j + 1
        i = i + 1


def insertion_sort(list, operator):
    pass
