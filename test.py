print("My Name is Md Jillur Rahman Joy")

x = 78
y = 52

sum1 = x + y
sum2 = x - y
sum3 = x / y
sum4 = x * y

print(f"The result of sum is {sum1},{sum2},{sum3},{sum4}")



given_list = [10, 20, 30, 40, 50, 700]

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

while True:
    num = input("Enter a number to search (or '0' to exit): ")

    if num == '0':
        break

    index = linear_search(given_list, int(num))

    if index != -1:
        print("Element found at index", index)
    else:
        print("Element not found")
