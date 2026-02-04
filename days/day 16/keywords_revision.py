#Print all Python keywords using the keyword module.
import keyword

print(keyword.kwlist)

#Write a program using any 5 Python keywords you have learned(example: if, else, for, break, pass).
for i in range(1,6):
    if i == 3:
        pass
    elif i == 4:
        break
    else:
        print(i)