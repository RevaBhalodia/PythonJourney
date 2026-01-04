dict = {
    "table": ["a piece of furniture", "lists of facts and figures "],
    "cat": "a small animal"

}
print(dict)

# count
list ={"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(list))


#wap
marks = {}# empty dictionary

n = int(input("How many subjects? "))

for i in range(n):
    subject = input("Enter subject name: ")
    mark = int(input(f"Enter marks for {subject}: "))
    marks[subject] = mark# adding to dictionary

print("\nStudent Marks:")
print(marks)


# figure out a way to store 9 and 9.0 as sepearte values in the set
values = {9 , 9.0}
print(values)
val = {9,"9.0"}
print(val)
set ={
    ("float", 9.0),
    ("int",9)
    }
print(set)