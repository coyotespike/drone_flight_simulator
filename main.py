#!/usr/bin/env python3

# main.py

import argparse
from battery_calculations import estimate_battery_capacity
from flight_time_calculations import calculate_flight_time
from forecasting import forecast

def main(amp_draw, desired_runtime_minutes, battery_weight, battery_capacity_wh, weight_without_battery, num_propellers):
    # Estimate the required battery capacity
    estimated_battery_capacity_mAh = estimate_battery_capacity(amp_draw, desired_runtime_minutes)
    print(f"Estimated battery capacity for {desired_runtime_minutes}-minute runtime: {estimated_battery_capacity_mAh:.2f} mAh")

    # Dummy data for forecasting (e.g., weight ratio or some other metric) and known_y (electrical power in watts)
    known_x = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50,
               0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.05]
    known_y = [288.46, 326.97, 365.45, 403.93, 442.43, 480.91, 519.40, 557.89,
               596.37, 634.85, 673.34, 711.82, 750.30, 788.80, 827.27, 865.76,
               904.25, 942.74, 981.20, 1019.72, 1058.18]  # Electrical power in watts

    # Input value for which to forecast W/prop (e.g., a specific weight ratio)
    x_value = 0.45  # Example input, can be adjusted as needed
    W_prop = forecast(x_value, known_x, known_y)

    # Calculate total weight and other parameters
    total_weight = battery_weight + weight_without_battery
    thrust_per_prop_hover = total_weight / num_propellers
    prop_efficiency = thrust_per_prop_hover / W_prop
    battery_energy_density = battery_capacity_wh / battery_weight

    # Calculate flight time
    flight_time = calculate_flight_time(
        Wbattery=battery_weight,
        sigma_battery=battery_energy_density,
        Wframe=weight_without_battery,
        prop_efficiency=prop_efficiency,
        num_propellers=num_propellers
    )

    # Output results
    print(f"Total Weight: {total_weight:.2f} g")
    print(f"Thrust/Prop @ Hover: {thrust_per_prop_hover:.2f} g")
    print(f"Estimated Flight Time: {flight_time * 60:.2f} minutes")  # Convert hours to minutes


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Drone Flight Time Estimator")
    parser.add_argument("--amp_draw", type=float, required=True, help="Average current draw in amps")
    parser.add_argument("--desired_runtime", type=float, required=True, help="Desired flight time in minutes")
    parser.add_argument("--battery_weight", type=float, required=True, help="Battery weight in grams")
    parser.add_argument("--battery_capacity_wh", type=float, required=True, help="Battery capacity in Wh")
    parser.add_argument("--weight_without_battery", type=float, required=True, help="Weight of the drone without the battery")
    parser.add_argument("--num_propellers", type=int, required=True, help="Number of propellers")

    args = parser.parse_args()

    # Run the main function with the specified parameters
    main(
        amp_draw=args.amp_draw,
        desired_runtime_minutes=args.desired_runtime,
        battery_weight=args.battery_weight,
        battery_capacity_wh=args.battery_capacity_wh,
        weight_without_battery=args.weight_without_battery,
        num_propellers=args.num_propellers
    )

# python3 main.py --amp_draw 25 --desired_runtime 15 --battery_weight 200 --battery_capacity_wh 28.86 --weight_without_battery 0 --num_propellers 4
