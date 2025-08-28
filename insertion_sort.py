
user_input ="7 1 5 2"
numbers = list(map(int,user_input.split()))


def insertion_sort(arr):
    n = len(arr)
    print("n :",n)

    for i in range(1,n):
        print("i :",i)

        current = arr[i]
        print("current :",current)

        previous = i-1
        print("Previous :",previous)
        print("\n")

        while previous >= 0 and arr[previous] > current:
            print("Prev arr : ",arr[previous])

            arr[previous+1] = arr[previous]
            previous -= 1

        arr[previous+1]=current
        print("cng :",numbers)

print("before: ",numbers)
insertion_sort(numbers)
print("After :",numbers)