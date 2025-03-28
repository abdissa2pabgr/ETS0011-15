text = "hello world, welcome to python!"
title_text = text.title()  # Capitalizes the first letter of each word
print(title_text)  
# Output: "Hello World, Welcome To Python!"

text = "python's features are amazing"
title_text = text.title()  # Incorrectly capitalizes 'S after apostrophe
print(title_text)  
# Output: "Python'S Features Are Amazing"
