# Welcome to Python3!

# This is a comment
#
# Anything on the same line that follows a '#' is not considered code
#
# Comments are used to improve readability of the code you write and
# also for you to learn more about code that someone else wrote

# TODO: (1) Type a comment below


# Displaying values
# If you want to see a value, put that value within the `print()` function like so:
# TODO: (2) Uncomment the print statements below and run this program to see the results.

#print(3)
#print(4)
#print(5)

# All programming languages have calculator functionality

# Addition:
#print(3+6)

# Subtraction:
#print(5-7)

# Multiplication:
#print(7*3)

# Division:
#print(10/2)

# Remainder (modulo):
#print(8%3)
#print(62%10)
#print(56%10)
#print(37%10)

# We can `print()` more than just numbers. `print()` also works on Strings.
# Anything enclosed within double-quotes "" is considered a string.
# You can put words and sentences within strings.
#print("Hello")
#print("I'm learning Python")

# Variables
# Rule 1 of programming is to avoid repetition. Variables help us reuse values
# and store temporary results. They are created like this:
x = 10

# The name of the variable is to the left of the equals sign
#     Be creative! Variable names can be anything as long as they start with a letter
#
# The value of the variable is to  the right of the equals sign
#     Variable values *must* be a number or a string (this is as much as we know so far)
#
# TODO: (3) What happens when you print(x)?



# TODO: (4) Create a variable named 'luckyNumber`, give it a value, then print it.

# TODO: (5) Create a variable named `catName`, give it a value, then print it.

# How to Use Functions
# Rule 2 of programming is also to avoid repetition. Functions are blocks of code that
# can be reused after they are written. We already know how to use functions.
# `print()` is a function that has been used a lot above.
#
# Example:  print(300)
# The name of the function is print. This is to the left of the parenthesis.
# The argument(s) to the function are within the parenthesis. In the above example, the argument is 300.

# How to Define Functions
# This is a bit trickier than using them. Here's an example function:
def say_hello():
    print("Hello")
#   Part 1: Function Signature
#       Defining a function starts with the 'def' keyword
#       Then comes the function name. In the example above, it is 'say_hello'
#       Then comes an opening and closing parenthesis.
#           Arguments to the function would be defined here.
#           In the example above, there is nothing in the parenthesis, so this function
#           uses no arguments.
#       Then comes a colon ':'
#           This marks  the end of the function signature
#   Part 2: Function Body
#       This is all code that is written on indented lines after the function signature
#       In the example above, the body contains `print("Hello"`

#  TODO: (6) Call the `say_hello()` function below.

# How to Define Functions Arguments
# TODO: (7) Define a function called `add_two` that takes in one number `n`

# Comparison Operators
# You may have seen this in math class:
#
# (1) Less than
#print(1 < 3)
#
# (2) Less than or equal to
#print(4 <= 3)
#
# (3) Greater than
#print(1 > 3)
#
# (4) Greater than or equal to
#print(6 >= 2)
#
# (5) Is Equal To?
#print(2 == 2)
#print(2 == 3)

# Notice that the result is equal to True or False.
# In programming, anything that equals True or False is called a Boolean.

# Conditional Statements
# These let programs execute different chunks of code depending on whether a statement is
# True of False.
# Here is an example:
#n = 7
#if n < 3:
#    print("n is small")
#else:
#    print("n is large")
# What do you think the above code will print?

# Loops
# while-loops
# Allow you to repeat a chunk of code as long as a condition is True
