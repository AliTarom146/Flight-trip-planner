"""Flight Trip Planner

Author: Ali Tarom
Purpose: A simple program for planning a trip and calculating travel costs.
Date: September 2026
"""

print("===== FLIGHT TRIP PLANNER =====")
print("Plan your next trip!")

trips = []

while True:
    print()
    print("1. Add Trip")
    print("2. View Trip")
    print("3. Calculate Total")
    print("4. Remove Trip")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        trip = {
            "destination": input("Enter your destination: "),
            "flight_cost": float(input("Enter flight cost: $")),
            "hotel_cost": float(input("Enter hotel cost: $")),
            "nights": int(input("Enter number of nights: ")),
            "activities": input("Enter an activity: ")
        }

        trips.append(trip)
        print("Trip added successfully!")

    elif choice == "2":
        if len(trips) == 0:
            print("No trips have been added.")
        else:
            for trip in trips:
                print()
                print("Trip Information")
                print("Destination:", trip["destination"])
                print("Flight Cost: $", trip["flight_cost"])
                print("Hotel Cost: $", trip["hotel_cost"])
                print("Nights:", trip["nights"])
                print("Activities:", trip["activities"])

    elif choice == "3":
        if len(trips) == 0:
           print("No trips have been added.")
        else:
            for trip in trips:
                total = trip["flight_cost"] + trip["hotel_cost"]
                print("Total Trip Cost: $", total)

    elif choice == "4":
        print("Remove Trip selected")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")