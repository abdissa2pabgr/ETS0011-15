isdigit()  is an example of string methods used in python and it Checks if the string consists of only digits or not. Its output is boolean

str.index(substring, start, end)
Finds the index (position) of the first occurrence of a specified substring within the string.
If the substring is not found, it raises a ValueError.


str.startswith(prefix, start, end)
Checks if the string starts with a specified substring.
Returns True if it does, False otherwise.


 str.endswith(suffix, start, end)
Checks if the string ends with a specified substring.
Returns True if it does, False otherwise.


str.rstrip()
The .rstrip() method removes trailing whitespace (spaces, tabs, newlines) or specified characters from the right side of a string.


str.split()
The .split() method splits a string into a list of substrings based on a specified delimiter. By default, it splits on whitespace.



str.join()
The .join() method joins elements of an iterable (like a list) into a single string using a specified separator.



str.replace()
The .replace(old, new, count) method replaces occurrences of a substring with another substring.

old: The substring to be replaced.

new: The substring to replace with.

count (optional): Number of times to replace (default: all occurrences).



str.strip()
The .strip() method removes leading and trailing whitespace (or specified characters) from a string.


str.lstrip()
The .lstrip() method removes leading whitespace (or specified characters) from the left side of a string.



str.isalnum()
Function:

This method returns True if all characters in the string are alphanumeric (i.e., only letters and numbers).

If the string contains spaces, symbols, or is empty, it returns False.



str.isspace()
Function:

This method returns True if the string only contains whitespace characters (spaces, tabs, newlines).

If the string has any non-space characters, it returns False.



str.format()
Function:

This method is used to format strings by inserting values into placeholders {}.

It allows for dynamic string creation with variables.



f-strings (Formatted String Literals)
Function:

f-strings provide a concise and readable way to format strings in Python.

Introduced in Python 3.6, f-strings allow embedding expressions inside string literals using {}



len()
Function:

len() returns the number of elements in an object (string, list, tuple, dictionary, etc.).



str.encode()
Function:

Converts a string into bytes using a specified encoding (default is UTF-8).

Useful for working with binary data, file handling, and network communication.

str.islower()

This method checks if all the alphabetic characters in a string are lowercase.

If the string contains at least one letter and all letters are lowercase, it returns True; otherwise, it returns False.

str.isupper()

This method checks if all the alphabetic characters in a string are uppercase.

If the string contains at least one letter and all letters are uppercase, it returns True; otherwise, it returns False.

str.isalpha()

This method checks if all characters in the string are alphabetic (letters) and there are no numbers or special characters.

If the string contains only letters, it returns True; otherwise, it returns False.

str.swapcase()
This method returns a new string where all uppercase letters are converted to lowercase and all lowercase letters are converted to uppercase.

str.find(sub, start, end)
This method searches for a substring (sub) in the given string.

It returns the index of the first occurrence of sub or -1 if the substring is not found.

Optional start and end arguments can define a search range.

str.title() in Python
The title() method returns a new string where the first letter of each word is capitalized, and all other letters are converted to lowercase.

It is useful for formatting strings into title case.

