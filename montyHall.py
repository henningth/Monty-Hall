# -*- coding: utf-8 -*-
"""
Monty Hall simulator

Assumes that the door which the car is behind is random and independent in each game

Henning Thomsen, 15.02.2017

"""

# Imports
import numpy as np

# Parameters
reps = 1000 # Repetitions of M.H.

# Variables
succStay = 0
succSwitch = 0
doors = np.arange(0,3)
carId = np.random.randint(0,3,reps+1) # Door ID of the car

# Main simulation loop
for i in range(0,reps):
    
    # Contestant chooses a door
    doorChoice = np.random.choice(doors)
    
    # Strategy 1: Always stay
    if carId[i] == doorChoice:
        succStay = succStay + 1
    
    # Strategy 2: Always switch   
    hostChoices = np.setdiff1d(doors, carId[i]) # The doors having goats behind them
    
    hostChoices = np.setdiff1d(hostChoices, doorChoice) # Host does'nt open chosen door
    
    hostChoice = np.random.choice(hostChoices) # Host reveals one goat door
    
    switchChoices = np.setdiff1d(doors, hostChoice) # Remove host' choice
    
    switchChoices = np.setdiff1d(switchChoices, doorChoice) # We switch, so inital choice is removed

    newDoorChoice = np.random.choice(switchChoices)
    if carId[i] == newDoorChoice:
        succSwitch = succSwitch + 1
        
# Print results
successStay = float(succStay)/reps*100
successSwitch = float(succSwitch)/reps*100
print "Success Probability of not switching: %.2f pct.\n" % successStay
print "Success Probability of switching: %.2f pct.\n" % successSwitch