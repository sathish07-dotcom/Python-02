
#### 1. **Check Even or Odd**  

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#### 2. **Positive, Negative, or Zero**  

num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


#### 3. **Largest of Two Numbers**  

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)


#### 4. **Largest of Three Numbers**  

a, b, c = map(int, input("Enter three numbers: ").split())
if a > b and a > c:
    print("Largest:", a)
elif b > c:
    print("Largest:", b)
else:
    print("Largest:", c)


#### 5. **Leap Year Checker**  

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


#### 6. **Divisibility Test (by 5 and 11)**  

num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")

#### 7. **Vowel or Consonant**  

char = input("Enter a character: ").lower()
if char in 'aeiou':
    print("Vowel")
elif char.isalpha():
    print("Consonant")
else:
    print("Invalid input")


#### 8. **Grade Calculation**  

marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")


#### 9. **Triangle Validity**  

a, b, c = map(int, input("Enter three angles: ").split())
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("Valid Triangle")
else:
    print("Invalid Triangle")


#### 10. **Check for Alphabet, Digit, or Special Character**  

char = input("Enter a character: ")
if char.isalpha():
    print("Alphabet")
elif char.isdigit():
    print("Digit")
else:
    print("Special Character")


#### 11. **Odd or Even Without Using % Operator**  

num = int(input("Enter a number: "))
if num & 1 == 0:
    print("Even")
else:
    print("Odd")


#### 12. **Electricity Bill Calculation**  

units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2
else:
    bill = 100 * 1.5 + 100 * 2 + (units - 200) * 3
print("Electricity Bill:", bill)


#### 13. **Simple Calculator**  

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/' and b != 0:
    print("Result:", a / b)
else:
    print("Invalid operation")


#### 14. **Check Palindrome Number**  

num = input("Enter a number: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


#### 15. **Check Armstrong Number**  

num = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) ** len(str(num)) for digit in str(num))
if num == sum_of_digits:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")




### **Real-World Scenarios**
#### 16. **ATM Withdrawal**  

balance = 5000
amount = int(input("Enter withdrawal amount: "))
if amount <= balance and amount % 100 == 0:
    balance -= amount
    print("Withdrawal Successful! Remaining Balance:", balance)
else:
    print("Invalid Transaction")

#### 17. **Toll Tax Calculation**  

vehicle = input("Enter vehicle type (car/bike/truck): ").lower()
if vehicle == "car":
    print("Toll: ₹50")
elif vehicle == "bike":
    print("Toll: ₹20")
elif vehicle == "truck":
    print("Toll: ₹100")
else:
    print("Invalid vehicle type")

#### 18. **Username & Password Validation**  

correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Credentials")

#### 19. **Discount Calculator**  

amount = float(input("Enter total purchase amount: "))
if amount > 5000:
    discount = amount * 0.2
elif amount > 3000:
    discount = amount * 0.15
elif amount > 1000:
    discount = amount * 0.1
else:
    discount = 0
print("Final Amount after Discount:", amount - discount)


#### 20. **Bus Ticket Fare Calculation**  

age = int(input("Enter age: "))
distance = int(input("Enter distance (km): "))

if age < 12:
    fare = distance * 2
elif age >= 60:
    fare = distance * 3
else:
    fare = distance * 5

print("Total Fare: ₹", fare)
