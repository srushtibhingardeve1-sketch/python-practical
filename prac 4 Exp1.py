# Accept status input from user
status_input = input("Enter order status (e.g., pending, shipped, out for delivery, delivered): ")

# Normalize the input (lowercase and remove extra whitespace)
status = status_input.strip().lower()

# Process status and output customized logistics update message
print("\n" + "=" * 50)
print(f"{'LOGISTICS TRACKING SYSTEM':^50}")
print("=" * 50)
print(f" Raw Input Status : {status_input.strip()}")
print("-" * 50)

if status == "pending":
    print(" Status Message   : ORDER RECEIVED")
    print(" Details          : Your order has been placed and is currently")
    print("                    being processed in our warehouse.")
elif status == "shipped":
    print(" Status Message   : IN TRANSIT")
    print(" Details          : Your package has left the facility and is on")
    print("                    its way to the local distribution center.")
elif status == "out for delivery":
    print(" Status Message   : OUT FOR DELIVERY")
    print(" Details          : The courier has loaded your package and will")
    print("                    attempt delivery today.")
elif status == "delivered":
    print(" Status Message   : DELIVERED")
    print(" Details          : Package delivered successfully. Please check")
    print("                    your doorstep or mailroom.")
elif status == "cancelled":
    print(" Status Message   : ORDER CANCELLED")
    print(" Details          : This order has been cancelled. A refund will")
    print("                    be issued if payment was processed.")
else:
    print(" Status Message   : UNKNOWN STATUS")
    print(" Details          : Invalid keyword entered. Valid statuses: pending,")
    print("                    shipped, out for delivery, delivered, cancelled.")

print("=" * 50)