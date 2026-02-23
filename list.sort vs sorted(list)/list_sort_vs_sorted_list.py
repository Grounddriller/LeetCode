# ---------------------------------------------
# Demonstrating list.sort() vs sorted()
# ---------------------------------------------

# Original list
numbers = [5, 2, 9, 1, 3]

print("Original list:", numbers)
print()


# Using list.sort()  (modifies original list)
print("Using list.sort()")

numbers.sort()  # sorts the list in place

print("After sort():", numbers)
print("Return value of sort():", numbers.sort())  # Will print None
print()

# Reset the list
numbers = [5, 2, 9, 1, 3]

# Using sorted()  (creates new list)
print("Using sorted()")

new_numbers = sorted(numbers)  # creates new sorted list

print("Original list after sorted():", numbers)
print("New sorted list:", new_numbers)
print("Return value of sorted():", sorted(numbers))