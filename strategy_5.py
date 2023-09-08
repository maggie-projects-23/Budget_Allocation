import numpy as np
import random
from ordered_subbattlefield_contribution import Largest, Second_and_Third_Largest

def Strategy_5(r,keep_playing, Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat):
    print(percent_contribution_cat)
    strat=strat
    budget=budget
    r=r
    Payoff_Bank=Payoff_Bank
    payoff_matrix=payoff_matrix

            
    (max_laws, max_reserves, max_community) = Largest(Payoff_Bank, payoff_matrix)
    (sec_max_laws, sec_max_reserves, sec_max_community\
           ,third_max_laws, third_max_reserves, third_max_community) = Second_and_Third_Largest(Payoff_Bank, payoff_matrix)   
        
    
    ##### Strategy 5 #####
    max_contribution=max(percent_contribution_cat[0], percent_contribution_cat[1], percent_contribution_cat[2])
    
                 
    ###  If two battlefields have equal max contributions, then throw error         
    if percent_contribution_cat[0]==percent_contribution_cat[1]==max_contribution\
        or percent_contribution_cat[0]==percent_contribution_cat[2]==max_contribution\
        or percent_contribution_cat[1]==percent_contribution_cat[2]==max_contribution:
            keep_playing="yes"
            print("Strategy 5 was played")
            print("Error: Two battlefields share the same max contributing value")
            return(strat, keep_playing)
    else:
        ### If all battlefields have equal contribution
        if percent_contribution_cat[0]== percent_contribution_cat[1]==percent_contribution_cat[2]:
            for j in range(3):
                for i in range(3):
                    strat[j][i]=budget[j]/3
        
        else:
            if percent_contribution_cat[0]==max_contribution:
                max_pos=0 #column with the most contribution is laws
            if percent_contribution_cat[1]==max_contribution:
                max_pos=1 #column with the most contribution is reserves
            if percent_contribution_cat[2]==max_contribution:
                max_pos=2 #column with the most contribution is community   
          ### If the max contributing battlefield > the sum of the other two's contribution
            if percent_contribution_cat[0]>percent_contribution_cat[1]+percent_contribution_cat[2]\
                or percent_contribution_cat[1]>percent_contribution_cat[0]+percent_contribution_cat[2]\
                or percent_contribution_cat[2]>percent_contribution_cat[0]+percent_contribution_cat[1]:
                    strat[0][max_pos]=budget[0]
                    strat[1][max_pos]=budget[1]
                    strat[2][max_pos]=budget[2]
          ### If the max contributing battlefield < the sum of the other two's contribution
            else:
                if max_contribution==percent_contribution_cat[0] and percent_contribution_cat[0]< percent_contribution_cat[1]+percent_contribution_cat[2]:
                    
                    ratio=percent_contribution_cat[1]/percent_contribution_cat[2]
                    for i in range(3):
                        community_strategy=budget[i]/(1+ratio)
                        strat[i][2]=community_strategy
                        strat[i][1]=ratio*community_strategy
                        
                if max_contribution==percent_contribution_cat[1] and percent_contribution_cat[1]< percent_contribution_cat[0]+percent_contribution_cat[2]:
                    
                    ratio=percent_contribution_cat[0]/percent_contribution_cat[2]
                    for i in range(3):
                        community_strategy=budget[i]/(1+ratio)
                        strat[i][2]=community_strategy
                        strat[i][0]=ratio*community_strategy
                
                if max_contribution==percent_contribution_cat[2] and percent_contribution_cat[2]< percent_contribution_cat[0]+percent_contribution_cat[1]:
                    
                    ratio=percent_contribution_cat[0]/percent_contribution_cat[1]
                    for i in range(3):
                        reserves_strategy=budget[i]/(1+ratio)
                        strat[i][1]=reserves_strategy
                        strat[i][0]=ratio*reserves_strategy
                                   
    
        keep_playing='no'             
        print("Strategy 5 was played")
        return(strat, keep_playing)
            
    
