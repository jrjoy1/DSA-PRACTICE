# Linear search algorithm e first e akta function niye for loop dite hbe array length er jonno ,
#if condition e dekhbo target value array index e ase ki na,
#then output showing by condition.....

given_list = [10, 20, 30, 40, 50, 700]
target = int(input("Enter the number : "))

joy = len(given_list)

def linear_search(given_list,target):       #create a function with list & targrt
    for i in range(joy):    #Getting the index of list
        if(given_list[i]==target):      #Checking the list element through index with target element
            return i                    #If its equal then return the index number
    return -1                               #Neither -1

result = linear_search(given_list, target)  #Storing the function result in a variable


if(result != -1):                           #Condition for printing output
    print(f"The element is fount at index : {result}")
else:
    print("The element not found.")

