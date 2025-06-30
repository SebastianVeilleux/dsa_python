from collections import Counter, defaultdict

# 1. Define a dictionary with initial values
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# 2. Add or update a key-value pair
my_dict['d'] = 4  # Add
my_dict['b'] = 5  # Update
print(my_dict)  # Output: {'a': 1, 'b': 5, 'c': 3, 'd': 4}

# 3. Remove a key-value pair
removed_value = my_dict.pop('b')  # Removes 'b'
print(removed_value)  # Output: 5
print(my_dict)  # Output: {'a': 1, 'c': 3, 'd': 4}

last_removed = my_dict.popitem()  # Removes last item
print(last_removed)  # Output: ('d', 4)
print(my_dict)  # Output: {'a': 1, 'c': 3}

del my_dict['a']  # Delete key 'a'
print(my_dict)  # Output: {'c': 3}

my_dict.clear()  # Clear all elements
print(my_dict)  # Output: {}

# 4. Retrieve a value with get()
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.get('b'))  # Output: 2
print(my_dict.get('x', 0))  # Output: 0 (default value)

# 5. Check if a key exists
print('a' in my_dict)  # Output: True
print('z' in my_dict)  # Output: False

# 6. Get all keys, values, and items
print(my_dict.keys())   # Output: dict_keys(['a', 'b', 'c'])
print(my_dict.values()) # Output: dict_values([1, 2, 3])
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# 7. Copy a dictionary
copy_dict = my_dict.copy()
print(copy_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# 8. Merge dictionaries using update()
dict1 = {'x': 10, 'y': 20}
dict2 = {'y': 30, 'z': 40}
dict1.update(dict2)
print(dict1)  # Output: {'x': 10, 'y': 30, 'z': 40}

# 9. Count occurrences using a hashmap
numbers = [1, 2, 2, 3, 3, 3, 4]
count = Counter(numbers)
print(count)  # Output: {1: 1, 2: 2, 3: 3, 4: 1}

# 10. Sort dictionary by keys or values
sorted_by_keys = dict(sorted(my_dict.items()))
print(sorted_by_keys)  # Output: {'a': 1, 'b': 2, 'c': 3}

sorted_by_values = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted_by_values)  # Output: {'a': 1, 'b': 2, 'c': 3}

# 11. Default values using defaultdict
default_dict = defaultdict(int)
default_dict['a'] += 1
print(default_dict)  # Output: defaultdict(<class 'int'>, {'a': 1})
