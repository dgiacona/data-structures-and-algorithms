# Blog Notes: Quick Sort
### By Dominic GIacona

## How to sort through an an array with Quick Sort.
This sorting method uses the divide and conquer approach as well. Below we will break down the steps of executing a quick sort.

1. First the array in question is divided into sub arrays by selecting a pivot element. While we divide the array the pivot element should be positioned in a way that element in the array that are less than the pivot stay on the left side and those elements in the array that are larger in value are placed on the right side.
2. Next we use this same approach when dividing the sub arrays and the process will continue until each subarray contains a single element.
3. Lastly, at this point the elements will be sorted and they are combined to for a sorted array.

## Pseudo Code

```python
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```
