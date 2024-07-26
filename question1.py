# Task 1: Calculate Area with Conditions
# Write a Python function calculate_area that takes two parameters: length and width. It
# should calculate and return the area of a rectangle. However, add a condition: if the length
# is equal to the width, return "This is a square!" instead of the area. Then, write a program to
# input values for length and width from the user and call the calculate_area function to
# display either the area or the message.

# Definition a function to calculate the area of a rectangle

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    str: A message indicating if it's a square or the area of the rectangle.
    """
    # Check if length and width are equal

    if length == width:
        return "This is a square!"
    else:
        area = length * width
        return f"Area of the rectangle is {area:.2f}"

# Prompt the user for input

print("Enter length and width to calculate the area of a rectangle:")

# Take input values for length and width, separated by a space

try:
    length, width = map(float, input().split())
    
    # Call the calculate_area function and store the result

    result = calculate_area(length, width)
    
    # Display the result

    print(result)
    
except ValueError:
    print("Invalid input. Please enter numeric values for length and width.")
