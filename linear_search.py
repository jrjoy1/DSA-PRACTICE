# Linear search algorithm e first e akta function niye for loop dite hbe array length er jonno ,
#if condition e dekhbo target value array index e ase ki na,
#then output showing by condition.....

given_list = [10, 20, 30, 40, 50, 700]

def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1 
 
while True:
    find_value = input("Enter a number to search (or '0' to exit): ")

    if find_value == '0':
        break

    result = linear_search(given_list, int(find_value))

    if result != -1:
        print("the exact element found at index", result)
    else:
        print("Element not found")
