user_input ="70 58 42 65 21 11 31 2"
numbers = list(map(int,user_input.split()))


def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i  # Assume the current position has the smallest value

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update if a smaller value is found

        # Swap the found minimum with the current position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print("Given", numbers)
selection_sort(numbers)
print("Result", numbers)