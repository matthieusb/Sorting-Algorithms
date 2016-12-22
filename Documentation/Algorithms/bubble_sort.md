# Bubble sort explained
Bubble sort is one of the simplest algorithms


## Algorithm
One of the simplest sorting algorithms

```
-- FUNCTIONS
swap(array, index1, index2) Function to swap to array elements according to two indices

-- VARIABLES
array is an array of int (For this example)
arraySize is an int
i is an int

-- ALGORITHM
arraySize = length(array)

# We iterate to size-1 to avoid overlapping
for i = 0 to arraySize - 1
  if array[i] > array[i + 1] then
    swap(array, i, i + 1)
```



## Complexity
The bubble sort algorithm is *O(n)*
