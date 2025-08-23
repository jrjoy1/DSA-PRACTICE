
a = int(input("Enter the first value : "))
b = int(input("Enter the second value : "))

sum1 = a + b
sum2 = a - b
sum3 = a * b
sum4 = a // b

if (a/b == 10):
    print("Congratulations..!")
    print(f"The value is: {sum4}")
else:
    print("This is not divisible by 10..!! \n The other results are below...")
    print(f" --> Addition = {sum1}\n --> Subtraction = {sum2}\n --> Multiplication = {sum3}\n --> Division = {sum4}")

