
def Strategy_7(r,Payoff_Bank, payoff_matrix, budget, strat):
    
    strat=strat
    budget=budget
    r=r
    Payoff_Bank=Payoff_Bank
    payoff_matrix=payoff_matrix

            
    ##### Strategy 7 #####
    for i in range(3):
        strat[i][2]=budget[i]
            
    print("Strategy 7 was played")
    return(strat)
        