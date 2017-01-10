# Bubble sort explained
Bubble sort is one of the simplest sorting algorithms.
You just iterate through each array tile and determine wether the current element is inferior/superior to the following, and you swap them according to the order you want, until the list is sorted

## Algorithm
__Naive version of the algorithm :__
```
-- FUNCTIONS
swap(array, index1, index2) Function to swap to array elements according to two indices
isSorted(array) : checks if array is already sorted

-- VARIABLES
array is an array of int (For this example)
arraySize is an int
i is an int

-- ALGORITHM
arraySize = length(array)


while not (isSorted(array))
  # We iterate to size-1 to avoid overlapping
  for i = 0 to arraySize - 1
    if array[i] > array[i + 1] then
      swap(array, i, i + 1)
    end if
  end for
end while
```

**IMPORTANT** :
There is another way to check if everything is sorted : add a *swap* flag as a boolean. If nothing was swapped while ou go through the list, it's ok to stop.

__Better version of the algorithm :__

```
-- FUNCTIONS
swap(array, index1, index2) Function to swap to array elements according to two indices
exit_application() Quit the program

-- VARIABLES
array is an array of int (For this example)
arraySize is an int
i is an int
swapped_flag is a boolean

-- ALGORITHM
for i = 0 to arraySize - 1
  swapped_flag = false
  for j = 0 to arraySize - 1

    if array[j] < array[j + 1] then
      swap(array, j, j + 1)
      swapped = true # Not a tautology, we want it to keep its true value until the end of the current loop
    end if
  end for

  if not(swapped) then
    exit_application()
  end if
end for

```

## Complexity
The bubble sort algorithm is *O(n²)* (where n is the array length, as usual) since it has to go through the table with two loops.
At best, complexity is *o(n)*
