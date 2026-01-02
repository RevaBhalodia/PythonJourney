# an operator is a symbol that performs certain operations between operands
# types: arithematic,relational,assignment,logical

#arithemetic 
a = 1
b = 2
print( a + b)
print( a - b)
print( a * b)
print( a / b)
print( a % b)     # % used to find reminder
print( a ** b)    # power

#relational
a = 50
b = 9
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)
print(a < b)
print(a > b)

#assignment 
num = 10
num -= 10
num *= 10
num /= 10
num += 10
print("num :", num)

#logical(not,and,or)
#not
a = 40
b =37
print(not False)
print(not (a>b))
#and
val1 = True
val2 = False
print("and operator:", val1 and val2)
#or
print("OR operator:", val1 and val2)