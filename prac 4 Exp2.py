# Accept atmospheric status input from user
status_input = input("Enter atmospheric status (e.g., hot, humid, cold, freezing, normal): ")

# Normalize the input (lowercase and remove extra whitespace)
status = status_input.strip().lower()

# Process atmospheric status and determine hardware recommendations
print("\n" + "=" * 50)
print(f"{'SMART-HOME CLIMATE MONITORING SYSTEM':^50}")
print("=" * 50)
print(f" Atmospheric Status : {status_input.strip()}")
print("-" * 50)

if status in ["hot", "sweltering", "very hot"]:
    print(" Action Required    : TURN ON AC")
    print(" Recommendation     : Set target temperature to 22°C.")
elif status in ["humid", "muggy"]:
    print(" Action Required    : ACTIVATE DEHUMIDIFIER")
    print(" Recommendation     : Set humidity target to 45%.")
elif status in ["cold", "chilly", "freezing"]:
    print(" Action Required    : ACTIVATE HEATER")
    print(" Recommendation     : Set heating target to 24°C.")
elif status in ["normal", "comfortable", "optimal", "idle"]:
    print(" Action Required    : IDLE")
    print(" Recommendation     : Systems in standby mode. Climate optimal.")
else:
    print(" Action Required    : UNKNOWN ATMOSPHERIC STATUS")
    print(" Recommendation     : Invalid entry. Please enter hot, humid,")
    print("                      cold, freezing, or normal.")

print("=" * 50)