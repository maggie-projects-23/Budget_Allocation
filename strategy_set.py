import numpy as np
import random


def Strategy(budget, payoff_matrix, Payoff_Bank):
    
    strat=np.zeros((3,3)) ####                 Laws    Reserves    Commnity 
                          #### Monetary     [                               ]
                          #### Non-Monetary [                               ]
                          #### People       [                               ]
    r=random.randint(0,100)
    
    
    #Gives percentage (in decimal form) of how much the Laws, Reserves, and Community bettlefield contribute
    percent_contribution_cat=np.array(np.sum(payoff_matrix, axis=1)/Payoff_Bank)
    print(percent_contribution_cat)
    
    #Determines largest contributing sub-battlefield
    def Largest(Payoff_Bank):
        max_laws=max(payoff_matrix[0][0],payoff_matrix[1][0], payoff_matrix[2][0])
        max_reserves=max(payoff_matrix[0][1],payoff_matrix[1][1], payoff_matrix[2][1])
        max_community=max(payoff_matrix[0][2],payoff_matrix[1][2], payoff_matrix[2][2])
        return(max_laws, max_reserves, max_community)
    
    #Determines second largest contributing sub-battlefield
    def Second_and_Third_Largest(Payoff_Bank):
        laws_list=[payoff_matrix[0][0],payoff_matrix[1][0], payoff_matrix[2][0]]
        reserves_list=[payoff_matrix[0][1],payoff_matrix[1][1], payoff_matrix[2][1]]
        community_list=[payoff_matrix[0][2],payoff_matrix[1][2], payoff_matrix[2][2]]
        
        laws_list.sort()
        reserves_list.sort()
        community_list.sort()
        
        sec_max_laws=laws_list[1]
        sec_max_reserves=reserves_list[1]
        sec_max_community=community_list[1]
        
        third_max_laws=laws_list[0]
        third_max_reserves=reserves_list[0]
        third_max_community=community_list[0]
        return(sec_max_laws, sec_max_reserves, sec_max_community\
               ,third_max_laws, third_max_reserves, third_max_community)
        
    
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
    ## llocate all resources of a particular type to the sub-battlefield that contributes the post
    ## payoff for that battlefield. If the same sub-battlefield type contributes the most in two different
    ## battlefields, then the resources are split according to how much one battlefield contributes that then other 
    if r>10 and r<=20:
        
        (max_laws, max_reserves, max_community) = Largest(Payoff_Bank)
        
        print("The payoff matrix is", payoff_matrix)
     
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
                    strat[i][0]= percent_contribution_cat[0]*budget[i] #amount of resources that go to laws
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

        print("Strategy 2 was played") 
    # =============================================================================
    # =============================================================================
    

    # =============================================================================
    # =============================================================================   
    ##### Strategy 3 #####
    ## Distribute all respectuve resources evenly across all corresponding sub-battlefields
    if r>0 and r<=100:
        (sec_max_laws, sec_max_reserves, sec_max_community\
               ,third_max_laws, third_max_reserves, third_max_community) = Second_and_Third_Largest(Payoff_Bank)
        print(third_max_community)
        
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
                
        
        print("Strategy 3 was played")
        
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
                strat[share_pos][2]=0
            
            
        if sec_max_reserves_pos==sec_max_community_pos:
            share_pos=sec_max_reserves_pos
            ratio=percent_contribution_cat[1]/percent_contribution_cat[2]
            
            community_strategy=budget[share_pos]/(1+ratio)
            strat[share_pos][2]=community_strategy # amount of resources that go to community
            strat[share_pos][1]=ratio * community_strategy #amount of resources that go to reserves
            
            if share_pos==third_max_laws_pos:
                strat[share_pos][2]=0
            
        if sec_max_laws_pos==sec_max_reserves_pos==sec_max_community_pos:
            share_pos=sec_max_reserves_pos
            for j in range(3):
                strat[share_pos][j]= percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to laws
                strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to reserves
                strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] # amount of resources that go to community
             
              
             
        # if third_max_laws_pos==third_max_reserves_pos:
        #     share_pos=third_max_laws_pos
        #     ratio=percent_contribution_cat[0]/percent_contribution_cat[1]
            
        #     reserves_strategy=budget[share_pos]/(1+ratio)
        #     strat[share_pos][1]=reserves_strategy # amount of resources that go to reserves
        #     strat[share_pos][0]=ratio * reserves_strategy #amount of resources that go to laws
                    
                   
        # if third_max_laws_pos==third_max_community_pos:
        #     share_pos=sec_max_laws_pos
        #     ratio=percent_contribution_cat[0]/percent_contribution_cat[2]
            
        #     community_strategy=budget[share_pos]/(1+ratio)
        #     strat[share_pos][2]=community_strategy # amount of resources that go to community
        #     strat[share_pos][0]=ratio * community_strategy #amount of resources that go to laws
                   
                   
        # if third_max_reserves_pos==third_max_community_pos:
        #     share_pos=sec_max_reserves_pos
        #     ratio=percent_contribution_cat[1]/percent_contribution_cat[2]
            
        #     community_strategy=budget[share_pos]/(1+ratio)
        #     strat[share_pos][2]=community_strategy # amount of resources that go to community
        #     strat[share_pos][1]=ratio * community_strategy #amount of resources that go to reserves
            
        # if third_max_laws_pos==third_max_reserves_pos==sec_max_community_pos:
        #     share_pos=sec_max_reserves_pos
        #     for j in range(3):
        #         strat[share_pos][j]= percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to laws
        #         strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] #amount of resources that go to reserves
        #         strat[share_pos][j]=percent_contribution_cat[j]*budget[share_pos] # amount of resources that go to community
 
    # =============================================================================
    # =============================================================================
        
                
    print("The strategy matrix is")
    print(strat)
        
        

        
Strategy([10,9,21],np.array([[3.75,9,5.5],[3,6,16.5], [8.25, 15, 33]]), 100)














