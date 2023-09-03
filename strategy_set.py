import numpy as np
import random


def Strategy(budget):
    
    strat=np.zeros((3,3)) ####                 Laws    Reserves    Commnity 
                          #### Monetary     [                               ]
                          #### Non-Monetary [                               ]
                          #### People       [                               ]
    r=random.randint(0,100)
    
    ##### Strategy 1 #####
    ## Distribute all respectuve resources evenly across all corresponding sub-battlefields
    if r>0 and r<=100:
        for j in range(3):
            for i in range(3):
                strat[j][i]=budget[j]/3
        print(strat)
        
        
        
        
Strategy([10,9,21])