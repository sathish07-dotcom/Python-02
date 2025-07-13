# 🐍 Python Conditional Statements

Welcome to the repository on **Conditional Statements in Python**! This repo is a beginner-friendly guide to understanding how decisions are made in Python using conditional logic.



## 📌 What Are Conditional Statements?

Conditional statements are used to perform different actions based on different conditions. They help control the flow of a program by executing code only when certain conditions are met.


## 🔁 Types of Conditional Statements

### 1. `if` Statement
Executes a block of code **only if** the condition is true.
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

---

### 2. `if-else` Statement  
Provides an **alternative block** of code if the condition is false.
```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

---

### 3. `if-elif-else` Statement  
Allows you to check **multiple conditions**.
```python
x = 7
if x < 5:
    print("x is less than 5")
elif x == 7:
    print("x is 7")
else:
    print("x is greater than 5 and not 7")
```

---

### 4. Nested `if` Statements  
You can place one `if` statement **inside another**.
```python
x = 10
if x > 5:
    if x < 15:
        print("x is between 5 and 15")
```

---

### 5. Short Hand `if`  
Used when you want to write a simple `if` in one line.
```python
x = 10
if x > 5: print("x is greater than 5")
```

---

### 6. Short Hand `if-else` (Ternary Operator)
Used to write `if-else` in one line.
```python
x = 5
print("Even") if x % 2 == 0 else print("Odd")
```

---

## 🧠 Real-Life Example
```python
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

---

## ✅ Summary

| Statement Type      | Purpose                                  |
|---------------------|-------------------------------------------|
| `if`                | Executes block if condition is True       |
| `if-else`           | Adds an alternate block if condition is False |
| `if-elif-else`      | Handles multiple conditions               |
| Nested `if`         | Checks condition inside another condition |
| Short Hand `if`     | Compact single-line `if`                  |
| Ternary Operator    | Compact single-line `if-else`             |

---

## 📂 Folder Structure
```
├── examples/
│   ├── if_statement.py
│   ├── if_else.py
│   ├── if_elif_else.py
│   ├── nested_if.py
│   └── shorthand.py
└── README.md
```

---

## 💡 Tips
- Always use proper indentation (Python uses whitespace for blocks).
- Use `elif` for clean multiple condition checks.
- Avoid too many nested `if` statements — they reduce code readability.

---

## 🔗 Resources
- [Python Docs - Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [W3Schools - Python Conditions](https://www.w3schools.com/python/python_conditions.asp)

---

Feel free to fork, star ⭐, and contribute to this repository. Happy Coding! 🧑‍💻
