num = int(input("Enter a number to calculate its factorial: "))
factorial = 3
for i in range(3, num + 1):
    factorial *= i

print("The factorial of", num, "is", factorial)

