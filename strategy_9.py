import numpy as np
import random
from ordered_subbattlefield_contribution import Largest, Second_and_Third_Largest

def Strategy_9(r, keep_playing, Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat):
    
    strat=strat
    budget=budget
    r=r
    Payoff_Bank=Payoff_Bank
    payoff_matrix=payoff_matrix

    
    ##### Strategy 9 ##### 
    max_percent=max(percent_contribution_cat[0], percent_contribution_cat[1]) #exclude community because we are defintely allocating resources there
    if percent_contribution_cat[0]==percent_contribution_cat[1]==percent_contribution_cat[2]:
          for j in range(3):
              for i in range(3):
                  strat[j][i]=budget[j]/3
    else:   
        if percent_contribution_cat[0]==percent_contribution_cat[1]==max_percent:
            r=random.randint(0, 100)
            if r<50:
                max_pos=0
            else:
                max_pos=1
        else:
            if percent_contribution_cat[0]==max_percent:
                max_pos=0
            if percent_contribution_cat[1]==max_percent:
                max_pos=1
                        
                        
    ratio=percent_contribution_cat[max_pos]/percent_contribution_cat[2]
    
    for i in range(3):
        community_strategy=budget[i]/(1+ratio)
        strat[i][2]=community_strategy
        strat[i][max_pos]=ratio*community_strategy
    
    keep_playing='no'        
    print("Strategy 9 was played")
    return(strat, keep_playing)
            
                
                
            

        
    
    
    
    
    
    
    ### What to do if second and third most contributing are the same