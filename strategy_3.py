import numpy as np
import random
from ordered_subbattlefield_contribution import Largest, Second_and_Third_Largest

def Strategy_3(r, keep_playing, Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat):
    
    strat=strat
    budget=budget
    r=r
    Payoff_Bank=Payoff_Bank
    payoff_matrix=payoff_matrix

            
    (max_laws, max_reserves, max_community) = Largest(Payoff_Bank, payoff_matrix)
    (sec_max_laws, sec_max_reserves, sec_max_community\
           ,third_max_laws, third_max_reserves, third_max_community) = Second_and_Third_Largest(Payoff_Bank, payoff_matrix)   
        
    
    ##### Strategy 3 ##### 
    if sec_max_laws==third_max_laws and sec_max_reserves==third_max_reserves:
        keep_playing="yes"
        print("Strategy 3 was played")
        print("Error: More than one battlefield has identical second and third sub-battlefield payoffs")
        return strat,keep_playing
    elif sec_max_laws==third_max_laws and sec_max_community==third_max_community:
        keep_playing="yes"
        print("Strategy 3 was played")
        print("Error: More than one battlefield has identical second and third sub-battlefield payoffs")
        return strat,keep_playing
    elif sec_max_reserves==third_max_reserves and sec_max_community==third_max_community:
        keep_playing="yes"
        print("Strategy 3 was played")
        print("Error: More than one battlefield has identical second and third sub-battlefield payoffs")
        return strat,keep_playing
    elif sec_max_laws==max_laws or sec_max_reserves==max_reserves or sec_max_community==max_community:
        keep_playing="yes"
        print("Strategy 3 was played")
        print("Error: Second sub-battlefield has same contribution as max sub-battlefield")
        return strat,keep_playing
    else:
        for i in range(3):
            if sec_max_laws==payoff_matrix[i][0]:
                sec_max_laws_pos=i
                strat[i][0]=budget[i]
            if sec_max_reserves==payoff_matrix[i][1]:
                sec_max_reserves_pos=i
                strat[i][1]=budget[i]
            if sec_max_community==payoff_matrix[i][2]:
                sec_max_community_pos=i
                strat[i][2]=budget[i]
                
            if third_max_laws==payoff_matrix[i][0]:
                third_max_laws_pos=i
                strat[i][0]=budget[i]
            if third_max_reserves==payoff_matrix[i][1]:
                third_max_reserves_pos=i
                strat[i][1]=budget[i]
            if third_max_community==payoff_matrix[i][2]:
                third_max_community_pos=i
                strat[i][2]=budget[i] 
        
        if sec_max_laws != third_max_laws and sec_max_reserves != third_max_reserves and\
             sec_max_community!= third_max_community:
       
            if sec_max_laws_pos==sec_max_reserves_pos:
                share_pos=sec_max_laws_pos
                ratio=percent_contribution_cat[0]/percent_contribution_cat[1]
                
                reserves_strategy=budget[share_pos]/(1+ratio)
                strat[share_pos][1]=reserves_strategy # amount of resources that go to reserves
                strat[share_pos][0]=ratio * reserves_strategy #amount of resources that go to laws
                
                if share_pos==third_max_community_pos:
                    strat[share_pos][2]=0
                        
                
            if sec_max_laws_pos==sec_max_community_pos:
                share_pos=sec_max_laws_pos
                ratio=percent_contribution_cat[0]/percent_contribution_cat[2]
                
                community_strategy=budget[share_pos]/(1+ratio)
                strat[share_pos][2]=community_strategy # amount of resources that go to community
                strat[share_pos][0]=ratio * community_strategy #amount of resources that go to laws
                
                if share_pos==third_max_reserves_pos:
                    strat[share_pos][1]=0
                
                
            if sec_max_reserves_pos==sec_max_community_pos:
                share_pos=sec_max_reserves_pos
                ratio=percent_contribution_cat[1]/percent_contribution_cat[2]
                
                community_strategy=budget[share_pos]/(1+ratio)
                strat[share_pos][2]=community_strategy # amount of resources that go to community
                strat[share_pos][1]=ratio * community_strategy #amount of resources that go to reserves
                
                if share_pos==third_max_laws_pos:
                    strat[share_pos][0]=0
                
            if sec_max_laws_pos==sec_max_reserves_pos==sec_max_community_pos:
                share_pos=sec_max_reserves_pos
                for j in range(3):
                    strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to laws
                    strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to reserves
                    strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] # amount of resources that go to community
                 
            
            if third_max_laws_pos != sec_max_reserves_pos and third_max_laws_pos != sec_max_community_pos:
                 
                if third_max_laws_pos==third_max_reserves_pos:
                    share_pos=third_max_laws_pos
                    ratio=percent_contribution_cat[0]/percent_contribution_cat[1]
                    
                    reserves_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][1]=reserves_strategy # amount of resources that go to reserves
                    strat[share_pos][0]=ratio * reserves_strategy #amount of resources that go to laws
                        
                       
                if third_max_laws_pos==third_max_community_pos:
                    share_pos=third_max_laws_pos
                    ratio=percent_contribution_cat[0]/percent_contribution_cat[2]
                    
                    community_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][2]=community_strategy # amount of resources that go to community
                    strat[share_pos][0]=ratio * community_strategy #amount of resources that go to laws
            else:
                strat[third_max_laws_pos][0]=0
                
                
                
            if third_max_reserves_pos != sec_max_laws_pos and third_max_reserves_pos != sec_max_community_pos:
                
                if third_max_laws_pos==third_max_reserves_pos:
                    share_pos=third_max_laws_pos
                    ratio=percent_contribution_cat[0]/percent_contribution_cat[1]
                    
                    reserves_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][1]=reserves_strategy # amount of resources that go to reserves
                    strat[share_pos][0]=ratio * reserves_strategy #amount of resources that go to laws
            
                if third_max_reserves_pos==third_max_community_pos:
                    share_pos=third_max_reserves_pos
                    ratio=percent_contribution_cat[1]/percent_contribution_cat[2]
                    
                    community_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][2]=community_strategy # amount of resources that go to community
                    strat[share_pos][1]=ratio * community_strategy #amount of resources that go to reserves
            else:
                strat[third_max_reserves_pos][1]=0
                
            
            if third_max_community_pos != sec_max_laws_pos and third_max_community_pos != sec_max_reserves_pos:
                
                if third_max_laws_pos==third_max_community_pos:
                    share_pos=third_max_laws_pos
                    ratio=percent_contribution_cat[0]/percent_contribution_cat[2]
                    
                    community_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][2]=community_strategy # amount of resources that go to community
                    strat[share_pos][0]=ratio * community_strategy #amount of resources that go to laws
            
                if third_max_reserves_pos==third_max_community_pos:
                    share_pos=third_max_reserves_pos
                    ratio=percent_contribution_cat[1]/percent_contribution_cat[2]
                    
                    community_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][2]=community_strategy # amount of resources that go to community
                    strat[share_pos][1]=ratio * community_strategy #amount of resources that go to reserves
            else:
                strat[third_max_community_pos][2]=0
                
                
            if third_max_laws_pos==third_max_reserves_pos==third_max_community_pos:
                share_pos=third_max_reserves_pos
                for j in range(3):
                    strat[share_pos][j]= percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to laws
                    strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to reserves
                    strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] # amount of resources that go to community
            
            for i in range(3):
                if sec_max_laws_pos!=i and third_max_laws_pos!=i and\
                    sec_max_reserves_pos!=i and third_max_reserves_pos !=i and\
                        sec_max_community_pos!=i and third_max_community_pos!=i:
                                for j in range(3):
                                    strat[i][j]= percent_contribution_cat[j]*budget[i] #amount of resources that go to laws
                                    strat[i][j]=percent_contribution_cat[j]*budget[i] #amount of resources that go to reserves
                                    strat[i][j]=percent_contribution_cat[j]*budget[i] # amount of resources that go to community
                    
            
        else:
            print("second and third contributing sub-battlefields have the same contribution in at least one of the battlefields")
            
            for i in range(3):
                
                ###Initialize positions if two values are the same
                if i==1:
                    if sec_max_laws==payoff_matrix[i][0]==payoff_matrix[i-1][0]:
                        sec_max_laws_pos=(i-1)
                    if sec_max_reserves==payoff_matrix[i][1]==payoff_matrix[i-1][1]:
                        sec_max_reserves_pos=(i-1)
                    if sec_max_community==payoff_matrix[i][2]==payoff_matrix[i-1][2]:
                        sec_max_community_pos=(i-1)
                        
                    if sec_max_laws==payoff_matrix[i][0]==payoff_matrix[i+1][0]:
                        sec_max_laws_pos=i
                    if sec_max_reserves==payoff_matrix[i][1]==payoff_matrix[i+1][1]:
                        sec_max_reserves_pos=i
                    if sec_max_community==payoff_matrix[i][2]==payoff_matrix[i+1][2]:
                        sec_max_community_pos=i
                        
                    if third_max_laws==payoff_matrix[i][0]==payoff_matrix[i-1][0]:
                        third_max_laws_pos=(i)
                    if third_max_reserves==payoff_matrix[i][1]==payoff_matrix[i-1][1]:
                        third_max_reserves_pos=(i)
                    if third_max_community==payoff_matrix[i][2]==payoff_matrix[i-1][2]:
                        third_max_community_pos=(i)
                        
                    if third_max_laws==payoff_matrix[i][0]==payoff_matrix[i+1][0]:
                        third_max_laws_pos=(i+1)
                    if third_max_reserves==payoff_matrix[i][1]==payoff_matrix[i+1][1]:
                        third_max_reserves_pos=(i+1)
                    if third_max_community==payoff_matrix[i][2]==payoff_matrix[i+1][2]:
                        third_max_community_pos=(i+1)
                        
                if i==0:
                    if sec_max_laws==payoff_matrix[i][0]==payoff_matrix[2][0]:
                        sec_max_laws_pos=(2)
                    if sec_max_reserves==payoff_matrix[i][1]==payoff_matrix[2][1]:
                        sec_max_reserves_pos=(2)
                    if sec_max_community==payoff_matrix[i][2]==payoff_matrix[2][2]:
                        sec_max_community_pos=(2)
                        
                    if sec_max_laws==payoff_matrix[i][0]==payoff_matrix[i+1][0]:
                        sec_max_laws_pos=i
                    if sec_max_reserves==payoff_matrix[i][1]==payoff_matrix[i+1][1]:
                        sec_max_reserves_pos=i
                    if sec_max_community==payoff_matrix[i][2]==payoff_matrix[i+1][2]:
                        sec_max_community_pos=i
                        
                    if third_max_laws==payoff_matrix[i][0]==payoff_matrix[2][0]:
                        third_max_laws_pos=(i)
                    if third_max_reserves==payoff_matrix[i][1]==payoff_matrix[2][1]:
                        third_max_reserves_pos=(i)
                    if third_max_community==payoff_matrix[i][2]==payoff_matrix[2][2]:
                        third_max_community_pos=(i)
                        
                    if third_max_laws==payoff_matrix[i][0]==payoff_matrix[i+1][0]:
                        third_max_laws_pos=(i+1)
                    if third_max_reserves==payoff_matrix[i][1]==payoff_matrix[i+1][1]:
                        third_max_reserves_pos=(i+1)
                    if third_max_community==payoff_matrix[i][2]==payoff_matrix[i+1][2]:
                        third_max_community_pos=(i+1)
                if i==3:
                    if sec_max_laws==payoff_matrix[i][0]==payoff_matrix[i-1][0]:
                        sec_max_laws_pos=(i-1)
                    if sec_max_reserves==payoff_matrix[i][1]==payoff_matrix[i-1][1]:
                        sec_max_reserves_pos=(i-1)
                    if sec_max_community==payoff_matrix[i][2]==payoff_matrix[i-1][2]:
                        sec_max_community_pos=(i-1)
                        
                    if sec_max_laws==payoff_matrix[i][0]==payoff_matrix[0][0]:
                        sec_max_laws_pos=i
                    if sec_max_reserves==payoff_matrix[i][1]==payoff_matrix[0][1]:
                        sec_max_reserves_pos=i
                    if sec_max_community==payoff_matrix[i][2]==payoff_matrix[0][2]:
                        sec_max_community_pos=i
                        
                    if third_max_laws==payoff_matrix[i][0]==payoff_matrix[i-1][0]:
                        third_max_laws_pos=(i)
                    if third_max_reserves==payoff_matrix[i][1]==payoff_matrix[i-1][1]:
                        third_max_reserves_pos=(i)
                    if third_max_community==payoff_matrix[i][2]==payoff_matrix[i-1][2]:
                        third_max_community_pos=(i)
                        
                    if third_max_laws==payoff_matrix[i][0]==payoff_matrix[0][0]:
                        third_max_laws_pos=(0)
                    if third_max_reserves==payoff_matrix[i][1]==payoff_matrix[0][1]:
                        third_max_reserves_pos=(0)
                    if third_max_community==payoff_matrix[i][2]==payoff_matrix[0][2]:
                        third_max_community_pos=(0) 
                
            
             ###  start scenarios where the second and third values are the same       
            if sec_max_laws==third_max_laws:
                if sec_max_laws_pos==sec_max_reserves_pos:
                    share_pos=sec_max_laws_pos
                    ratio=percent_contribution_cat[0]/percent_contribution_cat[1]
                    
                    reserves_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][1]=reserves_strategy # amount of resources that go to reserves
                    strat[share_pos][0]=ratio * reserves_strategy #amount of resources that go to laws
                    
                    if share_pos==third_max_community_pos:
                        strat[share_pos][2]=0
                            
                    
                if sec_max_laws_pos==sec_max_community_pos:
                    share_pos=sec_max_laws_pos
                    ratio=percent_contribution_cat[0]/percent_contribution_cat[2]
                    
                    community_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][2]=community_strategy # amount of resources that go to community
                    strat[share_pos][0]=ratio * community_strategy #amount of resources that go to laws
                    
                    if share_pos==third_max_reserves_pos:
                        strat[share_pos][1]=0
                        
                 
                if third_max_laws_pos==sec_max_reserves_pos:
                    share_pos=third_max_laws_pos
                    ratio=percent_contribution_cat[0]/percent_contribution_cat[1]
                    
                    reserves_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][1]=reserves_strategy # amount of resources that go to reserves
                    strat[share_pos][0]=ratio * reserves_strategy #amount of resources that go to laws
                    
                    if share_pos==third_max_community_pos:
                        strat[share_pos][2]=0
                            
                    
                if third_max_laws_pos==sec_max_community_pos:
                    share_pos=third_max_laws_pos
                    ratio=percent_contribution_cat[0]/percent_contribution_cat[2]
                    
                    community_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][2]=community_strategy # amount of resources that go to community
                    strat[share_pos][0]=ratio * community_strategy #amount of resources that go to laws
                    
                    if share_pos==third_max_reserves_pos:
                        strat[share_pos][1]=0
                        
                        
                if sec_max_laws_pos==third_max_reserves_pos:
                    share_pos=sec_max_laws_pos
                    strat[share_pos][1]=0
                if third_max_laws_pos==third_max_reserves_pos:
                    share_pos=third_max_laws_pos
                    strat[share_pos][1]=0
                if sec_max_laws_pos==third_max_community_pos:
                    share_pos=sec_max_laws_pos
                    strat[share_pos][2]=0
                if third_max_laws_pos==third_max_community_pos:
                    share_pos=third_max_laws_pos
                    strat[share_pos][2]=0
    
                        
                if sec_max_laws_pos==sec_max_reserves_pos==sec_max_community_pos:
                     share_pos=sec_max_reserves_pos
                     for j in range(3):
                         strat[share_pos][j]= percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to laws
                         strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to reserves
                         strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] # amount of resources that go to community
                if third_max_laws_pos==sec_max_reserves_pos==sec_max_community_pos:
                     share_pos=sec_max_reserves_pos
                     for j in range(3):
                         strat[share_pos][j]= percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to laws
                         strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to reserves
                         strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] # amount of resources that go to community
                    
            if sec_max_reserves==third_max_reserves:
                if sec_max_laws_pos==sec_max_reserves_pos:
                    share_pos=sec_max_laws_pos
                    ratio=percent_contribution_cat[0]/percent_contribution_cat[1]
                    
                    reserves_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][1]=reserves_strategy # amount of resources that go to reserves
                    strat[share_pos][0]=ratio * reserves_strategy #amount of resources that go to laws
                    
                    if share_pos==third_max_community_pos:
                        strat[share_pos][2]=0
                
                if sec_max_reserves_pos==sec_max_community_pos:
                    share_pos=sec_max_reserves_pos
                    ratio=percent_contribution_cat[1]/percent_contribution_cat[2]
                    
                    community_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][2]=community_strategy # amount of resources that go to community
                    strat[share_pos][1]=ratio * community_strategy #amount of resources that go to reserves
                    
                    if share_pos==third_max_laws_pos:
                        strat[share_pos][0]=0
                
                if sec_max_laws_pos==third_max_reserves_pos:
                    share_pos=sec_max_laws_pos
                    ratio=percent_contribution_cat[0]/percent_contribution_cat[1]
                    
                    reserves_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][1]=reserves_strategy # amount of resources that go to reserves
                    strat[share_pos][0]=ratio * reserves_strategy #amount of resources that go to laws
                    
                    if share_pos==third_max_community_pos:
                        strat[share_pos][2]=0
                
                if third_max_reserves_pos==sec_max_community_pos:
                    share_pos=third_max_reserves_pos
                    ratio=percent_contribution_cat[1]/percent_contribution_cat[2]
                    
                    community_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][2]=community_strategy # amount of resources that go to community
                    strat[share_pos][1]=ratio * community_strategy #amount of resources that go to reserves
                    
                    if share_pos==third_max_laws_pos:
                        strat[share_pos][0]=0
                    
                if sec_max_reserves_pos==third_max_laws_pos:
                    share_pos=sec_max_reserves_pos
                    strat[share_pos][0]=0
                if third_max_reserves_pos==third_max_laws_pos:
                    share_pos=third_max_reserves_pos
                    strat[share_pos][0]=0
                if sec_max_reserves_pos==third_max_community_pos:
                    share_pos=sec_max_reserves_pos
                    strat[share_pos][2]=0
                if third_max_reserves_pos==third_max_community_pos:
                    share_pos=third_max_reserves_pos
                    strat[share_pos][2]=0       
                        
                if sec_max_reserves_pos==sec_max_laws_pos==sec_max_community_pos:
                     share_pos=sec_max_reserves_pos
                     for j in range(3):
                         strat[share_pos][j]= percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to laws
                         strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to reserves
                         strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] # amount of resources that go to community
                if third_max_reserves_pos==sec_max_laws_pos==sec_max_community_pos:
                     share_pos=third_max_reserves_pos
                     for j in range(3):
                         strat[share_pos][j]= percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to laws
                         strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to reserves
                         strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] # amount of resources that go to community
                        
                        
            if sec_max_community==third_max_community:
                if sec_max_laws_pos==sec_max_community_pos:
                    share_pos=sec_max_laws_pos
                    ratio=percent_contribution_cat[0]/percent_contribution_cat[2]
                    
                    community_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][2]=community_strategy # amount of resources that go to community
                    strat[share_pos][0]=ratio * community_strategy #amount of resources that go to laws
                    
                    if share_pos==third_max_reserves_pos:
                        strat[share_pos][1]=0
                        
                if sec_max_reserves_pos==sec_max_community_pos:
                    share_pos=sec_max_reserves_pos
                    ratio=percent_contribution_cat[1]/percent_contribution_cat[2]
                    
                    community_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][2]=community_strategy # amount of resources that go to community
                    strat[share_pos][1]=ratio * community_strategy #amount of resources that go to reserves
                    
                    if share_pos==third_max_laws_pos:
                        strat[share_pos][0]=0
                
                if sec_max_laws_pos==third_max_community_pos:
                    share_pos=sec_max_laws_pos
                    ratio=percent_contribution_cat[0]/percent_contribution_cat[2]
                    
                    community_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][2]=community_strategy # amount of resources that go to community
                    strat[share_pos][0]=ratio * community_strategy #amount of resources that go to laws
                    
                    if share_pos==third_max_reserves_pos:
                        strat[share_pos][1]=0
                        
                if sec_max_reserves_pos==third_max_community_pos:
                    share_pos=sec_max_reserves_pos
                    ratio=percent_contribution_cat[1]/percent_contribution_cat[2]
                    
                    community_strategy=budget[share_pos]/(1+ratio)
                    strat[share_pos][2]=community_strategy # amount of resources that go to community
                    strat[share_pos][1]=ratio * community_strategy #amount of resources that go to reserves
                    
                    if share_pos==third_max_laws_pos:
                        strat[share_pos][0]=0
                 
                if sec_max_community_pos==third_max_laws_pos:
                    share_pos=sec_max_community_pos
                    strat[share_pos][0]=0
                if third_max_community_pos==third_max_laws_pos:
                    share_pos=third_max_community_pos
                    strat[share_pos][0]=0
                if sec_max_community_pos==third_max_reserves_pos:
                    share_pos=sec_max_community_pos
                    strat[share_pos][1]=0
                    print("hi")
                if third_max_community_pos==third_max_reserves_pos:
                    share_pos=third_max_community_pos
                    strat[share_pos][1]=0 
                        
                if sec_max_community_pos==sec_max_reserves_pos==sec_max_laws_pos:
                     share_pos=sec_max_reserves_pos
                     for j in range(3):
                         strat[share_pos][j]= percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to laws
                         strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to reserves
                         strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] # amount of resources that go to community
                
                if third_max_community_pos==sec_max_reserves_pos==sec_max_laws_pos:
                     share_pos=sec_max_reserves_pos
                     for j in range(3):
                         strat[share_pos][j]= percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to laws
                         strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to reserves
                         strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] # amount of resources that go to community   
       
        
       ### If the second and third sub-battlefields are not the same
        if sec_max_laws != third_max_laws:
            if sec_max_laws_pos==third_max_reserves_pos:
                share_pos=sec_max_laws_pos
                strat[share_pos][1]=0
            if sec_max_laws_pos==third_max_community_pos:
                share_pos=sec_max_laws_pos
                strat[share_pos][2]=0
        if sec_max_reserves!= third_max_reserves:
            if sec_max_reserves_pos==third_max_laws_pos:
                share_pos=sec_max_reserves_pos
                strat[share_pos][0]=0
            if sec_max_reserves_pos==third_max_community_pos:
                share_pos=sec_max_reserves_pos
                strat[share_pos][2]=0
        if sec_max_community != third_max_community:
            if sec_max_community_pos==third_max_laws_pos:
                share_pos=sec_max_community_pos
                strat[share_pos][0]=0
            if sec_max_community_pos==third_max_reserves_pos:
                share_pos=sec_max_community_pos
                strat[share_pos][1]=0

           
                
        ### No overlap 
        for i in range(3):
            if sec_max_laws_pos!=i and third_max_laws_pos!=i and\
                sec_max_reserves_pos!=i and third_max_reserves_pos !=i and\
                    sec_max_community_pos!=i and third_max_community_pos!=i:
                            for j in range(3):
                                strat[i][j]= percent_contribution_cat[j]*budget[i] #amount of resources that go to laws
                                strat[i][j]=percent_contribution_cat[j]*budget[i] #amount of resources that go to reserves
                                strat[i][j]=percent_contribution_cat[j]*budget[i] # amount of resources that community
        
        keep_playing='no'
        print("Strategy 3 was played") 
        return strat, keep_playing 
            

