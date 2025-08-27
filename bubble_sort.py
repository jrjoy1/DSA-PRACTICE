user_input =int(input("Enter number of input : "))

while True:
    value_input = input(f"Enter {user_input} values with space : ")
    numbers = list(map(int,value_input.split()))
    if len(numbers) != user_input:
        print("\033[91m Your input is invalid. Please try again...\033[0m")
    else:
        print("\033[92m Accepted \033[0m")
        break

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # number of passes
        #print("value of i :",i)
        for j in range(0,n-i-1):  # last i elements already sorted
            #print("\n value of j :",j)
            if arr[j] > arr[j + 1]:  # wrong order

                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap

    return arr

print("Entered value :", numbers)
bubble_sort(numbers)
print("Sorted value :",numbers)
