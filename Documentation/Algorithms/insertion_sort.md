# Insertion sort explained

Insertion sort follows this process :
  - First element of the list means it's sorted, so you return the list
  - Go to the next element
  - Compare with all elements in sorted sublist
  - Put the current element at the good place in the sublist
  - As usual, repeat until the list is sorted

## Algorithm
```
-- VARIABLES
array is an array of int (For this example)
arraySize is an int
i is an int
indexToInsert is an int
valueToInsert is an int

-- ALGORITHM
arraySize = length(array)

for i = 0 to arraySize
  valueToInsert = array[i]
  indexToInsert = i

  while indexToInsert > 0 and array[indexToInsert - 1] > valueToInsert
    array[indexToInsert] = array[indexToInsert - 1]
    indexToInsert--
  end while

  array[indexToInsert] = valueToInsert

end for




```

## Complexity
Two loops with a nested one means *O(n²)* complexity at worst. At best it is *O(n)* with an already sorted array, as it only has to go through it once.
