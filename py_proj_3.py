# Create a tuple called fruits containing the following elements: "apple", "banana", "cherry", "date".
# Print the first and last element of the tuple.

fruits = ("apple", "banana", "cherry", "date")

print(fruits[0])
print(fruits[-1])


print('=======================================')

# Create a new tuple numbers with values (1, 2, 3, 4, 5).
# Use tuple unpacking to assign the first two elements of numbers to variables a and b, and the remaining elements to a variable rest.
# Print a, b, and rest.

numbers = (1, 2, 3, 4, 5)

a, b, *rest = numbers

print(a)
print(b)
print(rest)


print('=======================================')
# Try to change the second element of the fruits tuple to "blueberry". Write down what happens and why.


# fruits[1] = "blueberry"
# This will raise an error because tuples are unchangeble in Python.


print('=======================================')

# Create a set called colors with the elements "red", "green", "blue", "yellow".
# Add the color "purple" to the set.


colors = {"red", "green", "blue", "yellow"}

colors.add("purple")

print(colors)


print('=======================================')


# Create another set called primary_colors containing "red", "blue", and "yellow".
# Find the intersection of colors and primary_colors.
# Find the union of colors and primary_colors.
# Find the difference between colors and primary_colors.

primary_colors = {"red", "blue", "yellow"}

intersection = colors.intersection(primary_colors)
union = colors.union(primary_colors)
difference = colors.difference(primary_colors)

print(intersection)
print(union)
print(difference)



print('=======================================')

# Check if "green" is in primary_colors. Print the result.
# Check if "orange" is not in colors. Print the result.


primary_colors = {"red", "blue", "yellow"}

print("green" in primary_colors)

print("orange" not in colors)



print('=======================================')


# Create a dictionary called student_grades with the following key-value pairs:"Alice": 85
# "Bob": 90
# "Charlie": 78
# "Diana": 92
# Print the grade of "Bob".

student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92}

print(student_grades["Bob"])



print('========================================')

# Add a new student "Eve" with a grade of 88 to the dictionary.
# Update "Alice"'s grade to 95.
# Remove "Charlie" from the dictionary.
# Print the updated dictionary.


student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92}

student_grades["Eve"] = 88

student_grades["Alice"] = 95

del student_grades["Charlie"]

print(student_grades)


print('=====================================')

# loop through the dictionary and print each key-value pair.

student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92}

for key, value in student_grades.items():
    print(f"Student: {key}, Grade: {value}") 