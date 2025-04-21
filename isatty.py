f = open("sample.txt", "r")
print("Is TTY:", f.isatty())
f.close()

# Output: Is TTY: False
