f = open("example.txt", "r")
line1 = f.readline()
line2 = f.readline()
f.close()

print("Line 1:", line1.strip())
print("Line 2:", line2.strip())

# Output:
# Line 1: Hello, Abdissa!
# Line 2: Welcome to Python.
