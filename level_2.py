# =============================================
# Python Level 2: Building Stronger Foundations
# =============================================

# Welcome to Level 2!
# In this file, we'll dive deeper into Python and Data Analytics skills:
# - Functions
# - If/Else Logic
# - Loops
# - Error Handling
# - More pandas for data analysis
# - Visualization with matplotlib

# -------------------------------
# Functions: Reusable Blocks of Code
# -------------------------------

def greet_user(name):
    print(f"Hello, {name}! Welcome back!")

# Call the function
greet_user("Alex")

# Functions can also return values
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print("Sum:", result)

# -------------------------------
# If/Else: Making Decisions
# -------------------------------

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C or lower")

# -------------------------------
# Loops: Repeating Actions
# -------------------------------

# For Loop
colors = ["red", "blue", "green"]
for color in colors:
    print("Color:", color)

# While Loop
count = 0
while count < 3:
    print("Counting:", count)
    count += 1

# -------------------------------
# Error Handling: try/except
# -------------------------------

try:
    number = int(input("Enter a number: "))
    print("Your number squared is:", number ** 2)
except ValueError:
    print("That's not a valid number!")

# -------------------------------
# Pandas: Going Deeper
# -------------------------------

import pandas as pd

# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Score": [85, 92, 78, 88]
}

df = pd.DataFrame(data)

print(df)

# Sorting
print("\nSorted by Score:")
print(df.sort_values(by="Score", ascending=False))

# Filtering
high_scores = df[df["Score"] > 80]
print("\nStudents with Scores > 80:")
print(high_scores)

# Grouping (example with more data)
grouped_data = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Subject": ["Math", "Math", "Science", "Science", "Math"],
    "Score": [85, 92, 78, 88, 95]
})

print("\nGrouped by Subject:")
print(grouped_data.groupby("Subject")["Score"].mean())

# -------------------------------
# Matplotlib: Basic Visualization
# -------------------------------

import matplotlib.pyplot as plt

# Create a simple bar chart
names = df["Name"]
scores = df["Score"]

plt.bar(names, scores)
plt.title("Student Scores")
plt.xlabel("Student")
plt.ylabel("Score")
plt.show()

# -------------------------------
# Mini Project: Student Grade Tracker
# -------------------------------

# 1. Create a list of students and their scores
# 2. Calculate the average score
# 3. Print out who scored above average
# 4. Visualize the scores in a bar chart

# (Try building this yourself!)

# -------------------------------
# Challenge Exercises
# -------------------------------

# 1. Write a function that takes a list of numbers and returns their average.
# 2. Loop through a list of temperatures and print only those above 75 degrees.
# 3. Read a CSV file of your favorite sports team stats and plot a chart.

# You are now on your way to becoming a Python Analyst!
# Keep practicing and trying mini projects!
