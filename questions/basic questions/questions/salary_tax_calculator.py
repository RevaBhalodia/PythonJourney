def calculate_tax(salary):

    tax = 0

    if salary <= 250000:
        tax = 0

    elif salary <= 500000:
        tax = (salary - 250000) * 0.05

    elif salary <= 1000000:
        tax = (250000 * 0.05) + (salary - 500000) * 0.20

    else:
        tax = (250000 * 0.05) + (500000 * 0.20) + (salary - 1000000) * 0.30

    net_salary = salary - tax

    print("\nAnnual Salary:", salary)
    print("Total Tax:", tax)
    print("Net Salary:", net_salary)


salary = float(input("Enter your annual salary: "))
calculate_tax(salary)
