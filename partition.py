text = "Python is awesome"
print(text.partition("is"))  # Separator found
print(text.partition("not")) # Separator not found

# Output:
# ('Python ', 'is', ' awesome')
# ('Python is awesome', '', '')
