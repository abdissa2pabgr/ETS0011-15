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

str.isalnum()
Function:

This method returns True if all characters in the string are alphanumeric (i.e., only letters and numbers).

If the string contains spaces, symbols, or is empty, it returns False.

s1 = "Hello123"
s2 = "Hello 123"
s3 = "123"
s4 = ""

print(s1.isalnum())  # True (only letters and numbers)
print(s2.isalnum())  # False (contains a space)
print(s3.isalnum())  # True (only numbers)
print(s4.isalnum())  # False (empty string)

str.isspace()
Function:

This method returns True if the string only contains whitespace characters (spaces, tabs, newlines).

If the string has any non-space characters, it returns False.

s1 = "   "  # Spaces only
s2 = "\t\n"  # Tab and newline (still whitespace)
s3 = " Hello "
s4 = ""

print(s1.isspace())  # True
print(s2.isspace())  # True
print(s3.isspace())  # False (contains letters)
print(s4.isspace())  # False (empty string)

str.format()
Function:

This method is used to format strings by inserting values into placeholders {}.

It allows for dynamic string creation with variables.

name = "Abdissa"
age = 25

message = "My name is {} and I am {} years old.".format(name, age)
print(message)
# Output: My name is Abdissa and I am 25 years old.

f-strings (Formatted String Literals)
Function:

f-strings provide a concise and readable way to format strings in Python.

Introduced in Python 3.6, f-strings allow embedding expressions inside string literals using {}

name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 25 years old.

len()
Function:

len() returns the number of elements in an object (string, list, tuple, dictionary, etc.).

# Example with a string
text = "Hello"
print(len(text)) 
 # Output: 5

# Example with a list
numbers = [1, 2, 3, 4, 5]
print(len(numbers)) 
 # Output: 5

# Example with a dictionary
data = {"name": "Alice", "age": 25}
print(len(data)) 
 # Output: 2 (counts the number of keys)

str.encode()
Function:

Converts a string into bytes using a specified encoding (default is UTF-8).

Useful for working with binary data, file handling, and network communication.

text = "Hello, world!"
encoded_text = text.encode()  # Default UTF-8 encoding
print(encoded_text) 
 # Output: b'Hello, world!'

# Encoding with a different format
encoded_utf16 = text.encode("utf-16")
print(encoded_utf16)  
# Output: b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00w\x00o\x00r\x00l\x00d\x00!\x00'

# Handling errors
text = "Héllo"
encoded_ascii = text.encode("ascii", errors="ignore")  # Ignores characters not in ASCII
print(encoded_ascii)  
# Output: b'Hllo'
