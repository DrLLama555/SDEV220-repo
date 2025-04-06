# 7.4 Make a list called things
things = ["mozzarella", "cinderella", "salmonella"]

# 7.5 Capitalize the element that refers to a person and print the list
things[1] = things[1].capitalize()  # Capitalizes "cinderella"
print(things)  # Output: ['mozzarella', 'Cinderella', 'salmonella']

# 7.6 Make the cheesy element of things all uppercase and print the list
things[0] = things[0].upper()  # Makes "mozzarella" uppercase
print(things)  # Output: ['MOZZARELLA', 'Cinderella', 'salmonella']

# 7.7 Delete the disease element from things and print the list
del things[2]  # Deletes "salmonella"
print(things)  # Output: ['MOZZARELLA', 'Cinderella']

# 9.1 Define a function called good()
def good():
    return ['Harry', 'Ron', 'Hermione']

# Example usage of the good() function
print("List from good():", good())  # Output: ['Harry', 'Ron', 'Hermione']

# 9.2 Define a generator function called get_odds()
def get_odds():
    for number in range(10):
        if number % 2 != 0:
            yield number

# Using a for loop to find and print the third value returned
odd_generator = get_odds()
count = 0
third_odd = None

for value in odd_generator:
    count += 1
    if count == 3:
        third_odd = value
        break

# Print the third odd number
print("The third odd number is:", third_odd)  # Output: 5
