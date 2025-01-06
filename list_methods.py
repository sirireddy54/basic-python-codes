lst= [1,2,3,4,5,6]

print(lst)
lst.insert(0,-1)
print(lst)
lst.append(7)
print(lst)
x= lst.copy()
print(f"x list is {x}")
x.clear()
print(x)

fruits= ["apple","banana","orange","orange","grapes","orange"]
print(fruits.count("orange"))