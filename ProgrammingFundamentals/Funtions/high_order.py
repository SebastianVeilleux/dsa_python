# Create a list of numbers
numbers = [1, 2, 3, 4]

# Use map to apply a function to each element of the list
# In this case, we are squaring each number using a lambda function
squares = map(lambda x: x ** 2, numbers)

# Convert the result to a list and print it
print(list(squares))  # Expected output: [1, 4, 9, 16]


# Another list of numbers
numbers = [1, 2, 3, 4, 5]

# Use filter to select only the even numbers from the list
# We use a lambda function that checks if the number is divisible by 2 (even)
evens = filter(lambda x: x % 2 == 0, numbers)

# Convert the result to a list and print it
print(list(evens))  # Expected output: [2, 4]


# Import the reduce function from functools
from functools import reduce

# Another list of numbers
numbers = [1, 2, 3, 4]

# Use reduce to reduce the list to a single value
# In this case, we are summing all the elements of the list using a lambda function
total_sum = reduce(lambda x, y: x + y, numbers)

# Print the result of the sum
print(total_sum)  # Expected output: 10


# Higher-order function that returns another function
def create_multiplier(n):
    # Inside this function, we define another function that multiplies by 'n'
    def multiplier(x):
        return x * n
    # We return the 'multiplier' function we just created
    return multiplier

# Use the 'create_multiplier' function to create custom functions
# These functions multiply any number by the value 'n' that we pass

multiply_by_3 = create_multiplier(3)  # Creates a function that multiplies by 3
multiply_by_5 = create_multiplier(5)  # Creates a function that multiplies by 5

# Use the created functions with different values
print(multiply_by_3(10))  # 10 * 3 = 30
print(multiply_by_5(4))   # 4 * 5 = 20
