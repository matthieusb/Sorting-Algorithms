# Merge sort explained
Merge sort divides the array into equal halves and combines them in a sorted manner.
It sorts the list recursively until everything is atomic, sorts every atomic part and returns a complete merged list.

The steps are the following :
  - If the list is only one element long, it is sorted, return it
  - Divide the list recursively into two helves until it cannot be divided
  - Merge the smaller lists into new lists in sorted order


## Algorithm
```

-- FUNCTIONS
removeFromArray(array, indexToRemove) : removes the indicated index element from an array
appendToArray(array, element) : adds an element to the end of an array
arrayIsEmpty(array) : returns a boolean telling wether the array is empty or not

-- ALGORITHM
procedure mergeSort(array is an array)
  arraySize = length(array)

  if arraySize = 1
    return array
  else
    arrayFirstHalf = array[0] to array[arraySize/2]
    arraySecondHalf = array[arraySize/2 + 1] to array[arraySize-1]

    arrayFirstHalf = mergeSort(arrayFirstHalf)
    arraySecondHalf = mergeSort(arraySecondHalf)
  end if

  return merge(arrayFirstHalf, arraySecondHalf)
end procedure


procedure merge(array1 is an array, array2 is an array)
  arrayRes is an array

  while (not arrayIsEmpty(array1) and not arrayIsEmpty(array2))
    if array1[0] > array2[0]
      appendToArray(arrayRes, array2[O])
      removeFromArray(array2, 0)
    else
      appendToArray(arrayRes, array1[O])      
      removeFromArray(array1, 0)
    end if
  end while

  while (not arrayIsEmpty(array1))
    appendToArray(arrayRes, array1[O])      
    removeFromArray(array1, 0)
  end while

  while (not arrayIsEmpty(array2))
    appendToArray(arrayRes, array2[O])
    removeFromArray(array2, 0)
  end while

  return arrayRes
end procedure
```

## Complexity
In the worst case, merge sort is O(n log n).
