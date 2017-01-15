# Quick sort explained
Quick sort partitions the array into smaller arrays.
We take the array, divide it by two smaller arrays and sort them using a pivot value. This algorithms is called recursively on both arrays.

For the pivot, steps are the following :
  1. Choose highest index value as pivot
  2. Take two variables left and right of the list without pivot
  3. Left has to point to the low index
  4. Right has to point to the high index
  5. While value at left is less than pivot, move right
  6. While value at right is greater than pivot move left
  7. Both 5 and 6 do not match, swap left and right
  8. Left > right => the point where they meet is the new pivot


Global quick sort instructions are the following :
  - Take the right array last value as pivot
  - Partition this array using the pivot value
  - Quick sort left array recursively
  - Quick sort right array recursively


## Algorithm

### Pivot
```
-- FUNCTIONS
swap(array, index1, index2) Function to swap to array elements according to two indices

-- VARIABLES
array is an array of int (For this example)
arraySize is an int


-- ALGORITHM
function partitionArray(array, left, right, pivot)
  leftPointer = left - 1
  rightPointer = right

  while True do
    while array[++leftPointer] < pivot
      # Nothing
    end while


    while rightPointer > 0 and array[--rightPointer] > pivot
      # Nothing
    end while

    if leftPointer >= rightPointer
      break
    else
      swap (array, leftPointer, rightPointer)
    end if
  end while

  swap (array, leftPointer, right)
  return leftPointer
end function
```

### Quick sort
```
-- VARIABLES
array is an array of int (For this example)
arraySize is an int


-- ALGORITHM
procedure quickSort(array, left, right)
  if right - left <= 0
    return
  else
    pivot = array[right]
    partition = partitionFunc(array, left, right, pivot)
    quickSort(array, left, parition - 1)
    quickSort(array, parition + 1, right)
  end if



```

## Complexity
Quick sort is highly efficient for large-sized data sets. Average and worst time complexity are *O(n log n)*.
