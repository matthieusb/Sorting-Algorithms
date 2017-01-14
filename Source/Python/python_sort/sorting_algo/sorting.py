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
        listToReturn = list(listToSort)  # copying the input list
        lengthMinusOne = len(listToReturn) - 1

        swappedFlag = True
        i = 0
        while i < lengthMinusOne and swappedFlag:
            swappedFlag = False
            j = 0
            while j < lengthMinusOne:
                if operator(listToReturn[j + 1], listToReturn[j]):
                    general_utilities.\
                        swap_list_elements(listToReturn, j, j + 1)
                    swappedFlag = True
                j = j + 1
            i = i + 1

        return listToReturn
    else:
        return []


def insertion_sort(listToSort, operator):
    """Sorts the given list using insertion algorithm and given operator.
    Returns a list

    :param listToSort: The list to check
    :type listToSort: :class:`list`
    :param operator: operator.le for asc, operator.ge for desc
    :type operator: :class:`operator`
    """

    if listToSort:
        listToReturn = list(listToSort)
        listLength = len(listToReturn)
        for i in range(0, listLength):
            valueToInsert = listToReturn[i]
            indexToInsert = i

            while (
                indexToInsert > 0 and
                operator(valueToInsert, listToReturn[indexToInsert - 1])
            ):
                listToReturn[indexToInsert] = \
                    listToReturn[indexToInsert - 1]
                indexToInsert = indexToInsert - 1

            listToReturn[indexToInsert] = valueToInsert

        return listToReturn
    else:
        return []


def selection_sort(listToSort, operator):
    """Sorts the given list using selection algorithm and given operator.
    Returns a list

    :param listToSort: The list to check
    :type listToSort: :class:`list`
    :param operator: operator.le for asc, operator.ge for desc
    :type operator: :class:`operator`
    """
    if listToSort:
        listToReturn = list(listToSort)
        listLength = len(listToReturn)
        listLengthMinusOne = listLength - 1

        for i in range(0, listLengthMinusOne):
            minIndex = i

            # Checking if the element is minimum of the whole list
            for j in range(i + 1, listLength):
                if operator(listToReturn[j], listToReturn[minIndex]):
                    minIndex = j

            if minIndex != i:
                general_utilities.swap_list_elements(
                    listToReturn, minIndex, i)

        return listToReturn
    else:
        return[]


def merge_sort(listToSort, operator):
    if listToSort:
        return merge_do_algo(listToSort, operator)
    else:
        return[]


def merge_do_algo(listToSort, operator):
    listSize = len(listToSort)

    if listSize == 1:
        return listToSort
    else:
        listFirstHalf = listToSort[:listSize/2]
        listSecondHalf = listToSort[listSize/2:]

        listFirstHalf = merge_do_algo(listFirstHalf, operator)
        listSecondHalf = merge_do_algo(listSecondHalf, operator)

    return merge_list_halves(listFirstHalf, listSecondHalf, operator)


def merge_list_halves(listOne, listTwo, operator):
    listResult = []

    while (listOne and listTwo):
        if operator(listTwo[0], listOne[0]):
            listResult.append(listTwo[0])
            listTwo.pop(0)
        else:
            listResult.append(listOne[0])
            listOne.pop(0)

    while listOne:
        listResult.append(listOne.pop(0))

    while listTwo:
        listResult.append(listTwo.pop(0))

    return listResult


def shell_sort(listToSort, operator):
    return[]


def quick_sort(listToSort, operator):
    return[]
