#Q1.Create a set of 5 numbers and print it.add one new number to the set.
s = {1,2,3,4,5}
s.add(9)
print(s)


'''
Create two sets:
A = {1, 2, 3}
B = {3, 4, 5}
Print:Union,Intersection
'''

A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))
print(A.intersection(B))