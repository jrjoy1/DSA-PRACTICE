
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):  # number of passes
        for j in range(n-1-i):  # last i elements already sorted
            if arr[j] > arr[j + 1]:  # wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
    return arr

# Example
user_input =input("Enter numbers with space : ")
numbers = list(map(int,user_input.split()))
print("Before:", numbers)
bubble_sort(numbers)
print("After:", numbers)


