# -*- coding: utf-8 -*-

import general_utilities


def bubble_sort(listToSort, operator):
    """Sorts the given list using bubble algorithm and given operator.
    Returns a list

    :param listToSort: The list to check
    :type listToSort: :class:`list`
    :param operator: operator.le for asc, operator.ge for desc
    :type operator: :class:`operator`
    """
    if listToSort:
        listToReturnSorted = list(listToSort)  # copying the input list
        lengthMinusOne = len(listToReturnSorted) - 1

        swappedFlag = True
        i = 0
        while i < lengthMinusOne and swappedFlag:
            swappedFlag = False
            j = 0
            while j < lengthMinusOne:
                if operator(listToReturnSorted[j + 1], listToReturnSorted[j]):
                    general_utilities.\
                        swap_list_elements(listToReturnSorted, j, j + 1)
                    swappedFlag = True
                j = j + 1
            i = i + 1

        return listToReturnSorted
    else:
        return []


def insertion_sort(listToSort, operator):
    """Sorts the given list using insertions algorithm and given operator.
    Returns a list

    :param listToSort: The list to check
    :type listToSort: :class:`list`
    :param operator: operator.le for asc, operator.ge for desc
    :type operator: :class:`operator`
    """

    if listToSort:
        listToReturnSorted = list(listToSort)
        listLength = len(listToReturnSorted)
        for i in range(0, listLength):
            valueToInsert = listToReturnSorted[i]
            indexToInsert = i

            while (
                indexToInsert > 0 and
                operator(valueToInsert, listToReturnSorted[indexToInsert - 1])
            ):
                listToReturnSorted[indexToInsert] = \
                    listToReturnSorted[indexToInsert - 1]
                indexToInsert = indexToInsert - 1

            listToReturnSorted[indexToInsert] = valueToInsert

        return listToReturnSorted
    else:
        return []
