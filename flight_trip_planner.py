
"""Flight Trip Planner

Author: Ali Tarom
Purpose: Plan trips and calculate travel costs.
Starter/Resources: Project 1 and Python Crash Course
Date: October, 2026
"""

from trip import Trip
import json
from pathlib import Path

TRIPS_FILE = Path("trips.json")


def save_trips(trips):
    """Save trips to a JSON file."""
    trip_data = []

    for trip in trips:
        trip_data.append({
            "destination": trip.destination,
            "flight_cost": trip.flight_cost,
            "hotel_cost": trip.hotel_cost,
            "nights": trip.nights,
            "activities": trip.activities
        })

    with open(TRIPS_FILE, "w") as file:
        json.dump(trip_data, file, indent=4)


def load_trips():
    """Load saved trips from a JSON file."""
    if not TRIPS_FILE.exists():
        return []

    with open(TRIPS_FILE, "r") as file:
        trip_data = json.load(file)

    trips = []

    for data in trip_data:
        trip = Trip(
            data["destination"],
            data["flight_cost"],
            data["hotel_cost"],
            data["nights"],
            data["activities"]
        )
        trips.append(trip)

    return trips


def display_menu():
    """Display the main menu."""
    print()
    print("1. Add Trip")
    print("2. View Trip")
    print("3. Calculate Total")
    print("4. Remove Trip")
    print("5. Exit")



def add_trip(trips):
    """Get trip information and add it to the list."""
    destination = input("Enter your destination: ").strip()
    flight_cost = float(input("Enter flight cost: $"))
    hotel_cost = float(input("Enter hotel cost: $"))
    nights = int(input("Enter number of nights: "))
    activities = input("Enter an activity: ").strip()

    trip = Trip(
        destination,
        flight_cost,
        hotel_cost,
        nights,
        activities
    )

    trips.append(trip)
    print("Trip added successfully!")




def view_trips(trips):
    """Display all trips in the list."""
    if not trips:
        print("No trips have been added.")
        return

    for trip in trips:
        print()
        print("Trip Information")
        print("Destination:", trip.destination)
        print(f"Flight Cost: ${trip.flight_cost:.2f}")
        print(f"Hotel Cost: ${trip.hotel_cost:.2f}")
        print("Nights:", trip.nights)
        print("Activities:", trip.activities)



def calculate_trip_cost(trip):
    """Return the total cost of a trip."""
    return trip.calculate_total()


def calculate_totals(trips):
    """Display the total cost of each trip."""
    if not trips:
        print("No trips have been added.")
        return

    for trip in trips:
        total = calculate_trip_cost(trip)
        print(f"Total Trip Cost: ${total:.2f}")



def remove_trip(trips):
    """Remove a trip by destination."""
    if not trips:
        print("No trips have been added.")
        return

    destination = input("Enter the destination to remove: ").strip()

    for trip in trips:
        if trip.destination.lower() == destination.lower():
            trips.remove(trip)
            print("Trip removed successfully!")
            return

    print("Trip not found.")



def main():
    """Run the main program."""
    trips = load_trips()

    print("===== FLIGHT TRIP PLANNER =====")
    print("Plan your next trip!")

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_trip(trips)
            save_trips(trips)
        elif choice == "2":
            view_trips(trips)
        elif choice == "3":
            calculate_totals(trips)
        elif choice == "4":
            remove_trip(trips)
            save_trips(trips)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
