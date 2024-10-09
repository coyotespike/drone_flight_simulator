#!/usr/bin/env python3

import numpy as np

def forecast(x, known_x, known_y):
    """
    Perform linear regression to forecast the value of W/prop based on known data.
    """
    # Perform linear regression to find the slope and intercept
    slope, intercept = np.polyfit(known_x, known_y, 1)
    # Calculate the forecasted value
    return slope * x + intercept
