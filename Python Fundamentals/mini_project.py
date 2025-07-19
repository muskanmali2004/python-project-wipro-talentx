print("===== Mini Project: Ride on Miles =====\n")

# Taking input from the user
vehicle = input("Enter vehicle type (e.g., Bike/Car): ")
speed = float(input("Enter average speed of vehicle in km/h: "))
time = float(input("Enter time travelled in hours: "))

# Calculating distance
distance = speed * time

# Output result
print(f"\n🚗 You travelled {distance:.2f} kilometers in a {vehicle} at {speed} km/h for {time} hours.")

# Optional: Suggest fuel usage (basic logic)
if distance < 50:
    print("It was a short ride.")
elif 50 <= distance <= 200:
    print("It was a medium distance ride.")
else:
    print("It was a long ride. Make sure to take breaks!")


