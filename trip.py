
"""Trip class for the Flight Trip Planner.

Author: Ali Tarom
Purpose: Store trip information and calculate trip costs.
Starter/Resources: Project 1 refactoring; Python Crash Course, Chapter 9.
Date: October, 2026
"""


class Trip:
    """Represent a planned trip."""

    def __init__(self, destination, flight_cost, hotel_cost, nights, activities):
        """Store the information for a trip."""
        self.destination = destination
        self.flight_cost = flight_cost
        self.hotel_cost = hotel_cost
        self.nights = nights
        self.activities = activities

    def calculate_total(self):
        """Return the combined flight and hotel costs."""
        return self.flight_cost + self.hotel_cost
