user_input ="9 8 7 6 5 4 3 2 1 0"
numbers = list(map(int,user_input.split()))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # number of passes
        print("value of i :",i)
        for j in range(0,n-i-1):  # last i elements already sorted
            print("\n value of j :",j)
            if arr[j] > arr[j + 1]:  # wrong order

                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap

    return arr

print("Before:", numbers)
bubble_sort(numbers)
print("After:",numbers)
