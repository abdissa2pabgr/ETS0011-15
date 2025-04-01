# Example of copy()
original_list = ["a", "b", "c"]
copied_list = original_list.copy()

print(copied_list)  
# Output: ['a', 'b', 'c']

# Verify that they are different objects
print(original_list is copied_list)  
# Output: False
