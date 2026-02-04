# set.add(el) = adds an element
# set.remove(el) = remoes the element
# set.clear() = empties the set
# set.pop = removes a random value
# set is mutable but the elements under set are immutable
#1
collection = set()
collection.add(9)
collection.add(1)
collection.add(1)
print(collection)

# 2
collection.remove(1)
print(collection)
# 3
collection.clear()
print(collection)
print(len(collection))
# 4
collection = {23,45,67,89,11, 12,"rico","eva","will","max","mike"}
print(collection.pop())



#set.union(set2) = combines both set values and returns new set
# set.intersection(set2) =  combines common values and return new

set1 = {"nancy","johanthan","steve","robin","eddie","hopper","joyce","mike","dustin","eleven"}
set2 = {"erica","will","mike","dustin","max","lucus","eddie"}
print(set1.union(set2))
print(set1.intersection(set2))