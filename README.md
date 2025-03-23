isdigit()  is an example of string methods used in python and it Checks if the string consists of only digits or not. Its output is boolean
text = "12345"
print(text.isdigit())  
# Output: True
str.index(substring, start, end)
Finds the index (position) of the first occurrence of a specified substring within the string.
If the substring is not found, it raises a ValueError.

text = "Hello, welcome to Python programming!"
index = text.index("Python")
print(index) 
 # Output: 18
str.startswith(prefix, start, end)
Checks if the string starts with a specified substring.
Returns True if it does, False otherwise.

text = "Hello, world!"
print(text.startswith("Hello"))  
print(text.startswith("world")) 
print(text.startswith("world", 7))  
# Output: True
 # Output: False
 # Output: True
 str.endswith(suffix, start, end)
Checks if the string ends with a specified substring.
Returns True if it does, False otherwise.

text = "data.txt"
print(text.endswith(".txt"))  
print(text.endswith(".csv"))  
print(text.endswith("data", 0, 4))  
# Output: True
# Output: False
# Output: True
str.rstrip()
The .rstrip() method removes trailing whitespace (spaces, tabs, newlines) or specified characters from the right side of a string.

text = "Hello, World!   "
cleaned_text = text.rstrip()  # Removes trailing spaces
print(f"'{cleaned_text}'")  
# Output: 'Hello, World!'

# Removing specific characters
text2 = "Python!!!"
cleaned_text2 = text2.rstrip("!")
print(cleaned_text2) 
 # Output: 'Python'
str.split()
The .split() method splits a string into a list of substrings based on a specified delimiter. By default, it splits on whitespace.

sentence = "Python is awesome"
words = sentence.split()  # Splitting by spaces
print(words)  
# Output: ['Python', 'is', 'awesome']

# Splitting using a custom delimiter
data = "apple,banana,grape"
fruits = data.split(",")
print(fruits)  
# Output: ['apple', 'banana', 'grape']

str.join()
The .join() method joins elements of an iterable (like a list) into a single string using a specified separator.

words = ['Python', 'is', 'awesome']
sentence = " ".join(words)  # Joining with space
print(sentence)  # Output: 'Python is awesome'

# Joining with a different separator
fruits = ['apple', 'banana', 'grape']
csv_string = ",".join(fruits)
print(csv_string)  
# Output: 'apple,banana,grape'

str.replace()
The .replace(old, new, count) method replaces occurrences of a substring with another substring.

old: The substring to be replaced.

new: The substring to replace with.

count (optional): Number of times to replace (default: all occurrences).

text = "Hello, world!"
new_text = text.replace("world", "Python")
print(new_text)  # Output: 'Hello, Python!'

# Limiting the number of replacements
sentence = "banana banana banana"
new_sentence = sentence.replace("banana", "apple", 2)
print(new_sentence)  
# Output: 'apple apple banana'

str.strip()
The .strip() method removes leading and trailing whitespace (or specified characters) from a string.

text = "   Hello, Python!   "
cleaned_text = text.strip()
print(f"'{cleaned_text}'")  
# Output: 'Hello, Python!'

# Removing specific characters
text2 = "---Hello---"
cleaned_text2 = text2.strip("-")
print(cleaned_text2)  
# Output: 'Hello'
str.lstrip()
The .lstrip() method removes leading whitespace (or specified characters) from the left side of a string.

text = "   Hello, Python!   "
cleaned_text = text.lstrip()
print(f"'{cleaned_text}'")  
# Output: 'Hello, Python!   '

# Removing specific characters
text2 = "---Hello---"
cleaned_text2 = text2.lstrip("-")
print(cleaned_text2) 
 # Output: 'Hello---'
