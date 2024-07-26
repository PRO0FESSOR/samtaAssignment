# Task 2: Generate Fibonacci Series
# Problem Statement:
# Write a Python program that generates the Fibonacci sequence up to a specified number of
# terms, n. The Fibonacci sequence starts with 0 and 1, and each subsequent number in the
# sequence is the sum of the two preceding numbers (e.g., 0, 1, 1, 2, 3, 5, 8, ...). Prompt the
# user to enter the number of terms (n) they want in the sequence and then display the
# Fibonacci sequence up to that number of terms.


# FIBONACCI SERIES

# define a function to generate serier 

def generate_fibonacci_series(n):
    """
    Generate and print the Fibonacci series up to n terms.

    Parameters:
    n (int): The number of terms in the Fibonacci series to generate.

    Returns:
    None
    """

    print("Printing Fibonacci Series")

    # initialise the first and second term of fibonacci series
    a , b = 0 , 1

    # handel the case when n is 0 or less than 0
    if n<=0:
        print("please enter a positive integer")
        return

    # printing first term
    print(a , end='')

    # handel the case if n is 1
    if n==1:
        print()
        return

    # print the second term
    print(', ', b , sep='' , end='')

    # print the remaining terms 
    for _ in range(2,n):
        c = a + b
        print(', ', c , sep = '' , end = '')
        a, b = b, c

    # Print a new line at the end
    print()

# prompt a user for a number

print("Enter a number of terms to generate and print fibonacci series")

try:
    # read the user input and convert to an integer
    number_of_terms = int(input())
    
    # call the function to generate and print fibonacci series
    generate_fibonacci_series(number_of_terms)

except ValueError:
    # handel a case when input is not a valid integer
    print("Invalid input. Please enter numeric value")




