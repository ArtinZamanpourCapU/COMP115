"""
Lab 6 - Strings and Tuples 
(100 marks in total, including 5 exercises - each 20 marks)

Author:  <your name>
Due Date: This Friday (Mar. 1) 11am.
Submission: Upload your lab python file to your GitHub repository.

Objective:
1. Learn how to write a good python docstring for documenting functions'
purpose, parameters, return values. A good docstring helps other developers 
understand how to use the function and serves as documentation that can be 
displayed in tools like IDEs. A sample docstring has been written for exercise 1 and 2,
students need to write good docstrings for all the other exercises.
2. Review how to code simple Python functions and write unit tests using assert
3. Practice how to operate on strings and tuples (similar to lists, but strings and tuples are immutable)
4. Review iterations using loop
5. Review the boolean expression and conditionals
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Exercise 1 (20 marks: function implementation: 10 marks, unit tests: 10 marks)

Complete the function below to reverse a string.

For example, 
reverse_str("Abd") should return "dbA".
reverse_str("COMP115") should return "511PMOC".

Hint: the accumulator algorithm and the string concatenation using the operator '+'
"""

def reverse_str(s):
    """
    This function reverses string s.

    E.g., 
    >>> reverse_str('app')
    'ppa'

    Parameters:
    - s (string): The string to be reversed

    Returns:
    - (string): A reversed version of string s.

    """
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

result = reverse_str("Abd")
print(result)  # Output: "dbA"

result = reverse_str("COMP115")
print(result)  # Output: "511PMOC"

# Your unit tests



"""
Exercise 2 (20 marks: function implementation: 10 marks, unit tests: 10 marks)

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string.

For example, 
count_vowels("Apple") should return 2, since 'A' and 'e' are vowels.
count_vowels("Hmmm") should return 0, since there are no vowels.

Hint: you may want to convert the input string to its lowercase version using s.lower() first.
"""
def count_vowels(s):
    """
    This function counts the number of vowels in the string s.

    E.g., 
    >>> count_vowels("Apple")
    2

    Parameters:
    - s (string): The string in which vowels are counted.

    Returns:
    - (int): The total number of vowels in the string s.

    """
    s = s.lower()
    count = 0

    for char in s:
        if char in ['a', 'e', 'i', 'o', 'u']:
            count += 1

    return count

result = count_vowels("Apple")
print(result)  # Output: 2

result = count_vowels("Hmmm")
print(result)  # Output: 0

    

# Your unit tests



"""
Exercise 3 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to remove the duplicate characters in a string.

E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"

Hint: We have implemented a function removing duplicates for a list in week 6. Similar.
"""
def remove_duplicates(s):
    """
    This function removes duplicate characters from the string s.

    E.g., 
    >>> remove_duplicates("apple")
    'aple'

    Parameters:
    - s (string): The input string from which duplicates are to be removed.

    Returns:
    - (string): The string with duplicate characters removed.

    """

    unique_chars = set()
    

    result_chars = []
    

    for char in s:
        
        if char not in unique_chars:
            
            unique_chars.add(char)
            result_chars.append(char)
    

    result = ''.join(result_chars)
    
    return result

result = remove_duplicates("apple")
print(result)  # Output: 'aple'

result = remove_duplicates("Popsipple")
print(result)  # Output: 'Popsile'

result = remove_duplicates("pear")
print(result)  # Output: 'pear'


# Your unit tests



"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the lowerest index of a charactor t found in a string s, 
to return -1 if the character is not in the string.

E.g.,
find_index("Abd", 'b') == 1
find_index("Abdccc", 'c') == 3
find_index("Abd", 'w') == -1

Note: we should implement our own algorithm, not using the built-in function find().
"""
def find_index(s, t):
    """
    This function finds the lowest index of character t in the string s.

    E.g., 
    >>> find_index("Abd", 'b')
    1

    Parameters:
    - s (string): The input string where the character is searched.
    - t (char): The character whose lowest index is to be found.

    Returns:
    - (int): The lowest index of character t in the string s, or -1 if not found.

    """

    result = -1
    
    for index, char in enumerate(s):
        
        if char == t:
            
            result = index if result == -1 or index < result else result
    
    return result

result = find_index("Abd", 'b')
print(result)  # Output: 1

result = find_index("Abdccc", 'c')
print(result)  # Output: 3

result = find_index("Abd", 'w')
print(result)  # Output: -1


# Your unit tests


"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the project completion day, 
given the current day in a week and estimated time of days to completion.

E.g.,
project_completion_day('Monday', 4) returns 'Friday'.
project_completion_day('Monday', 7) returns 'Monday'.
project_completion_day('Saturday', 2) returns 'Monday'.
project_completion_day('Saturday', 1) returns 'Sunday'.

Hint:
days_week.index(day) will return the index of the day in the tuple days_week.

"""

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')
# Notice that days_week is a tuple, and it works the same if it's a list,
# since the index operation is the same for tuple and list.


days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def project_completion_day(day, days_to_completion):
    """
    This function calculates the project completion day given the current day and estimated time of days to completion.

    E.g., 
    >>> project_completion_day('Monday', 4)
    'Friday'

    Parameters:
    - day (string): The current day in the week.
    - days_to_completion (int): The estimated time of days to completion.

    Returns:
    - (string): The project completion day.

    """
    
    current_day_index = days_week.index(day)
    
    
    completion_day_index = (current_day_index + days_to_completion) % 7
    
    
    completion_day = days_week[completion_day_index]
    
    return completion_day

result = project_completion_day('Monday', 4)
print(result)  # Output: 'Friday'

result = project_completion_day('Monday', 7)
print(result)  # Output: 'Monday'

result = project_completion_day('Saturday', 2)
print(result)  # Output: 'Monday'

result = project_completion_day('Saturday', 1)
print(result)  # Output: 'Sunday'

# Your unit tests



"""
Congratulations on finishing your lab6. Hope you feel more confident on function implementation.

Now you just need to upload it to your GitHub repository. That's all.
"""
