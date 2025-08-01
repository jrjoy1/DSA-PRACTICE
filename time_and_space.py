import time
import sys

start = time.time()

n = int(input("Enter a number: "))
#print(f"The square of {n} is {n*n}")

square = n * n
value = square

print("The square value is", value)

end = time.time()
mem = sys.getsizeof(value)

print(f"Memory used by result: {mem} bytes")
print(f"Time taken: {end - start:.6f} seconds")