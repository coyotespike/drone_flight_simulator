# Drone Flight Time

Based on [this spreadsheet](https://docs.google.com/spreadsheets/d/1G9zeRnEKNyZKFfD0QQFb3an53sGvwxXs6VtPaq8duSM/edit#gid=0), from this stellar [Tyto Robotics article](https://www.tytorobotics.com/blogs/articles/how-to-increase-drone-flight-time-and-lift-capacity).

Basically we are trying to represent these formulas from the article:

1. **Battery Capacity (Wh)**:
   - $E_{\text{battery}} = \sigma_{\text{battery}} \times W_{\text{battery}}$
   - Where:
     - $E_{\text{battery}}$ is the battery capacity in watt-hours.
     - $\sigma_{\text{battery}}$ is the energy density in watt-hours per gram.
     - $W_{\text{battery}}$ is the weight of the battery in grams.

2. **Power Calculation (Total Power in Watts)**:
   - $P_{\text{total}} = \frac{W_{\text{drone}}}{\text{prop\_efficiency}}$
   - Where:
     - $P_{\text{total}}$ is the total power consumption in watts.
     - $W_{\text{drone}}$ is the total weight of the drone, including the battery.
     - $\text{prop\_efficiency}$ is the propeller efficiency in grams per watt.

3. **Flight Time (Hours)**:
   - $\text{Flight Time} = \frac{E_{\text{battery}}}{P_{\text{total}}}$
   - or $$FT = \frac{\sigma_{battery} * W_{battery}}{W_{frame} + W_{battery}} * prop_{efficiency} \left(\frac{W_{frame} + W_{battery}}{NumberOfPropeller}\right)$$

   - This equation gives the flight time in hours based on the battery capacity and the total power consumption.

4. **Alternative Power Calculation Using Number of Propellers**:
   - $P_{\text{total}} = \frac{W_{\text{drone}} / \text{num\_propellers}}{\text{prop\_efficiency}}$
   - Where:
     - $\text{num\_propellers}$ is the number of propellers.

5. **Runtime Calculation (Minutes)**:
   - $\text{Runtime} = \left(\frac{\text{Battery Capacity (mAh)}}{\text{Amp Draw (A)} \times 1000}\right) \times 60$
   - This equation calculates the runtime in minutes based on the battery capacity in mAh and the average current draw in amps.

# Zero Weight Experiment
- How long could a drone fly, if only the battery had weight, and the frame/motors were weightless?
- Obviously we want to add weight, the payload is the point. But because drone flight time is limited by power (duh), we can focus on the fundamental limitation with this thought experiment.
- This is kind of an unanswerable question, because as the battery gets heavier, we need larger/slower/more efficient propellers to carry it. We really can't isolate the batteries purely.
- Still, I would like to come up with an answer like so: two AA batteries could fly for xx, medium drone battery for xx.
- As batteries improve, so will drones. Drones benefit from better batteries and better AI - neither field shows signs of slowing down so drones are just a beautiful area to build in.

### Command to test DJI's Matrice 300 battery, the TB60
- Capacity: 5935 mAh (5.935 Ah)
- Voltage: 52.8V (12S configuration)
- Energy: 274 Wh
- Battery Type: LiPo 12S
- Weight: 1350g (1.35 kg)

`python3 main.py --amp_draw 25 --desired_runtime 15 --battery_weight 1350 --battery_capacity_wh 274 --weight_without_battery 0 --num_propellers 4`

Yields:

```
Estimated battery capacity for 15.0-minute runtime: 6250.00 mAh
Total Weight: 1350.00 g
Thrust/Prop @ Hover: 337.50 g
Estimated Flight Time: 27.57 minutes
```

With two of these battery the Matrice 300 RTK can fly 55 minutes with no payload, so this appears approximately correct.

### Command to test high-speed racing battery
- Capacity: 1300 mAh
- Voltage: 22.v
- Energy: 28.86 Wh
- Weight: 200g

`python3 main.py --amp_draw 25 --desired_runtime 15 --battery_weight 200 --battery_capacity_wh 28.86 --weight_without_battery 0 --num_propellers 4`

```
Estimated battery capacity for 15.0-minute runtime: 6250.00 mAh
Total Weight: 200.00 g
Thrust/Prop @ Hover: 50.00 g
Estimated Flight Time: 2.90 minutes
```

Online reviews report 4-5 minutes of flight time with this battery (Tattu), so this appears to underestimate a bit.
