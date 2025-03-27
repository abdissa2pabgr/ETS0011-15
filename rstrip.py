text = "Hello, World!   "
cleaned_text = text.rstrip()  # Removes trailing spaces
print(f"'{cleaned_text}'")  
# Output: 'Hello, World!'

# Removing specific characters
text2 = "Python!!!"
cleaned_text2 = text2.rstrip("!")
print(cleaned_text2) 
 # Output: 'Python'