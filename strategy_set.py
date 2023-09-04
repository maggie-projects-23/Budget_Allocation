import numpy as np
import random
from strategy_3 import Strategy_3
from strategy_2 import Strategy_2



def Strategy(budget, payoff_matrix, Payoff_Bank):
    
    
    strat=np.zeros((3,3)) ####                 Laws    Reserves    Commnity 
                          #### Monetary     [                               ]
                          #### Non-Monetary [                               ]
                          #### People       [                               ]
    r=random.randint(0,100)
    
    print("The payoff matrix is")
    print(payoff_matrix)
    
    
    #Gives percentage (in decimal form) of how much the Laws, Reserves, and Community bettlefield contribute
    percent_contribution_cat=np.array(np.sum(payoff_matrix, axis=1)/Payoff_Bank)
    
    
    # =============================================================================
    # =============================================================================   
    ##### Strategy 1 #####
    ## Distribute all respectuve resources evenly across all corresponding sub-battlefields
    if r>0 and r<=10:
        for j in range(3):
            for i in range(3):
                strat[j][i]=budget[j]/3
        print("Strategy 1 was played")
    # =============================================================================
    # =============================================================================
                

    # =============================================================================
    # =============================================================================
    ##### Strategy 2 #####
    ## allocate all resources of a particular type to the sub-battlefield that contributes the post
    ## payoff for that battlefield. If the same sub-battlefield type contributes the most in two different
    ## battlefields, then the resources are split according to how much one battlefield contributes that then other 
    ## If the max sub-battlefield had the same payoff as another sub-battlefield in the same battlefield then this 
    ## strategy cannot be used
    
    Strategy_2(r,Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat)
 
    # =============================================================================
    # =============================================================================
    

    # =============================================================================
    # =============================================================================   
    ##### Strategy 3 #####
    ## Distribute all respectuve resources evenly across all corresponding sub-battlefields
    Strategy_3(r,Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat)
    # =============================================================================
    # =============================================================================
        
                
    print("The strategy matrix is")
    print(strat)
        
        

        
Strategy([10,9,21],np.array([[3,9,22],[3,15,16.5], [9, 6, 16.5]]), 100)














