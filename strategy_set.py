import numpy as np
import random
from strategy_2 import Strategy_2
from strategy_3 import Strategy_3
from strategy_4 import Strategy_4




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
    ## If all three battlefields share the max sub-battlefields, then the resources are distributed accouding
    ## to the contribution each battlefield makes
    
    Strategy_2(r,Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat)
 
    # =============================================================================
    # =============================================================================
    

    # =============================================================================
    # =============================================================================   
    ##### Strategy 3 #####
    ## Allocate resources of a particular type to the sub-battlefields that do not contribute the most
    ## that way they can win the most payoff from that battlefield without getting the most con-
    ## tributing sub-battlefield. If two battlefields share the same sub-battlefield as the second(third)
    ## most contributing then split the resources proportionally to how much they contribute similar
    ## to 1. If all three share the same second(third) contributing sub-battlefield, distribute the ac-
    ## cording the the contribution of the battlefield. If one battlefield shares a second contributing
    ## sub-battlefield with a third contributing sub-battlefield in a different sub-battle field, then all
    ## the resources go to the battlefield that has the second contributing sub-battlefield
    ## If one battlefields have identical second and third most contributing subbattlefields, then one is 
    ## chosen to be second and one third and proceedure it carried out same as above
    ## If two battlefields have identical second and third most contributing subbattlefields, then this strategy 
    ## cannot be used. If the most contributing subbattlefield and the second are identical, then this stragegy 
    ## cannot be used
    ## If all three battlefields share second(third) sub-battlefields, then the resources are distributed accouding
    ## to the contribution each battlefield makes
    Strategy_3(r,Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat)
    # =============================================================================
    # =============================================================================
        
    
    # =============================================================================
    # =============================================================================   
    ##### Strategy 4 #####
    ## Similar to Strategy 3. Allocate resources of a particular type to the sub-battlefields that do not contribute the most
    ## but this time if two battlefields share a second(third)sub-battlefield, then the majority (90-
    ## 95%) goes the the battlefield that contributes the most while a minority (5-10%) go to the
    ## other
    ## If all three battlefields share second(third) sub-battlefields, then the battlefield with the most 
    ## contribution gets the larger percentage and the second most contribution get the smaller percentage 
    ## while the least contributing gets 0
    ##If one battlefields have identical second and third most contributing subbattlefields, then one is 
    ## chosen to be second and one third and proceedure it carried out same as above
    ## If two battlefields have identical second and third most contributing subbattlefields, then this strategy 
    ## cannot be used. If the most contributing subbattlefield and the second are identical, then this stragegy 
    ## cannot be used
    Strategy_4(r,Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat)
    # =============================================================================
    # =============================================================================
    
    print(r)            
    print("The strategy matrix is")
    print(strat)
        
        

        
Strategy([10,9,21],np.array([[8.25, 9, 16.5 ],[3, 15, 5.5],[3.75, 6, 33]]), 100)














