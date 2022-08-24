# Blog Notes: Merge Sort

## How does Merge Sort work?
Merge Sort works by dividing and conquering. What I mean by this is the problem is broken down
into multiple sub problems until they become easy to solve. At this point the sub problems are
then combined or merged together to solve the original problem.

## Merge Sort Breakdown:
1. Split the array in half
2. Call Merge Sort on each half to sort them
3. Merge both sorted halves into one sorted array.

Below I present a visual representation of a merge sort through an example array.
What's happening is the array was split in half. Then the next step is to break those halved
arrays into smaller arrays until there is only one number in each array. Then we begin to merge
the numbers back together sorting each side until ultimately we merge the entire array back together.

![Example_Array](/example_array.png)
