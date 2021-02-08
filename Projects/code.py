# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton', 'Andrew Ng', 'Sebastian Raschka', 'Yoshua Bengio']
class_2 = ['Hilary Mason', 'Carla Gentry', 'Corinna Cortes']
# Concatenate both the strings
new_class = class_1 + class_2
print(new_class)
# Append the list
new_class.append('Peter Warden')
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary
courses = {'Math': 65, 'English': 70, 'History': 80, 'French': 70, 'Science': 60}
print(courses)
total = sum(courses.values())
print(total)
percentage = (total/500)*100
print(percentage)


# Slice the dict and stores  the all subjects marks in variable
mathematics = {'Geoffery Hinton': 78, 'Andrew Ng': 95,'Sebastian Raschka': 65, 'Yoshua Benjio': 50, 'Hilary Mason': 70, 'Corinna Cortes': 66, 'Peter Warden': 75}
topper = max(mathematics, key = mathematics.get)
print(topper)

First_name, Last_name = topper.split()
full_name = Last_name+" "+First_name 
certificate_name = full_name.upper()
print(certificate_name)

# Code ends here


