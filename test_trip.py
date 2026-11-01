"""Tests for the Trip class.

Author: Ali Tarom
Purpose: Test trip information and cost calculations.
"""

from trip import Trip
from flight_trip_planner import get_float_input, get_int_input


def test_trip_information():
    """Check that trip information is stored correctly."""
    trip = Trip("Paris", 800, 500, 5, "Visit museums")

    assert trip.destination == "Paris"
    assert trip.flight_cost == 800
    assert trip.hotel_cost == 500
    assert trip.nights == 5
    assert trip.activities == "Visit museums"


def test_calculate_total():
    """Check that the total trip cost is calculated correctly."""
    trip = Trip("London", 700, 400, 4, "Sightseeing")

    assert trip.calculate_total() == 1100


def test_calculate_total_with_zero_cost():
    """Check that a trip with no costs returns zero."""
    trip = Trip("Home", 0, 0, 1, "Relaxing")

    assert trip.calculate_total() == 0


def test_get_float_input(monkeypatch):
    """Check that invalid prices are rejected."""
    inputs = iter(["abc", "-50", "125.50"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))

    result = get_float_input("Enter flight cost: $")

    assert result == 125.50


def test_get_int_input(monkeypatch):
    """Check that invalid night counts are rejected."""
    inputs = iter(["three", "-2", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))

    result = get_int_input("Enter number of nights: ")

    assert result == 5
