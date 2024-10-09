#!/usr/bin/env python3

def calculate_flight_time(Wbattery, sigma_battery, Wframe, prop_efficiency, num_propellers):
    # Calculate Ebattery (battery capacity in Wh)
    Ebattery = sigma_battery * Wbattery

    # Total drone weight
    Wdrone = Wframe + Wbattery

    # Calculate power based on total weight and propeller efficiency
    Power = (Wdrone / num_propellers) / prop_efficiency

    # Calculate flight time in hours
    FlightTime = Ebattery / Power

    return FlightTime
