# Drone Flight Time

Based on [this spreadsheet](https://docs.google.com/spreadsheets/d/1G9zeRnEKNyZKFfD0QQFb3an53sGvwxXs6VtPaq8duSM/edit#gid=0), from this stellar [Tyto Robotics article](https://www.tytorobotics.com/blogs/articles/how-to-increase-drone-flight-time-and-lift-capacity).

Basically we are trying to represent these formulas from the article:

1. **Battery Capacity (Wh)**:
   \[
   E_{\text{battery}} = \sigma_{\text{battery}} \times W_{\text{battery}}
   \]
   Where:
   - \( E_{\text{battery}} \) is the battery capacity in watt-hours.
   - \( \sigma_{\text{battery}} \) is the energy density in watt-hours per gram.
   - \( W_{\text{battery}} \) is the weight of the battery in grams.

2. **Power Calculation (Total Power in Watts)**:
   \[
   P_{\text{total}} = \frac{W_{\text{drone}}}{\text{prop\_efficiency}}
   \]
   Where:
   - \( P_{\text{total}} \) is the total power consumption in watts.
   - \( W_{\text{drone}} \) is the total weight of the drone, including the battery.
   - \(\text{prop\_efficiency}\) is the propeller efficiency in grams per watt.

3. **Flight Time (Hours)**:
   \[
   \text{Flight Time} = \frac{E_{\text{battery}}}{P_{\text{total}}}
   \]
   This equation gives the flight time in hours based on the battery capacity and the total power consumption.

4. **Alternative Power Calculation Using Number of Propellers**:
   \[
   P_{\text{total}} = \frac{W_{\text{drone}} / \text{num\_propellers}}{\text{prop\_efficiency}}
   \]
   Where:
   - \(\text{num\_propellers}\) is the number of propellers.

5. **Runtime Calculation (Minutes)**:
   \[
   \text{Runtime} = \left(\frac{\text{Battery Capacity (mAh)}}{\text{Amp Draw (A)} \times 1000}\right) \times 60
   \]
   This equation calculates the runtime in minutes based on the battery capacity in mAh and the average current draw in amps.


# Zero Weight Experiment
- How long could a drone fly, if only the battery had weight, and the frame/motors were weightless?
- Obviously we want to add weight, the payload is the point. But because drone flight time is limited by power (duh), we can focus on the fundamental limitation with this thought experiment.
- This is kind of an unanswerable question, because as the battery gets heavier, we need larger/slower/more efficient propellers to carry it. We really can't isolate the batteries purely.
- Still, I would like to come up with an answer like so: two AA batteries could fly for xx, medium drone battery for xx.
- As batteries improve, so will drones. Drones benefit from better batteries and better AI - neither field shows signs of slowing down so drones are just a beautiful area to build in.
