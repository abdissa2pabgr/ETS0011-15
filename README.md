add()
Purpose: Adds a single element to a set. If the element already exists, it has no effect.

clear()
Purpose: Removes all elements from the set, making it empty.

copy()
Purpose: Returns a shallow copy of the set.

difference()
Returns a new set containing the difference between two or more sets. It does not modify the original set.

difference_update()
Removes elements found in another set from the original set. It modifies the original set.

discard()
Removes a specified element from the set if it is present. Does nothing if the element is not found (no error)

intersection()
Returns a new set with elements common to all sets. The original sets are not modified.

intersection_update()
Updates the set by keeping only elements found in it and all other sets. The original set is modified.

isdisjoint()
Returns True if the two sets have no elements in common, otherwise returns False.

issubset()
Checks whether all elements of this set are in another set. Returns True or False.

issuperset()
Checks whether this set contains all elements of another set. Returns True or False.

pop()
Removes and returns a random element from the set. Raises a KeyError if the set is empty. Since sets are unordered, the element removed is arbitrary.

remove()
Removes a specific element from the set.
Raises a KeyError if the element is not found.

symmetric_difference()
Returns a new set with elements in either set but not in both. Original sets are not changed.

symmetric_difference_update()
Updates the original set with the symmetric difference of itself and another set.