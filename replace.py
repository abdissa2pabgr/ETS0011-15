text = "Hello, world!"
new_text = text.replace("world", "Python")
print(new_text)  # Output: 'Hello, Python!'

# Limiting the number of replacements
sentence = "banana banana banana"
new_sentence = sentence.replace("banana", "apple", 2)
print(new_sentence)  
# Output: 'apple apple banana'