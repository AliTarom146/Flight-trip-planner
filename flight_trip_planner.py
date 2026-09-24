"""Flight Trip Planner

Author: Ali Tarom
Purpose: A simple program for planning a trip and calculating travel costs.
Date: September 2026
"""

print("===== FLIGHT TRIP PLANNER =====")
print("Plan your next trip!")

trips = []

trip = {
    "destination": input("Enter your destination: "),
    "flight_cost": float(input("Enter flight cost: $")),
    "hotel_cost": float(input("Enter hotel cost: $")),
    "nights": int(input("Enter number of nights: ")),
    "activities": input("Enter an activity: "),
}

trips.append(trip)

print()
print("Trip Information")
print("Destination:", trip["destination"])
print("Flight Cost: $", trip["flight_cost"])
print("Hotel Cost: $", trip["hotel_cost"])
print("Nights:", trip["nights"])
print("Activities:", trip["activities"])