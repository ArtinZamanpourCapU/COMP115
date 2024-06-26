"""
Lab 4 - Functions and Lists 
(100 marks in total, including 7 exercises)

Author:  <your name>
Due Date: This Friday (Feb. 2) 11am.

Objective:
1. Practice coding simple Python functions and writing unit tests testing functions by assert
2. Practice how to operate on lists
3. Practice with iterations using loop
4. Practice with the boolean expression and conditionals
5. Practice using the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, etc. 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Example 1: 

To implement a function for calculating the perimeter of a rectangle,
we know this function should have two parameters as inputs: length and width
of a rectangle.
We should also know this function should return a value of the perimeter.
Before or after our function implementation, we know that our function, let's say,
function's name is rectangle_perimeter, shoud pass the unit tests such as:
assert rectangle_perimeter(5, 6) == 22
assert rectangle_perimeter(1.25, 2.43) == 7.36
assert rectangle_perimeter(1.001, 2.005) == 6.01
"""

def rectangle_perimeter(length, width):
    perimeter = (length + width) * 2
    return round(perimeter, 2) # Round to the result to two decimal places


assert rectangle_perimeter(5, 6) == 22
assert rectangle_perimeter(1.25, 2.43) == 7.36
assert rectangle_perimeter(1.001, 2.005) == 6.01

"""
Exercise 1 (10 marks)

1 US dollar is around 1.34 Canadian dollars.
Write a function that takes American dollars as input 
and return the Canadian dollars equivalent. 

Requirement: Use round() to round the result to two decimal places.
For example, convert_american_dollars(100.05) should return 134.07
"""


def convert_american_dollars(american_dollars):
    exchange_rate = 1.34
    canadian_dollars = american_dollars * exchange_rate
    canadian_dollars_rounded = round(canadian_dollars, 2)
    return canadian_dollars_rounded

american_dollars_amount = 100.05
equivalent_canadian_dollars = convert_american_dollars(american_dollars_amount)
print(equivalent_canadian_dollars)

# assert (convert_american_dollars(1) == 1.34)
# assert (convert_american_dollars(100) == 134)
# assert (convert_american_dollars(100.05) == 134.07)

"""
Exercise 2 (10 marks)

From Interactive textbook Chap. 2.13 Question 3

## 
Convert Chap. 2.13 Question 3's solution (the following code) to a function
Your function should be able to pass the unit tests below.
##

current_time_string = input("What is the current time (in hours)? ")
waiting_time_string  = input("How many hours do you have to wait? ")

current_time_int = int(current_time_string)
waiting_time_int = int(waiting_time_string)

hours = current_time_int + waiting_time_int

timeofday = hours % 24

print(timeofday)
"""


def calculate_time_of_day(current_time_str, waiting_time_str):
    current_time_int = int(current_time_str)
    waiting_time_int = int(waiting_time_str)

    hours = current_time_int + waiting_time_int

    time_of_day = hours % 24

    return time_of_day

current_time_input = input("What is the current time (in hours)? ")
waiting_time_input = input("How many hours do you have to wait? ")

result = calculate_time_of_day(current_time_input, waiting_time_input)
print(result)




# assert alarm_time('13', '1') == 14
# assert alarm_time('12', '24') == 12
# assert alarm_time('13', '11') == 0
# assert alarm_time('15', '10') == 1


"""
Example 2 - To implement our own sum function that takes a list of numbers
as a parameter and returns the sum of the numbers.
"""
def my_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total

assert my_sum([1, 4, 5]) == 10
assert my_sum([9, 5]) == 14

"""
Exercise 3 (15 marks) - From interactive textbook 10.31.4

Write a function called average that takes a list of numbers as a parameter 
and returns the average of the numbers.

(Note: there is a built-in function named sum() but pretend you cannot use it.)

"""

# Function implementation (10 marks)
def average(numbers):
    if not numbers:
        return None  # Handle the case where the list is empty to avoid division by zero

    total = 0
    count = 0

    for number in numbers:
        total += number
        count += 1

    average_value = total / count
    return average_value

numbers_list = [2, 4, 6, 8, 10]
result = average(numbers_list)
print(result)


# Write and pass your units tests (5 marks)

"""
Exercise 4 (15 marks) - From interactive textbook 10.31.5

Write a Python function named find_max that takes a parameter containing 
a nonempty list of positive integers and returns the maximum value. 

(Note: there is a built-in function named max() but pretend you cannot use it.)

"""

# Function implementation (10 marks)
def find_max(numbers):
    if not numbers:
        return None  # Handle the case where the list is empty

    max_value = numbers[0]  # Assume the first element is the maximum

    for number in numbers[1:]:
        if number > max_value:
            max_value = number

    return max_value

numbers_list = [5, 12, 8, 3, 15, 7]
result = find_max(numbers_list)
print(result)


# Write and pass your units tests (5 marks)

"""
Exercise 5 (15 marks) 

Write a function called evens() that takes a list of numbers nums as its parameter 
and returns a list of nums' even numbers.

For example,
evens([1, 2, 3, 4]) will return [2, 4]
evens([2, 4, 6, 7, 8]) will return [2, 4, 6, 8]
evens([1, 3]) will return []

Hint:
1. Use a moduler operator % to check if a num is even. 
2. Create a variable assigned to an empty list [], 
and use the append() to add the required elements to the list.

"""

# Function implementation (10 marks)
def evens(nums):
    even_numbers = []

    for num in nums:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers

result1 = evens([1, 2, 3, 4])
result2 = evens([2, 4, 6, 7, 8])
result3 = evens([1, 3])

print(result1)  # Output: [2, 4]
print(result2)  # Output: [2, 4, 6, 8]
print(result3)  # Output: []


# Write and pass your units tests (5 marks)


"""
Exercise 6 (15 marks) - From interactive textbook 10.31.6

Write a function sum_of_squares(xs) that 
computes the sum of the squares of the numbers in the list nums. 
For example, sum_of_squares([2, 3, 4]) should return 4 + 9 + 16 which is 29:

Hint: you can use the power operator ** to calculate square
"""

# Function implementation (10 marks)
def sum_of_squares(xs):
    sum_squares = 0

    for num in xs:
        sum_squares += num ** 2

    return sum_squares

result = sum_of_squares([2, 3, 4])
print(result)  # Output: 29 (2^2 + 3^2 + 4^2 = 4 + 9 + 16 = 29)


# Write and pass your units tests (5 marks)
"""
Exercise 7 (20 marks) 

Write a function called squares() that takes a list of numbers nums as its parameter 
and returns a list of nums' squares.

For example,
squres([1, 2, 3, 4]) will return [1, 4, 9, 16]
squares([2, 4, 6, 7, 8]) will return [4, 16, 36, 49, 64]

Hint:
Create a variable assigned to an empty list [], 
and use the append() to add the required elements to the list.

"""

# Function implementation (15 marks)
def squares(nums):
    squared_numbers = []

    for num in nums:
        squared_numbers.append(num ** 2)

    return squared_numbers

result1 = squares([1, 2, 3, 4])
result2 = squares([2, 4, 6, 7, 8])

print(result1)  # Output: [1, 4, 9, 16]
print(result2)  # Output: [4, 16, 36, 49, 64]

# Write and pass your units tests (5 marks)



"""
Congratulations on finishing your lab4. This is a big move!
Now you just need to upload to your GitHub repository. That's all.
"""
