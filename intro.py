# =============================================
# Python Beginner Guide + Data Analytics Intro
# =============================================

# Welcome! This file is designed to teach you:
# - What Python is
# - How Python works
# - Basic Python Syntax
# - Your first small Data Analytics project
# - Some practice exercises

# -------------------------------
# What is Python?
# -------------------------------
# Python is a high-level, easy-to-read programming language.
# It is used for web development, automation, data analytics,
# artificial intelligence, and more.

# Why Python?
# - Simple and clean syntax (easy to learn!)
# - Huge community support
# - Tons of libraries (tools) to make life easier

# -------------------------------
# How Python Works
# -------------------------------
# Python reads your code line-by-line and executes it.
# You write code in a file (like this one), and Python runs it.
# If there are mistakes (called "errors"), it will stop and show you where.

# You can run Python files by typing:
#    python filename.py
# in your terminal/command line.

# Let's start simple:

# This is a comment. Python ignores anything after a # symbol.
print("Hello, world!")  # This will print text to the screen

# Variables store information
name = "Alex"
age = 20
is_student = True

print(name)
print(age)
print(is_student)

# -------------------------------
# Basic Data Types
# -------------------------------
# Text  -> str (string)
# Number -> int (integer), float (decimal)
# True/False -> bool (boolean)

# Example:
height = 5.9   # float
graduated = False  # bool

# -------------------------------
# Collections (Lists and Dictionaries)
# -------------------------------
# List = ordered collection of items
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Access second item (banana)

# Dictionary = key-value pairs
person = {
    "name": "Alex",
    "age": 20,
    "student": True
}
print(person["name"])  # Access value for key 'name'

# -------------------------------
# Small Data Analytics Project
# -------------------------------

# Imagine you are given the following data about sales:

sales_data = [
    {"month": "January", "sales": 3050},
    {"month": "February", "sales": 3560},
    {"month": "March", "sales": 4100},
]

# Let's calculate total sales and average sales

total_sales = 0
for record in sales_data:
    total_sales += record["sales"]

average_sales = total_sales / len(sales_data)

print("Total Sales:", total_sales)
print("Average Monthly Sales:", average_sales)

# -------------------------------
# Introduction to Libraries
# -------------------------------

# Python has libraries that make tasks easier.
# Example: pandas is a library for working with tables of data.

# Let's use pandas to analyze data:

import pandas as pd

# Create a simple table (DataFrame)
data = {
    "Month": ["January", "February", "March"],
    "Sales": [3050, 3560, 4100]
}

sales_df = pd.DataFrame(data)

print(sales_df)

# Calculate total and average sales with pandas
print("Total Sales:", sales_df["Sales"].sum())
print("Average Sales:", sales_df["Sales"].mean())

# -------------------------------
# Practice Exercises (try these!)
# -------------------------------

# 1. Print your name and your favorite hobby
# 2. Create a list of 5 colors and print the third one
# 3. Create a dictionary for a car (make, model, year) and print the model
# 4. Given the list of numbers [4, 7, 2, 9, 5], find the sum
# 5. BONUS: Use pandas to create a DataFrame of your favorite movies and their release years

# Great job reaching the end of this file!
# Practice a little bit every day.
# You are on your way to becoming a Python developer! 🚀
