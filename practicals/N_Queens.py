def solve_n_queens(n):
    def is_safe(row, col, assignment):
        for r in assignment:
            c = assignment[r]
            # Check same column or diagonal
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def get_domain(row, assignment):
        # Possible columns for a given row
        return [col for col in range(n) if is_safe(row, col, assignment)]

    def select_unassigned_variable(assignment):
        # MRV: choose row with minimum legal values
        unassigned = [r for r in range(n) if r not in assignment]
        return min(unassigned, key=lambda r: len(get_domain(r, assignment)))

    def forward_check(assignment):
        # Check if any unassigned variable has no valid domain
        for r in range(n):
            if r not in assignment:
                if len(get_domain(r, assignment)) == 0:
                    return False
        return True

    def backtrack(assignment):
        # If all rows assigned, solution found
        if len(assignment) == n:
            return assignment

        # Select variable using MRV
        row = select_unassigned_variable(assignment)

        for col in get_domain(row, assignment):
            # Assign value
            assignment[row] = col

            # Forward checking
            if forward_check(assignment):
                result = backtrack(assignment)
                if result:
                    return result

            # Undo assignment (backtrack)
            del assignment[row]

        return None

    return backtrack({})


def print_board(solution, n):
    if not solution:
        print("No solution found")
        return

    for i in range(n):
        row = ["Q" if solution[i] == j else "." for j in range(n)]
        print(" ".join(row))


# Example usage
n = 8
solution = solve_n_queens(n)
print("Solution:", solution)
print("\nBoard:")
print_board(solution, n)