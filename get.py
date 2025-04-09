person = {'name': 'Alice', 'age': 25}
print(person.get('name'))          # Output: Alice
print(person.get('gender'))        # Output: None
print(person.get('gender', 'N/A')) # Output: N/A
