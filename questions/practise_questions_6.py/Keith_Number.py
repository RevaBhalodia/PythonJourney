def is_keith_number(n):
    # Store digits in list
    digits = [int(d) for d in str(n)]
    k = len(digits)

    sequence = digits.copy()

    while True:
        next_term = sum(sequence[-k:])  # Sum of last k terms
        sequence.append(next_term)

        if next_term == n:
            return True
        if next_term > n:
            return False

num = int(input("Enter a number: "))

if is_keith_number(num):
    print("It is a Keith Number")
else:
    print("It is NOT a Keith Number")