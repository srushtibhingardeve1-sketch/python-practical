# Accept inputs for employee details
name = input("Enter Employee Name: ")
role = input("Enter Role/Designation: ")
monthly_salary = float(input("Enter Monthly Salary: "))

# Calculate annual salary
annual_salary = monthly_salary * 12

# Output Formatted Employee Identity Card
print("\n" + "=" * 40)
print(f"{'EMPLOYEE IDENTITY CARD':^40}")
print("=" * 40)
print(f" Name           : {name:<23}")
print(f" Role           : {role:<23}")
print(f" Monthly Salary : ${monthly_salary:<20.2f}")
print(f" Annual Salary  : ${annual_salary:<20.2f}")
print("=" * 40)