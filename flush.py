f = open("sample.txt", "w")
f.write("This will be flushed.")
f.flush()
print("Flushed content to file.")
f.close()

# Output: Flushed content to file.
