import math  # Importing the math module to access mathematical constants and functions

# User-defined function to calculate the area of a circle
# Parameters:
#   radius (float): The radius of the circle (positive number)
# Returns:
#   float: The area of the circle (π * r^2)
def area_circle(radius: float) -> float:
    # Validate that radius is a positive number
    if radius <= 0:
        raise ValueError("The radius must be a positive number.")
    return math.pi * radius**2  # Formula for the area of a circle: π * r^2

# Example usage of the area_circle function
print(area_circle(5))  # Expected output: 78.53981633974483 (area of a circle with radius 5)


# User-defined function to find the maximum number in a list
# Parameters:
#   numbers (list): A list of numerical values (integers or floats)
# Returns:
#   int or float: The maximum number in the list
def max_num(numbers: list) -> float:
    # Check if the list is empty and raise an error
    if not numbers:
        raise ValueError("The list cannot be empty.")
    return max(numbers)  # Built-in function to get the largest number in the list

# Example usage of the max_num function
print(max_num([1, 2]))  # Expected output: 6 (the maximum value in the list)