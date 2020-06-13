"""
Author: Agosh Saini
Date: April 08, 2020

Two Dimensional Random Walk:
"""
#Dependencies
import numpy as np
import random
import matplotlib.pyplot as plt

'''Global Variables'''
#Run variables control the number of movements per molecules and number of molecules
total_runs = 10000
runs_per_mol = 100

#Delta variables are the smallest movement a molecule can make
delta_x = 0.1
delta_y = 0.1

'''Functions'''

#This function sees how a molecule can randomly move from a central
#point to a random point
def random_walk(runs_per_mol, total_runs, delta_x, delta_y):
    # these are the arrays use to track the cordinates of molecules in a system
    x,y = np.zeros(total_runs, dtype=float), np.zeros(total_runs, dtype=float)
    
    #This for loop calculates the changes in X plane
    for i in range(total_runs):
        
        for j in range(runs_per_mol):
            #integers -1,0,1 result it no movement in any direction
            direction = random.randint(-2, 2) 
            if direction == -2:
                x[i] += -1*delta_x
            elif direction == 2:
                x[i] += 1*delta_x 
                
    #This for loop calculates the changes in Y plane            
    for i in range(total_runs):
       
        for j in range(runs_per_mol):
            #integers -1,0,1 result it no movement in any direction
            direction = random.randint(-2, 2)
            if direction == -2:
                y[i] += -1*delta_y
            elif direction == 2:
                y[i] += 1*delta_y
    
    x_reshaped, y_reshaped = x.reshape(total_runs, 1), y.reshape(total_runs, 1)
    
    return x_reshaped, y_reshaped


'''Plotting'''
x, y = random_walk(runs_per_mol, total_runs, delta_x, delta_y)

plt.scatter(x, y, s=2)
plt.title(str(total_runs) + " Gas Molecules After " + str(runs_per_mol) + " Movements")
plt.xlabel('x')
plt.ylabel('y')

#limiting the axis to -5 to 5 in X and Y planes to better see diffusion
plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.savefig(str(total_runs)+"_molecules_after_"+str(runs_per_mol)+"_movements.png")

plt.show()


        

        
        
        
