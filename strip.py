text = "   Hello, Python!   "
cleaned_text = text.strip()
print(f"'{cleaned_text}'")  
# Output: 'Hello, Python!'

# Removing specific characters
text2 = "---Hello---"
cleaned_text2 = text2.strip("-")
print(cleaned_text2)  
# Output: 'Hello'