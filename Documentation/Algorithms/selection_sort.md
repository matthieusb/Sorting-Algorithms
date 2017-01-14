# Selection sort explained
With selection sort, the list is divided into two parts :
  - Left part, which is sorted
  - Right part, which is not sorted

At the beginning, we have an empty sorted part, and the unsorted part is obviously the entire list.
At each iteration, you look for the minimum of the list and swap both elements.

The steps are the following :
  - Set minimum location to 0
  - Search for the minimum in the list
  - Swap with value at the minimum location
  - Increment minimum location (Pointing to the next element)
  - Repeat until the list is sorted

## Algorithm
```
-- FUNCTIONS
swap(array, index1, index2) Function to swap to array elements according to two indices

-- VARIABLES
array is an array of int (For this example)
arraySize is an int
i is an int

-- ALGORITHM
arraySize = length(array)

for i = 0 to arraySize - 1
  min = i

  # Check if the element is minimum of the whole list
  for j = i + 1 to arraySize
    if list[j] < list[min] then
      min = j
    end if
  end for

  if indexMin != i then
    swap(array, min, i)
  end if

end for



```

## Complexity
Two loops with a nested one means *O(n²)* complexity at worst. At best it is *O(n²)* too, so this is not adapted to large datasets.
