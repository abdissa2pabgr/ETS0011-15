s1 = "Hello123"
s2 = "Hello 123"
s3 = "123"
s4 = ""

print(s1.isalnum())  # True (only letters and numbers)
print(s2.isalnum())  # False (contains a space)
print(s3.isalnum())  # True (only numbers)
print(s4.isalnum())  # False (empty string)