# -*- coding: utf-8 -*-
"""
Monty Hall simulator

Assumes that the door which the car is behind is random and independent in each game

The player switches door with probability p.

Henning Thomsen, 16.02.2017

"""

# Imports
import matplotlib.pyplot as plt
import numpy as np

# Parameters
reps = 100000 # Simulation repetitions
probs = 10 # Distinct probabilities

# Variables
maxDoors = 16
doorStep = 3
numDoorVec = np.arange(3,maxDoors,doorStep)
success = np.zeros((np.size(numDoorVec,0),probs, reps))       # Matrix holding indicator vars. of success
pVec = np.linspace(0.0, 1.0, probs)     # Probability of switching
colorVec = np.array(['r', 'b', 'g', 'k', 'm', 'c', 'y'])

dIdx = 0 # door index

# Iterate over number of doors
for numDoors in numDoorVec:

    pIdx = 0 # probability index
    
    doors = np.arange(0,numDoors) # Possible door choices
    carId = np.random.randint(0,numDoors,reps+1)   # Door ID of the car

    # Iterate over probability of switching
    for p in pVec:
        
        # Main simulation loop
        for i in range(0,reps):
            
            # Contestant chooses a door
            doorChoice = np.random.choice(doors)
            
            # Host reveals door   
            hostChoices = np.setdiff1d(doors, carId[i]) # The doors having goats behind them
            
            hostChoices = np.setdiff1d(hostChoices, doorChoice) # Host does'nt open chosen door
            
            hostChoice = np.random.choice(hostChoices, numDoors-2, replace=False) # Host reveals all but one goat door
            
            switchChoices = np.setdiff1d(doors, hostChoice) # Remove host' choices
            
            switchChoices = np.setdiff1d(switchChoices, doorChoice) # We switch, so inital choice is removed
            
            if np.random.rand(1) >= p: # Stay
                
                newDoorChoice = doorChoice
                            
            else: # Switch
            
                newDoorChoice = np.random.choice(switchChoices)
    
            if carId[i] == newDoorChoice:
                success[dIdx,pIdx,i] = success[dIdx,pIdx,i] + 1
                    
        pIdx = pIdx + 1
        
    dIdx = dIdx + 1
    
# Average results
successVec = np.mean(success, 2)

# Plot results
plt.axis([0,1,0,1])
for i in np.arange(0,np.size(numDoorVec,0)):
    j = doorStep*(i+1)
    plt.plot(pVec, successVec[i,:], colorVec[i], label="doors={0}".format(j))
plt.legend(loc="upper left")
plt.xlabel('Prob. of switching')
plt.ylabel('Prob. of winning car')
plt.title('Monty Hall, max. %g doors, %g repetitions' % (int(maxDoors-1), reps))
plt.grid()
plt.show()