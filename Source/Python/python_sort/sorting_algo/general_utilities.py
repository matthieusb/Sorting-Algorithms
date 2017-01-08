# -*- coding: utf-8 -*-

import random


def swap_list_elements(listTo, idx1, idx2):
    """Swap two elements of a list. Returns a boolean to notify swap success or not

    :param listTo: The list to swap
    :type listTo: :class:`list`
    :param idx1: The index of the first element to swap
    :type idx1: :class:`int`
    :param idx2: The index of the second element to swap
    :type idx2: :class:`int`
    """

    if listTo and idx1 >= 0 and idx2 >= 0:
        length = len(listTo)
        if idx1 < length and idx2 < length:
            listTo[idx1], listTo[idx2] = listTo[idx2], listTo[idx1]
            return True
        else:
            return False
    else:
        return False


def is_list_sorted(listToCheck, operator):
    """Check if a list is sorted according to an operator.
    Returns False if the list is empty

    :param listToCheck: The list to check
    :type listToCheck: :class:`list`
    :param operator: The sorted order to check
    :type operator: :class:`operator`
    """
    if not listToCheck:
        return False
    else:
        lengthMinusOne = len(listToCheck) - 1
        isSorted = True
        i = 0

        # Exists loop as soon as isSorted is found false
        while (isSorted and i < lengthMinusOne):
            isSorted = operator(listToCheck[i], listToCheck[i + 1])
            i = i + 1

        return isSorted


def generate_random_int_list(size, min, max):
    """Generates an integer list that is random.
    Empty list if size is 0 (Independently of isSorted parameter)

    :param size: The size of the list to create
    :type size: :class:`int`
    :param min: Minimum integer to randomly generate (Included)
    :type min: :class:`int`
    :param max: Maximum integer to randomly generate (Included)
    :type max: :class:`int`
    """
    if size == 0 or min > max:
        return []
    else:
        return [random.randint(min, max) for i in xrange(size)]


def generate_random_int_list_sorted(size, min, max, operator):
    """Generates an integer list that is sorted
    Empty list if size is 0 (Independently of isSorted parameter)

    :param size: The size of the list to create
    :type size: :class:`int`
    :param min: Minimum integer to randomly generate (Included)
    :type min: :class:`int`
    :param max: Maximum integer to randomly generate (Included)
    :type max: :class:`int`
    :param operator: operator.ge for asc, operator.le for desc
    :type operator: :class:`operator`
    """
    if size == 0 or min > max:
        return []
    else:
        i = 1  # Because first tile is already affected
        resultList = [random.randint(min, max)]
        while i < size:
            randInt = random.randint(min, max)
            if operator(randInt, resultList[i - 1]):
                resultList.append(randInt)
                i = i + 1
        return resultList
