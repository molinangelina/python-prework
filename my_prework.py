# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    """Printing hello_USERNAME!"""
    print("hello_USERNAME!")

hello_name('username')

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """Printing odd #'s 1-100."""
    current_number = 1
    while current_number <= 100:
        print(current_number)
        current_number += 2

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 

def max_num_in_list(a_list):
    """Printing #5 out of the list 1-5."""
    last_element = integers[4:]
    print("The last element in the list is ", last_element)
    
integers = [1,2,3,4,5]
max_num_in_list(integers)


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false). 

def is_leap_year(year):
    """Defining values for leap years."""
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
        
# Making a while loop for user input.

while True:
    year = int(input("\nEnter a year : "))

    is_leap_year(year)
    if year == 999:
        break
    if is_leap_year(year):
        print(year, "is a leap year" + 
        "\n(Enter '999' to exit.) ")
    else:
        print(year, "is not a leap year" + 
        "\n(Enter '999' to exit.) ")

# Question 5
# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    user_list = [int(num) for num in input("Enter the integers separated by a space: ").split()]
    print("\nYour list: ", user_list)
    sorted_list = sorted(user_list)
    range_list=list(range(min(user_list), max(user_list)+1))
    if sorted_list == range_list:
        print("Your list has consecutive numbers.")
        return True
    else:
        print("Your list has no consecutive numbers.")
        return False

formatted_list = is_consecutive('user_list')
print(formatted_list)