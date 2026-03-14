# SUM OF TWO NUMBERS
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a + b
print("Sum =", sum)

# ODD OR EVEN
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Find Largest of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest number is", a)
else:
    print("Largest number is", b)

# Factorial of a Number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("Factorial =", fact)

# Reverse a String
text = input("Enter a string: ")
reverse = text[::-1]
print("Reversed string:", reverse)

# Check Palindrome
text = input("Enter a word: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Sum of Natural Numbers
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum =", sum)

# Simple Calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("1.Add 2.Subtract 3.Multiply 4.Divide")
choice = int(input("Enter choice: "))
if choice == 1:
    print("Result =", a + b)
elif choice == 2:
    print("Result =", a - b)
elif choice == 3:
    print("Result =", a * b)
elif choice == 4:
    print("Result =", a / b)
else:
    print("Invalid choice")
