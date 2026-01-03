#list.append() = adds value at the end 
books = [1,3,5,6,8,9,1]
print(books.append(4))
print(books)

#list.sort()= list sorted in ascending order (returns none)
books = [1,3,5,6,8,9,1]
print(books.sort)
print(books)

#list.sort(reverse=true) used for descending order
books = [1,3,5,6,8,9,1]
print(books.sort(reverse=True))
print(books)

#list.reverse()   (reverse the list)
list = ["a", "b", "c","r","n","s"]
list.reverse()
print(list)

#list.insert() insert element at index
list = ["a", "b", "c","r","n","s"]
list.insert(1,4)
print(list)

#list.remove()  removes first occurance of element
list = [1,3,4,1,3]
list.remove(3)
print(list)

#list.pop()  removes element at index
list = [2,4,6,8,10]
list.pop(3)
print(list)