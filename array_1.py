'''
# Using For Loop
j = []

o = int(input("Enter the number of element : "))

for i in range(o):
    element = int(input(f"Enter the number {i+1} : "))
    j.append(element)

print("The Array is = ",j)

'''
import time
import sys

start = time.time()

# Using while loop 
j = []

n = int(input("Enter the num of elements :"))

i = 0

while(i < n):
    y = int(input(f"Enter the num {i+1} :"))
    j.append(y)
    i += 1
end = time.time()
mem = sys.getsizeof(y)
 #mem = sys.getsizeof(int)

print("The Array is : ", j)

print(f"The memory used is :{mem} bytes")
print(f"time taken is :{end - start:.6f}second")