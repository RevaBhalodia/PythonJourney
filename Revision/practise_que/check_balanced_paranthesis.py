def is_balanced(expr):
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}

    for ch in expr:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


expression = input("Enter expression: ")

if is_balanced(expression):
    print("Balanced")
else:
    print("Not Balanced")