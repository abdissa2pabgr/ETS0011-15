text = "apple, banana, cherry"
print(text.rpartition(","))  # Separator found
print(text.rpartition("not")) # Separator not found

# Output:
# ('apple, banana', ',', ' cherry')
# ('apple, banana, cherry', '', '')
