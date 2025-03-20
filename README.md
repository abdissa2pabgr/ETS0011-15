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