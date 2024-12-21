# Define a list with initial values
arr = [1, 2, 3]

# Add an element to the end of the list using append()
arr.append(4)  # Adds 4 at the end of the list
# arr = [1, 2, 3, 4]

# Insert an element at a specific index using insert()
# Moves all other elements to the right
arr.insert(2, 6)  # Inserts 6 at index 2
# arr = [1, 2, 6, 3, 4]
print(arr)  # Output: [1, 2, 6, 3, 4]

# Remove a specific element (not by index) using remove()
arr.remove(1)  # Removes the first occurrence of 1
# arr = [2, 6, 3, 4]
print(arr)  # Output: [2, 6, 3, 4]

# Print (returns) and remove the last element using pop()
popped_element = arr.pop()  # Removes and returns the last element (4)
print(popped_element)  # Output: 4
# arr = [2, 6, 3]

# Sort the list in ascending and descending order using sorted()
sorted_arr_asc = sorted(arr)  # Returns a new list sorted in ascending order
sorted_arr_desc = sorted(arr, reverse=True)  # Returns a new list sorted in descending order
print(sorted_arr_desc)  # Output: [6, 3, 2]
print(sorted_arr_asc)   # Output: [2, 3, 6]

# Reverse the list using reversed()
reversed_arr = list(reversed(arr))  # Returns a new list in reversed order
print(reversed_arr)  # Output: [3, 6, 2]

# Extend a list by adding elements from another list using extend()
arr2 = [5, 7, 8, 9, 12]  # Define another list
arr.extend(arr2)  # Adds all elements of arr2 to arr
print(arr)  # Output: [2, 6, 3, 5, 7, 8, 9, 12]

# Count the number of occurrences of a specific element
print(arr.count(1000))  # Output: 0 (1000 is not present in the list)

# Find the index of a specific element using index()
print(arr2.index(7))  # Finds the index of the first occurrence of 7
# Output: 1

# Create a copy of a list using copy()
arr3 = arr2.copy()  # Creates a separate copy of arr2
print(arr3)  # Output: [5, 7, 8, 9, 12]
print(arr2)  # Output: [5, 7, 8, 9, 12]

# Remove an element from the list by index using del
del arr[0]  # Deletes the element at index 0
print(arr)  # Output: [6, 3, 5, 7, 8, 9, 12]

# Clear all elements from the list using clear()
arr.clear()  # Removes all elements, leaving the list empty
print(arr)  # Output: []
