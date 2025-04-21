f = open("sample.txt", "r")
content = f.read()
print("File content:", content)
f.close()

# Output: File content: This will be flushed.
