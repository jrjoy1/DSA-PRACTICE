def quicksort(arr):
    if len(arr) <= 1:  #if the element is only 1 or 0 then it is already sorted
        return arr  #then sorting finished from here
    
    pivot = arr[0]  # take 1st element as pivot
    left = []   #elements smaller than pivot
    right = []  #elements larger than pivot
    
    print(f"\nPivot: {pivot}")

    for i in arr[1:]:   #loop for other element of list (excluding pivot)
        if i < pivot:   #if element is smaller than pivot
            left.append(i)  #it goes to left
        else:
            right.append(i) #if its large then goes to right 
    print(f"Left: {left}")
    print(f"Right: {right}")
    #combine all the sorted part recursively with the pivot in middle
    return quicksort(left) + [pivot] + quicksort(right)

numbers = [7, 1, 5, 2]
print("Original:", numbers)
sorted_numbers = quicksort(numbers)
print("\nFinal Sorted:", sorted_numbers)
