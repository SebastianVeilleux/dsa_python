# Crear un string y una lista de caracteres
s = "hola"
chars = list(s)  # ['h', 'o', 'l', 'a']

# -------------------------------
# ➕ Concatenación de strings — O(n + m)
s2 = s + " mundo"  # "hola mundo"

# -------------------------------
# ➕ Multiplicación — O(n × k)
echo = "ha" * 3  # "hahaha"

# -------------------------------
# 🔍 Acceso por índice — O(1)
char = s[1]  # 'o'

# -------------------------------
# 🔄 Iteración — O(n)
for c in s:
    print(c)  # h\no\nl\na

# -------------------------------
# 🧠 'in' / 'not in' — O(n)
has_a = 'a' in s      # True
not_z = 'z' not in s  # True

# -------------------------------
# 📊 .count(char) — O(n)
count_l = s.count('l')  # 1

# -------------------------------
# 🔍 .find(substr) / .index(substr) — O(n)
idx = s.find('l')     # 2 (−1 si no está)
idx2 = s.index('l')   # 2 (lanza ValueError si no está)

# -------------------------------
# 🔁 .replace(old, new) — O(n)
s3 = s.replace("ho", "HA")  # "HAlA"

# -------------------------------
# 🔗 .join(iterable) — O(k)
chars = ['h', 'o', 'l', 'a']
s4 = ''.join(chars)  # "hola"

# -------------------------------
# 🔠 .upper() / .lower() / .capitalize() — O(n)
s.upper()        # "HOLA"
s.lower()        # "hola"
s.capitalize()   # "Hola"

# -------------------------------
# 🧹 .strip() / .lstrip() / .rstrip() — O(n)
"  hola  ".strip()   # "hola"
"  hola  ".lstrip()  # "hola  "
"  hola  ".rstrip()  # "  hola"

# -------------------------------
# ✂️ Slicing — O(k)
s5 = "abcdefg"
sub1 = s5[2:5]    # "cde"
sub2 = s5[::-1]   # "gfedcba"
sub3 = s5[::2]    # "aceg"

# -------------------------------
# 🔃 sorted(str) — O(n log n)
sorted_s = sorted("dcba")        # ['a', 'b', 'c', 'd']
joined_sorted = ''.join(sorted_s)  # "abcd"

# -------------------------------
# 🔃 reversed(str) — O(1) iterador, O(n) al convertir
reversed_iter = reversed(s)
list_reversed = list(reversed_iter)  # ['a', 'l', 'o', 'h']

# -------------------------------
# 🧪 Comparación de strings — O(n)
"abc" == "abc"  # True
"abc" < "abd"   # True (lexicográfica)

# -------------------------------
# 🧱 Conversión entre string y lista — O(n)
chars2 = list("hola")     # ['h', 'o', 'l', 'a']
str2 = ''.join(chars2)    # "hola"

# -------------------------------
# ⚙️ Modificar string → usar lista — O(n)
chars3 = list("hola")
chars3[0] = 'H'
new_s = ''.join(chars3)  # "Hola"
