# Crear una lista con elementos iniciales
arr = [1, 2, 3]

# -------------------------------
# ➕ .append(element) — O(1) amortizado
arr.append(4)  # [1, 2, 3, 4]

# -------------------------------
# ➕ .insert(index, element) — O(n)
arr.insert(2, 6)  # [1, 2, 6, 3, 4]

# -------------------------------
# ➕ .extend(iterable) — O(k), k = longitud del iterable añadido
arr.extend([7, 8])  # [1, 2, 6, 3, 4, 7, 8]

# -------------------------------
# ❌ .remove(element) — O(n)
arr.remove(6)  # [1, 2, 3, 4, 7, 8]

# -------------------------------
# ❌ del lista[indice] — O(n - i)
del arr[0]  # [2, 3, 4, 7, 8]

# -------------------------------
# ❌ .pop() — O(1) al final; O(n - i) con índice
last = arr.pop()        # last = 8; arr = [2, 3, 4, 7]
mid = arr.pop(1)        # mid = 3; arr = [2, 4, 7]

# -------------------------------
# 📊 .count(element) — O(n)
arr.count(4)  # 1

# -------------------------------
# 🔍 .index(element) — O(n)
arr.index(7)  # 2

# -------------------------------
# 🧹 .clear() — O(1)
arr.clear()  # []

# -------------------------------
# 📄 .copy() — O(n)
arr2 = [5, 7, 9]
arr3 = arr2.copy()  # arr3 = [5, 7, 9]

# -------------------------------
# 🔁 .reverse() — O(n)
# Invierte la lista en su lugar (modifica el original)
arr3.reverse()  # arr3 = [9, 7, 5]

# -------------------------------
# 🔁 reversed(lista) — O(1) para crear el iterador; O(n) al convertir en lista
# Útil para iterar sin copiar la lista
for val in reversed(arr3):
    print(val)  # 5\n7\n9

# Si necesitas una nueva lista invertida:
reversed_arr = list(reversed(arr3))  # [5, 7, 9]

# -------------------------------
# 🎯 Slicing invertido [::-1] — O(n) tiempo y espacio
# Crea una nueva lista invertida (no modifica la original)
nums = [0, 1, 2, 3, 4, 5, 6]
reversed_nums = nums[::-1]  # [6, 5, 4, 3, 2, 1, 0]

# También puedes hacer subarrays:
sub1 = nums[2:5]     # [2, 3, 4]
sub2 = nums[:3]      # [0, 1, 2]
sub3 = nums[::2]     # [0, 2, 4, 6]

# -------------------------------
# 🧮 len(lista) — O(1)
n = len(arr3)  # 3

# -------------------------------
# 🧠 'in' / 'not in' — O(n)
is_present = 7 in arr3      # True
is_missing = 10 not in arr3 # True

# -------------------------------
# 🔃 .sort() — O(n log n) (Timsort)
arr3.sort()              # [5, 7, 9]
arr3.sort(reverse=True)  # [9, 7, 5]

# -------------------------------
# 🔃 sorted(lista) — O(n log n)
# Devuelve una nueva lista ordenada (no modifica la original)
sorted_arr = sorted(arr3)                # [5, 7, 9]
sorted_desc = sorted(arr3, reverse=True) # [9, 7, 5]

# -------------------------------
# 🔗 Concatenación (a + b) — O(n + k)
a = [1, 2]; b = [3, 4]
c = a + b  # [1, 2, 3, 4]

# -------------------------------
# 🧱 Multiplicación ([x] * k) — O(n × k)
repeated = [0] * 5  # [0, 0, 0, 0, 0]

# -------------------------------
# 🔄 Iteración — O(n)
for val in arr3:
    print(val)  # 9\n7\n5

for i in range(len(arr3)):
    print(i, arr3[i])  # 0 9\n1 7\n2 5

for i, val in enumerate(arr3):
    print(i, val)  # 0 9\n1 7\n2 5
