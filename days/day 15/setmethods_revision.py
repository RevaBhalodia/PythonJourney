#s = {10, 20, 30},Remove 20,Add 40,Print the updated set
s = {10, 20, 30}
s.add(40)
s.remove(20)
print(s)


#Check whether 25 exists in the set {10, 20, 25, 30}.
set = {10, 20, 25, 30}

if 25 in set:
    print("25 exist in the set")
else:
    print("25 doesn't exist in the set")