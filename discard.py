a = {1, 2, 3, 4}

a.discard(3)
print(a)  # Output: {1, 2, 4}

a.discard(10)
print(a)  # Output: {1, 2, 4} (no error, element not found)
