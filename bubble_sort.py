'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # number of passes

        for j in range(0,n-i-1):  # last i elements already sorted

            if arr[j] > arr[j + 1]:  # wrong order

                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap

    return arr

# Example
user_input ="9 8 7 6 5 4 3 2 1 0"
numbers = list(map(int,user_input.split()))
print("Before:", numbers)
bubble_sort(numbers)
print("After:",numbers)

'''


import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # number of passes
        print(f"\n🧪 Pass {i + 1}:")
        for j in range(0, n - i - 1):
            # Highlight current comparison
            print(f"🔍 Comparing arr[{j}] = {arr[j]} and arr[{j+1}] = {arr[j+1]}")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"  🔄 Swapped ➜ {arr}")
            else:
                print(f"  ✅ No swap needed")
            time.sleep(0.2)  # Optional delay for visualization
        print(f"📊 After Pass {i + 1}: {arr}")
        print("   " + " ".join(f"{x:2}" for x in arr))  # print visually aligned list
        time.sleep(0.4)
    return arr

# Example
user_input = "9 8 7 6 5 4 3 2 1 0"
numbers = list(map(int, user_input.split()))
print("📥 Before Sorting:", numbers)
bubble_sort(numbers)
print("\n✅ After Sorting:", numbers)

