# Accept candidate details and academic metrics
graduation_score = float(input("Enter graduation score (%): "))
backlogs = int(input("Enter number of active academic backlogs: "))

# Define criteria thresholds
MIN_SCORE = 70.0

# Check eligibility (70% or more AND 0 active backlogs)
is_eligible = (graduation_score >= MIN_SCORE) and (backlogs == 0)

# Print Formatted Eligibility Status
print("\n" + "=" * 45)
print(f"{'PLACEMENT ELIGIBILITY REPORT':^45}")
print("=" * 45)
print(f" Graduation Score    : {graduation_score:.2f}%")
print(f" Active Backlogs     : {backlogs}")
print("-" * 45)

if is_eligible:
    print(" Status              : ELIGIBLE")
    print(" Remarks             : Meets all placement criteria.")
else:
    print(" Status              : NOT ELIGIBLE")
    print(" Remarks             :", end=" ")
    if graduation_score < MIN_SCORE and backlogs > 0:
        print("Score below 70% and active backlogs present.")
    elif graduation_score < MIN_SCORE:
        print("Graduation score must be at least 70%.")
    else:
        print("Must have 0 active academic backlogs.")

print("=" * 45)