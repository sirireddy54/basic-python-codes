
#Lists are mutable and dynamic; list items can be added, removed or changed after the list is defined. 
# Lists are ordered; newly added items will be placed at the end of the list.

names= ['siri','chinnu','munish','rosh','dinesh']
print(names)
print(names[1]) #index value
print(names[-1])
names[1]='sowmu'
print(names)   
names.append('bharat')
print(names)
names.remove('munish')
print(names) #['siri', 'sowmu', 'rosh', 'dinesh', 'bharat']
print(names[1:3]) #['sowmu', 'rosh']

x= "my name is siri, I am 24 years old, I am from India"
print(x.split(" ")) #split by space and make it as list
print(x.split(",")) #split by comma and make it as list
