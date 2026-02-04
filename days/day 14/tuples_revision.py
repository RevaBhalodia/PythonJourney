#Create a tuple of 4 fruits and print:The tuple,The second element.
fruits = ("apple", "banana", "cheery", "berries")
print(fruits)
print(fruits[1])
#Try to change one element of the tuple.
fruits_list = list(fruits)
fruits_list[0] = "grape"
fruits = tuple(fruits_list)
print(fruits)
