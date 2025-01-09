
fruits=['apple','banana','grapes']
for item in fruits:
    print(item)

print("===============")

n=5
for i in range(n):
    print(i)

print("===============")

n=5
for i in range(1,n):
    print(i)

print("===============")

name= "siri"
for character in name:
    print(character)

print("===============")

Dict = {"name":"siri", "age":25, "city":"Saint Louis"}
for key,value in Dict.items():
    print(f"{key}:{value}")

print("===============")

#nested loops
for i in range(3):
    for j in range(2):
        print(f"i= {i} , j= {j}")

print("===============")

#for , else statements
for i in range(3):
    print(i)
else:
    print("finished")

    