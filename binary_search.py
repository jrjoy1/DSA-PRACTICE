
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = int(input("Enter number from (1-15) to find : "))


def binary_search(arr, target):
    low = 0
    high = len(arr) -1

    while(low <= high):             #its a condition for valid range, if low is greater than high then the range excedded
        mid = (low + high) // 2     #its the method of divide the data in two parts
        if(arr[mid] == target):     #if mid equals to target then we got the value
            return mid              #return the value
        elif(arr[mid] < target):    #if mid is less than target then 
            low = mid + 1           #go to the left side for search
        else:
            high = mid - 1          #if mid is greater than target then go to the right side for search
    return -1
    
result = binary_search(arr, target)

if(result != -1):
    print(f"{target} found in index {result}")
else:
    print("Not found")
