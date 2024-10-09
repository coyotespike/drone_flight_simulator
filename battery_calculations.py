#!/usr/bin/env python3

def estimate_battery_capacity(amp_draw, desired_runtime_minutes):
    """
    Estimate the required battery capacity (in mAh) for a given average amp draw
    and desired runtime.
    """
    battery_capacity_ah = (amp_draw * desired_runtime_minutes) / 60
    return battery_capacity_ah * 1000  # Convert to mAh
