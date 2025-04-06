append() Method
The append() method adds an element to the end of the list. It modifies the original list in place.

python
Copy
Edit
 
 clear() Method
The clear() method removes all elements from the list, making it empty.

copy() Method
The copy() method creates a shallow copy of the list. This means the new list contains the same elements but is a separate object from the original list.

copy()

Creates a shallow copy of the list.

index(value, start, end)

Returns the index of the first occurrence of value in the list.

Optional start and end define a search range.

extend(iterable)

Adds all elements of iterable (list, tuple, set, etc.) to the list.

Modifies the original list in place.

remove Method
The remove method searches for the first occurrence of a specified value in a list and deletes it. If the value is not found, it raises a ValueError.

insert() Method
The insert() method inserts an element at a specified index.

pop() Method
The pop() method removes and returns an element at a specified index.

reverse() Method
Purpose: Reverses the elements of the list in place (modifies the original list).

Note: It does not sort, it just flips the order.

sort() Method
Purpose: Sorts the list in ascending order by default.

Note: Also modifies the list in place.

Use sort(reverse=True) for descending order.

