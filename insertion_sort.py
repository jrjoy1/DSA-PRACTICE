
user_input ="70 58 42 65 21 11 31 2"
numbers = list(map(int,user_input.split()))


def selection_sort(arr):
    n = len(arr)
    for i in range(1,n):
        current = arr[i]
        previous = i-1

        while previous >= 0 and arr[previous] > current:
            arr[previous+1] = arr[previous]
            previous -= 1

        arr[previous+1]=current

print("before: ",numbers)
selection_sort(numbers)
print("After :",numbers)