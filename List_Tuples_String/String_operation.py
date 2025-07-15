# Sample string
text = "  Hello Python World! Hello  "

# 1. len()
print("Length:", len(text))  # Total characters including spaces

# 2. Negative Indexing
print("Last character:", text[-1])
print("Second last character:", text[-2])

# 3. upper()
print("Uppercase:", text.upper())

# 4. lower()
print("Lowercase:", text.lower())

# 5. capitalize()
print("Capitalized:", text.capitalize())

# 6. strip()
print("Stripped:", text.strip())  # Removes leading/trailing spaces

print(text.strip(" "))

# 7. split()
print("Split:", text.split())  # Default splits on spaces

# 8. replace()
#when do replace not original string is modified it always returns new string
print("Replace 'Hello' with 'Hi':", text.replace("Hello", "Hi"))

# 9. Slicing
print("Sliced [2:12]:", text[2:12])  # Slicing part of the string

# 10. count()
print("Count of 'Hello':", text.count("Hello"))

# 11. startswith()
print("Starts with '  Hello':", text.startswith("  Hello"))

# 12. endswith()
print("Ends with 'Hello  ':", text.endswith("Hello  "))

# 13. find()
print("Find 'Python':", text.find("Python"))  # Returns first index or -1

# 14. index()
print("Index of 'World':", text.index("World"))  # Returns first index or error if not found
