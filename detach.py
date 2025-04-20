import io

# Create a binary stream
binary_stream = io.BytesIO(b"Hello, world!")

# Wrap the binary stream with TextIOWrapper
text_stream = io.TextIOWrapper(binary_stream, encoding='utf-8')

# Detach the binary buffer
buffer = text_stream.detach()

# Output:
print("Buffer is detached:", isinstance(buffer, io.BufferedIOBase))  # True
# Trying to use text_stream now would raise ValueError
