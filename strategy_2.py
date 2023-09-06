import numpy as np
import random
from ordered_subbattlefield_contribution import Largest, Second_and_Third_Largest

def Strategy_2(r,keep_playing, Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat):

            
    (max_laws, max_reserves, max_community) = Largest(Payoff_Bank, payoff_matrix)
    (sec_max_laws, sec_max_reserves, sec_max_community\
           ,third_max_laws, third_max_reserves, third_max_community) = Second_and_Third_Largest(Payoff_Bank, payoff_matrix)   
        
 
    ##### Strategy 2 #####
    ### What to do if max and second max are the same
    if max_laws==sec_max_laws:
        keep_playing="yes"
        print("Strategy 2 was played")
        print("Error:Two sub-battlefields in Laws contain highest amount")
        return strat,keep_playing
    elif max_reserves==sec_max_reserves:
        keep_playing="yes"
        print("Strategy 2 was played")
        print("Error:Two sub-battlefields in Reserves contain highest amount")
        return strat,keep_playing
    elif max_community==sec_max_community:
        keep_playing="yes"
        print("Strategy 2 was played")
        print("Error:Two sub-battlefields in Community contain highest amount")
        return strat,keep_playing
        
    else:             
 
        for i in range(3):
            if max_laws==payoff_matrix[i][0]:
                max_laws_pos=i
                strat[i][0]=budget[i]
            if max_reserves==payoff_matrix[i][1]:
                max_reserves_pos=i
                strat[i][1]=budget[i]
            if max_community==payoff_matrix[i][2]:
                max_community_pos=i
                strat[i][2]=budget[i]
                
                
        if max_laws_pos==max_reserves_pos:
            share_pos=max_laws_pos
            ratio=percent_contribution_cat[0]/percent_contribution_cat[1]
            
            reserves_strategy=budget[share_pos]/(1+ratio)
            strat[share_pos][1]=reserves_strategy # amount of resources that go to reserves
            strat[share_pos][0]=ratio * reserves_strategy #amount of resources that go to laws
            
            for i in range(3):
                if i!= share_pos and i!=max_community_pos:
                    strat[i][0]=percent_contribution_cat[0]*budget[i] #amount of resources that go to laws
                    strat[i][1]=percent_contribution_cat[1]*budget[i] #amount of resources that go to reserves
                    strat[i][2]=percent_contribution_cat[2]*budget[i] # amount of resources that go to community
                    
            
        if max_laws_pos==max_community_pos:
            share_pos=max_laws_pos
            ratio=percent_contribution_cat[0]/percent_contribution_cat[2]
            
            community_strategy=budget[share_pos]/(1+ratio)
            strat[share_pos][2]=community_strategy # amount of resources that go to community
            strat[share_pos][0]=ratio * community_strategy #amount of resources that go to laws
            
            for i in range(3):
                if i!= share_pos and i!=max_reserves_pos:
                    strat[i][0]= percent_contribution_cat[0]*budget[i] #amount of resources that go to laws
                    strat[i][1]=percent_contribution_cat[1]*budget[i] #amount of resources that go to reserves
                    strat[i][2]=percent_contribution_cat[2]*budget[i] # amount of resources that go to community
                    
                    
            
        if max_reserves_pos==max_community_pos:
            share_pos=max_reserves_pos
            ratio=percent_contribution_cat[1]/percent_contribution_cat[2]
            
            community_strategy=budget[share_pos]/(1+ratio)
            strat[share_pos][2]=community_strategy # amount of resources that go to community
            strat[share_pos][1]=ratio * community_strategy #amount of resources that go to reserves
            
            for i in range(3):
                if i!=share_pos and i!=max_laws_pos:
                    strat[i][0]= percent_contribution_cat[0]*budget[i] #amount of resources that go to laws
                    strat[i][1]=percent_contribution_cat[1]*budget[i] #amount of resources that go to reserves
                    strat[i][2]=percent_contribution_cat[2]*budget[i] # amount of resources that go to community
            
            
        if max_laws_pos==max_reserves_pos==max_community_pos:
            for i in range(3):
                for j in range(3):
                    strat[i][j]= percent_contribution_cat[j]*budget[i] #amount of resources that go to laws
                    strat[i][j]=percent_contribution_cat[j]*budget[i] #amount of resources that go to reserves
                    strat[i][j]=percent_contribution_cat[j]*budget[i] # amount of resources that go to community

        keep_playing="no"
        print("Strategy 2 was played")
        return strat, keep_playing

  