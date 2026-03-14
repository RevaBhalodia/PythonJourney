salary = float(input("Enter salary: "))

if salary > 50000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

total_salary = salary + bonus

print("Bonus:", bonus)
print("Total Salary:", total_salary)