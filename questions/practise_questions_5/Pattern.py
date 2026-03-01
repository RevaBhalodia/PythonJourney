def print_pattern(n):
    for i in range(1, n + 1):        # Rows
        for j in range(1, i + 1):    # Numbers in each row
            print(j, end=" ")
        print()  # Move to next line


num = int(input("Enter a number: "))
print_pattern(num)