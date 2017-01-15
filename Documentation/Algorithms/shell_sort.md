# Shell sort explained
Shells rots relies on insertion sort but avoids large shifts if the smaller value is too far to the right of the array.
It uses an interval calculated with Knuth's formula to know which indices to compare elements.
The steps are the following :
  - Initialize knuth's *interval* value
  - Divide the list into smaller sublists using *interval* value
  - Sort these sublists with **insertion sort**
  - Repeat until the list is sorted


*Knuth's formula :*  ```interval = interval * 3 + 1``` where int is an interval with initial value 1

## Algorithm
```
-- VARIABLES
array is an array of int (For this example)
arraySize is an int
inner, outer is an int
interval is an int
valueToInsert is an int

-- ALGORITHM
interval = 1
arraySize = length(array)

# First, initialize the interval
while interval < arraySize / 3
  interval = interval * 3 + 1
end while

while interval > 0
  for outer = interval to arraySize
    valueToInsert = array[outer]
    inner = outer

    while inner > interval - 1 and array[inner - interval] >= valueToInsert
      array[inner] = array[inner - interval]
      inner = inner - interval
    end while

    array[inner] = valueToInsert
  end for

  interval = (interval - 1) / 3
end while
```

## Complexity
Shell sort time complexity is at the worst and best cases *O(n)*. It is said to be quite efficient for medium-sized data sets.

Some sources say it can also be *O(n²)* and that determining its complexity is still an open problem.
We'll compare algorithm performance to see which one is the best.
