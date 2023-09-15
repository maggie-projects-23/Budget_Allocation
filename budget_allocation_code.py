import numpy as np
import random
from strategy_set import Strategy


def Budget_Allocation_Game(r,r_2, memory, POPULATION, C, P, PAYOFF_BANK,payoff_worth, Laws_payoff, \
                           Reserves_payoff, Community_payoff, Payoff_matrix ):
    C_PEOPLE=C[2]
    P_PEOPLE=P[2]
    
    ######################## Playing the Game!  ########################
    game_number=0
    winners="none" # gets overwritten after first game is played
    previous_strat=0
    previous_games_C=[]
    previous_payoffs_C=[]
    previous_games_P=[]
    previous_payoffs_P=[]
    C_PAYOFF=0 # gets overwritten after first game is played
    P_PAYOFF=0 # gets overwritten after first game is played
    
    while C[2]>0 and P[2]>0:
        ####### Players distribute resources #######
        keep_playing="yes"
        
        while keep_playing == "yes":
            
            r=r #90 #random.uniform(0, 99)
            
            if winners != "none":
                if memory == "no memory":
                    C_strat , keep_playing = Strategy(r,C,Payoff_matrix, PAYOFF_BANK)
                    # print("The Convervationalists strategy is")
                    # print(C_strat)
                    
                if memory == "last game":
                    if winners == "Conservationists ":
                        adopt_previous_strat=random.uniform(0, 100)
                        if adopt_previous_strat<(C_PAYOFF/PAYOFF_BANK):
                            print("C: previous strat was played")
                            C_strat , keep_playing = Strategy(previous_strat,C,Payoff_matrix, PAYOFF_BANK)
                            r=previous_strat
                        else:
                            C_strat , keep_playing = Strategy(r,C,Payoff_matrix, PAYOFF_BANK)
                    else: 
                        C_strat , keep_playing = Strategy(r,C,Payoff_matrix, PAYOFF_BANK)
                    # print("The Conservationists  strategy is")
                    # print(C_strat)
                    
                if memory == "all previous games":
                    previous_games_C.append(r)
                    previous_payoffs_C.append(sum(C_PAYOFF))
                    
                    strat_with_top_payoff=max(previous_payoffs_C)
                    
                    adopt_previous_strat=random.uniform(0, 100)
                    if adopt_previous_strat<((strat_with_top_payoff/PAYOFF_BANK)*100):
                        print("C: previous strat with top payoff was played")
                        for i in range(len(previous_payoffs_C)):
                            if strat_with_top_payoff == previous_payoffs_C[i]:
                                r= previous_games_C[i]
                        C_strat , keep_playing = Strategy(r,C,Payoff_matrix, PAYOFF_BANK)
                    else:
                        C_strat , keep_playing = Strategy(r,C,Payoff_matrix, PAYOFF_BANK)
            
                    # print("The Conservationists  strategy is")
                    # print(C_strat)
        
            if winners == "none":
                C_strat , keep_playing = Strategy(r,C,Payoff_matrix, PAYOFF_BANK)
                # print("The Conservationists strategy is")
                # print(C_strat)
            
            previous_strat=r
                  
            
        keep_playing="yes"    
        while keep_playing == "yes":
            
            r_2=r_2# 90 random.uniform(0, 99)
            
            if winners != "none":
                if memory == "no memory":
                    P_strat , keep_playing = Strategy(r_2,P,Payoff_matrix, PAYOFF_BANK)
                    # print("The Poachers strategy is")
                    # print(P_strat)
                    
                if memory == "last game":
                    if winners == "Poachers":
                        adopt_previous_strat=random.uniform(0, 100)
                        if adopt_previous_strat<(P_PAYOFF/PAYOFF_BANK):
                            print("P: previous strat was played")
                            P_strat , keep_playing = Strategy(previous_strat,P,Payoff_matrix, PAYOFF_BANK)
                            r_2=previous_strat
                        else:
                            P_strat , keep_playing = Strategy(r_2,P,Payoff_matrix, PAYOFF_BANK)
                    else: 
                        P_strat , keep_playing = Strategy(r_2,P,Payoff_matrix, PAYOFF_BANK)
                    # print("The Poachers strategy is")
                    # print(P_strat)
                    
                if memory == "all previous games":
                    previous_games_P.append(r_2)
                    previous_payoffs_P.append(sum(P_PAYOFF))
                    
                    strat_with_top_payoff=max(previous_payoffs_P)
                    
                    adopt_previous_strat=random.uniform(0, 100)
                    if adopt_previous_strat<((strat_with_top_payoff/PAYOFF_BANK)*100):
                        print("P: previous strat with top payoff was played")
                        for i in range(len(previous_payoffs_P)):
                            if strat_with_top_payoff == previous_payoffs_P[i]:
                                r_2= previous_games_P[i]      
                        P_strat , keep_playing = Strategy(r_2,P,Payoff_matrix, PAYOFF_BANK)
                    else:
                        P_strat , keep_playing = Strategy(r_2,P,Payoff_matrix, PAYOFF_BANK)
            
                    # print("The Poachers strategy is")
                    # print(P_strat)
                            
            if winners == "none":
                P_strat , keep_playing = Strategy(r_2,P,Payoff_matrix, PAYOFF_BANK)
                # print(" The Poachers strategy is")
                # print(P_strat)
            previous_strat=r_2
            
            
            
                #Rows are the following: Monetary, Non-Monetary, People. Columns are Player 1 and Player 2
        
        LAWS=np.array([[C_strat[0][0], P_strat[0][0]]\
            ,[C_strat[1][0], P_strat[1][0]]\
            ,[C_strat[2][0], P_strat[2][0]]])
        RESERVES=np.array([[C_strat[0][1], P_strat[0][1]]\
            ,[C_strat[1][1], P_strat[1][1]]\
            ,[C_strat[2][1], P_strat[2][1]]])
        COMMUNITY=np.array([[C_strat[0][2], P_strat[0][2]]\
            ,[C_strat[1][2], P_strat[1][2]]\
            ,[C_strat[2][2], P_strat[2][2]]])
    
    
    
        ####### See who won each sub-battlefield and award points #######
        C_PAYOFF=np.zeros(3)
        P_PAYOFF=np.zeros(3)
        C_people_bud=0 #For tracking what percent of people go to Conservationists  next game
        P_people_bud=0 #For tracking what percent of people go to Poachers next game
    
        for i in range(3):
            if LAWS[i-1][0]>LAWS[i-1][1]:
                C_PAYOFF[0]=C_PAYOFF[0]+Laws_payoff[i-1]
            else:
                P_PAYOFF[0]=P_PAYOFF[0]+Laws_payoff[i-1]
    
            if RESERVES[i-1][0]>RESERVES[i-1][1]:
                C_PAYOFF[1]=C_PAYOFF[1]+Reserves_payoff[i-1]
            else:
                P_PAYOFF[1]=P_PAYOFF[1]+Reserves_payoff[i-1]
    
            if COMMUNITY[i-1][0]>COMMUNITY[i-1][1]:
                C_people_bud=C_people_bud+payoff_worth[i]
                C_PAYOFF[2]=C_PAYOFF[2]+Community_payoff[i-1]
            else:
                P_people_bud=P_people_bud+payoff_worth[i]
                P_PAYOFF[2]=P_PAYOFF[2]+Community_payoff[i-1]
    
    
    
        ####### See who won the game and set budget for next game#######
        C_final_score=sum(C_PAYOFF)
        P_final_score=sum(P_PAYOFF)
        if C_final_score>P_final_score:
            print("Conservationists won the round with a payoff of ", C_final_score)
            winners="Conservationists "
        else:
            print("Poachers won the round with a payoff of ", P_final_score)
            winners="Poachers"
            print("The game is over with winners being", winners )
        return(winners, C_PAYOFF, P_PAYOFF)
        
    
        ####### Set budgets for next game #######
        game_number=game_number+1
        print("The number of games played is:", game_number)
    
        if C_people_bud>0 and P_people_bud>0:
            C[2]=round(C_people_bud*POPULATION)
            C[0]=4*C_PEOPLE
            P[2]=round(P_people_bud*POPULATION)
            P[0]=6*P_PEOPLE
            C[2]=0  # Uncomment for only one round to be played
            P[2]=0  # Uncomment for only one round to be played
        else:
            C[2]=round(C_people_bud*POPULATION)
            P[2]=round(P_people_bud*POPULATION)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            