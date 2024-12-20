# Anonymous/Lambda Functions
# They are defined without name and written in one line
from functools import reduce

# Order tuples by second num
tuples = [(1, 4), (2, 3), (3, 1), (4, 2)]
ordered_tuples = sorted(tuples, key = lambda x: x[1])

# Square a number
square = lambda n : n**2
print(square(2))

# Sum two numbers
two_sum = lambda n, m : n+m
print(two_sum(1,2.0))

# Order a list of word by its len
words = ["hola", "hola5", "hola66", "hola777"]
ordered_words = sorted(words, key = lambda m: len(m))
print(ordered_words)

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda n: n%2 == 0, numbers))
print(even_numbers)

# Every element times two
numbers = [2, 4, 6, 8]
multiplied_numbers = list(map(lambda x: x * 2, numbers))
print(multiplied_numbers)

# Max of two numbers
max = lambda a, b: a if a > b else b
print(max)

# Calc the product of a list of nums
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)