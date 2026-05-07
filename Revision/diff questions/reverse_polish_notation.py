def eval_rpn(tokens):
    stack = []

    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]
# Example usage:
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.    
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
# Note that division between two integers should truncate toward zero.
# For example, given the tokens ["2", "1", "+", "3", "*"], the expression is ((2 + 1) * 3) which evaluates to 9.
# Given the tokens ["4", "13", "5", "/", "+"], the expression is (4 + (13 / 5)) which evaluates to 4 + 2 = 6.
