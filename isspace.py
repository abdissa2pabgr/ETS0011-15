s1 = "   "  # Spaces only
s2 = "\t\n"  # Tab and newline (still whitespace)
s3 = " Hello "
s4 = ""

print(s1.isspace())  # True
print(s2.isspace())  # True
print(s3.isspace())  # False (contains letters)
print(s4.isspace())  # False (empty string)