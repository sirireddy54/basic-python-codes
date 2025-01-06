lst= []
n= int(input("enter number of elements"))
print("emter list items")
for i in range(n):
    element= int(input())
    lst.append(element)
    i+=1
print(lst)

print("List items are: ",lst)
#print(f"list items are {lst}")

''' 
F-strings, or formatted string literals, are a feature introduced in Python 3.6 that allows you to embed expressions directly within string literals. 
They are prefixed with the letter 'f' or 'F' and use curly braces {} to enclose expressions that will be evaluated and inserted into the string.
'''