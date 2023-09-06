import numpy as np
import random
from strategy_2 import Strategy_2
from strategy_3 import Strategy_3
from strategy_4 import Strategy_4
from strategy_5 import Strategy_5
from strategy_8 import Strategy_8
from strategy_9 import Strategy_9




def Strategy(r,budget, payoff_matrix, Payoff_Bank):
    
    keep_playing="yes"
    
    strat=np.zeros((3,3)) ####                 Laws    Reserves    Commnity 
                          #### Monetary     [                               ]
                          #### Non-Monetary [                               ]
                          #### People       [                               ]
    
    
    #Gives percentage (in decimal form) of how much the Laws, Reserves, and Community bettlefield contribute
    percent_contribution_cat=np.array(np.sum(payoff_matrix, axis=0)/Payoff_Bank)
    
    
    # =============================================================================
    # =============================================================================   
    ##### Strategy 1 #####
    ## Distribute all respectuve resources evenly across all corresponding sub-battlefields
    if r>0 and r<=11:
        for j in range(3):
            for i in range(3):
                strat[j][i]=budget[j]/3
        keep_playing ='no'
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
    
    ## Distribute all respectuve resources evenly across all corresponding sub-battlefields
    
    if r>11 and r<=22:
        strat, keep_playing =Strategy_2(r,keep_playing,Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat)
 
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
   
    if r>22 and r<=33: 
        strat, keep_playing = Strategy_3(r, keep_playing, Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat)
        
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
    
    if r>33 and r<=44: 
        strat, keep_playing = Strategy_4(r, keep_playing, Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat)
    # =============================================================================
    # =============================================================================
    
    
    # =============================================================================
    # =============================================================================   
    ##### Strategy 5 #####
    ## If the payoff of the battlefield with the most contribution is greater than the sum of the con-
    ## tributions from the two remaining battlefields, then allocate all resources of all types to the
    ## battlefield that contributes the most.
    ##
    ## If the payoff of the battlefield with the most contribution is less than the sum of the contri-
    ## butions from the two remaining battlefields, then split all resources proportionally (same as
    ## in 1.) of all types to the two battlefields that do not contribute the most
    ##
    ## Cannot do strategy if two battlefields share the same max contribution value
    ##
    ## If all battefields have equal weight, distribute evenly.
    
    if r>44 and r<=55: 
        strat, keep_playing = Strategy_5(r, keep_playing, Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat)
    # =============================================================================
    # =============================================================================
    
    
    # =============================================================================
    # =============================================================================   
    ######Strategy 6
    ## Distribute resources accordingly to how much contribution the battlefield holds• 
    ## If Laws hold 15%, Reserves 30%, and Community 55%, then 15% of the Monetary, Non-
    ## Monetary, and People budgets would go to Laws, 30% of the Monetary, Non-Monetary,
    ## and People budgets would go to Reserves, etc
    
    if r>55 and r<=66: 
        for i in range(3):
            for j in range (3):
                strat[i][j]=percent_contribution_cat[j]*budget[i]
        keep_playing ='no'        
        print("Strategy 6 was played")
    # =============================================================================
    # =============================================================================
    
    
    # =============================================================================
    # =============================================================================   
    ######Strategy 7
    ## Always allocate all resources to the Community because it drives the game
    
    if r>66 and r<=77: 
        for i in range(3):
            strat[i][2]=budget[i]
        keep_playing ='no'        
        print("Strategy 7 was played")
    # =============================================================================
    # =============================================================================
    
    
    # =============================================================================
    # =============================================================================   
    ######Strategy 8
    ## Allocate resources proportionally to the the top two contributing battlefields.
    ## If the second and third contributing battlefields have the same contribution, then 
    ## randomly choose one to be labeled as the second.
    
    if r>77 and r<=88: 
        strat, keep_playing = Strategy_8(r, keep_playing, Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat)
    # =============================================================================
    # =============================================================================
    
    
    # =============================================================================
    # =============================================================================   
    ######Strategy 9
    ## Allocate resources proportionally to the the top two contributing battlefields.
    ## If the second and third contributing battlefields have the same contribution, then 
    ## randomly choose one to be labeled as the second.
    
    if r>88 and r<=99: 
       strat, keep_playing = Strategy_9(r, keep_playing, Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat)
    # =============================================================================
    # =============================================================================
    
    
    
    # print(r)            
    # print("The strategy matrix is")
    # print(strat)
    return(strat, keep_playing)
        














