course= 'Python for Beginners'
print(course)
print(course.upper())
print(course.lower())
print(course.capitalize()) #capitalize first letter
print(course.count('n'))

print(course.find('n')) #returns index of first occurence of charatcer 'n'
print(course.find('Z')) #returns -1 if not found
print(course.find('for')) #returns index of word 'for'

print(course.replace('for','4'))
print(course.replace('n','m'))

print('Python' in course) #in keyword returns boolean value instead of index
print('X' in course)
print('n' in course)
