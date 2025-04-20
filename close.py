f = open("sample.txt", "w")
f.write("Hello, Abdissa!")
f.close()

# Output: File is closed: True
print("File is closed:", f.closed)
