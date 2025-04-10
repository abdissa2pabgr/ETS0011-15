my_dict = {'name': 'Alice'}
value = my_dict.setdefault('age', 25)
print(value)        # 25
print(my_dict)      # {'name': 'Alice', 'age': 25}
