
def Strategy_6(r,Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat):
    
    strat=strat
    budget=budget
    r=r
    Payoff_Bank=Payoff_Bank
    payoff_matrix=payoff_matrix

            
    ##### Strategy 6 #####
    for i in range(3):
        for j in range (3):
            strat[i][j]=percent_contribution_cat[j]*budget[i]
            
    print("Strategy 6 was played")
    return(strat)
        