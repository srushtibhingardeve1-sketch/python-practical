# Accept inputs for age and annual family income
age = int(input("Enter applicant's age: "))
income = float(input("Enter annual family income (₹): "))

# Define qualification limits
AGE_LIMIT = 25
INCOME_LIMIT = 300000.0

# Evaluate eligibility using logical 'and' operator
is_eligible = (age < AGE_LIMIT) and (income < INCOME_LIMIT)

# Display formatted result
print("\n" + "=" * 45)
print(f"{'SCHOLARSHIP ELIGIBILITY REPORT':^45}")
print("=" * 45)
print(f" Age Status          : {age} years old")
print(f" Annual Income       : ₹{income:,.2f}")
print("-" * 45)

if is_eligible:
    print(" Status              : QUALIFIED")
    print(" Remarks             : Applicant meets all criteria.")
else:
    print(" Status              : NOT QUALIFIED")
    print(" Remarks             :", end=" ")
    if age >= AGE_LIMIT and income >= INCOME_LIMIT:
        print("Exceeds age and income limits.")
    elif age >= AGE_LIMIT:
        print("Must be under 25 years old.")
    else:
        print("Income must be below ₹3,00,000.")

print("=" * 45)