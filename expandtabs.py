text = "Hello\tWorld"
print(text.expandtabs())      # Default tab size (8 spaces)
print(text.expandtabs(4))     # Tab size of 4 spaces
print(text.expandtabs(2))     # Tab size of 2 spaces

# Output:
# "Hello   World"
# "Hello   World"
# "Hello World"
