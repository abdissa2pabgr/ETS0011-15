f = open("sample.txt", "r")
fd = f.fileno()

# Output: File descriptor: (an integer, e.g., 3 or 4 depending on system)
print("File descriptor:", fd)
f.close()
