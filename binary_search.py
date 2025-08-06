def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Found, return index
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Not found

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 3
result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print("Target not found")
