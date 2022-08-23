# Blog Notes: Insertion Sort
### By Dominic Giacona


## How does Insertion Sorting work in python?
When using insertion sorting for an aray there is a flow and process that follows. We can first assume that
the first element in the array to be sorted. By us assuming that the fiest element is sorted our focus shifts
to the second element in the array.
<br>
This is the start of the process and comparing the elements looking for what element has the greater value. We
can name the element in focus as the key element. As we have our sights on the key element we have to make a
decision on where it is placed based on if it is greater than the first element or not. If the key is greater
than the first element it is placed after the first element if it is less than the first element then it is placed
in front of the first element.
<br>
This process continues until the array has been sorted.



```

# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key


#sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
lst = [] #empty list to store sorted elements
print("Sorted array is : ")
for i range(len(arr)):
  lst.append(arr[i])       #appending the elements in sorted order
print(lst)

```
## Output
```
Sorted array is:
[5, 6, 11, 12, 13]

```
