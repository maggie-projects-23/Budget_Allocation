import numpy as np
import random
from strategy_set import Strategy

####### Decide if the players have memory of previous strategies(s) #######
##Uncomment which one you want ##

# ### No Memory###
# memory="no memory"


# ### Memory of last game  ###
# memory="last game"


### Memory of all previous games  ###
memory="all previous games"


####### Initialize player's budgets and  #######
POPULATION=100 #total people in the community/area of interest
C_PEOPLE=round(.5*POPULATION) #how many people are influenced on by the conservationalists
C_MONETARY=4*C_PEOPLE #Monetary budget for conservationalists Each person contributes so much to the budget.
C_NONMONETARY=250 #Non-monetary budget for conservationalists

P_PEOPLE=POPULATION-C_PEOPLE#how many people are influenced on by the poachers
P_MONETARY=6*P_PEOPLE #Monetary budget for poachers. Each person contributes so much to the budget.
P_NONMONETARY=150 #Non-monetary budget for poachers

C=[C_MONETARY, C_NONMONETARY, C_PEOPLE] #Initial budgets for Conservationalists
P=[P_MONETARY, P_NONMONETARY, P_PEOPLE] #Initial budgets for Conservationalists
print(C,P)

####### Battlefield's Payoffs #######
PAYOFF_BANK=100
payoff_worth=np.array([.15,.3,.55]) #[Laws payoff, Reserve payoff, Community payoff]

Laws_payoff=np.array([0.55*payoff_worth[0]*PAYOFF_BANK\
    ,0.2*payoff_worth[0]*PAYOFF_BANK\
        ,0.25*payoff_worth[0]*PAYOFF_BANK])

Reserves_payoff=np.array([0.3*payoff_worth[1]*PAYOFF_BANK\
    ,0.5*payoff_worth[1]*PAYOFF_BANK\
        ,0.2*payoff_worth[1]*PAYOFF_BANK])

Community_payoff=np.array([0.3*payoff_worth[2]*PAYOFF_BANK\
    ,0.1*payoff_worth[2]*PAYOFF_BANK\
        ,0.6*payoff_worth[2]*PAYOFF_BANK])
    
Payoff_matrix=np.zeros((3,3))
for i in range(3):
    Payoff_matrix[i][0]=Laws_payoff[i]
    Payoff_matrix[i][1]=Reserves_payoff[i]
    Payoff_matrix[i][2]=Community_payoff[i]

print("Payoff_Matrix")
print(Payoff_matrix)


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
        
        r=random.uniform(0, 99)
        
        if winners != "none":
            if memory == "no memory":
                C_strat , keep_playing = Strategy(r,C,Payoff_matrix, PAYOFF_BANK)
                print("The Convervationalists strategy is")
                print(C_strat)
                
            if memory == "last game":
                if winners == "Conservationalists":
                    adopt_previous_strat=random.uniform(0, 100)
                    if adopt_previous_strat<90:
                        print("C: previous strat was played")
                        C_strat , keep_playing = Strategy(previous_strat,C,Payoff_matrix, PAYOFF_BANK)
                        r=previous_strat
                    else:
                        C_strat , keep_playing = Strategy(r,C,Payoff_matrix, PAYOFF_BANK)
                else: 
                    C_strat , keep_playing = Strategy(r,C,Payoff_matrix, PAYOFF_BANK)
                print("The Convervationalists strategy is")
                print(C_strat)
                
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
        
                print("The Convervationalists strategy is")
                print(C_strat)
    
        if winners == "none":
            C_strat , keep_playing = Strategy(r,C,Payoff_matrix, PAYOFF_BANK)
            print("The Convervationalists strategy is")
            print(C_strat)
        
        previous_strat=r
              
        
    keep_playing="yes"    
    while keep_playing == "yes":
        
        r_2=random.uniform(0, 99)
        
        if winners != "none":
            if memory == "no memory":
                P_strat , keep_playing = Strategy(r_2,P,Payoff_matrix, PAYOFF_BANK)
                print("The Poachers strategy is")
                print(P_strat)
                
            if memory == "last game":
                if winners == "Poachers":
                    adopt_previous_strat=random.uniform(0, 100)
                    if adopt_previous_strat<90:
                        print("P: previous strat was played")
                        P_strat , keep_playing = Strategy(previous_strat,P,Payoff_matrix, PAYOFF_BANK)
                        r_2=previous_strat
                    else:
                        P_strat , keep_playing = Strategy(r_2,P,Payoff_matrix, PAYOFF_BANK)
                else: 
                    P_strat , keep_playing = Strategy(r_2,P,Payoff_matrix, PAYOFF_BANK)
                print("The Poachers strategy is")
                print(P_strat)
                
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
        
                print("The Poachers strategy is")
                print(P_strat)
                        
        if winners == "none":
            P_strat , keep_playing = Strategy(r_2,P,Payoff_matrix, PAYOFF_BANK)
            print(" The Poachers strategy is")
            print(P_strat)
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

    # print("Laws Battlefield:")
    # print(LAWS)
    # print("Reserves Battlefield:")
    # print(RESERVES)
    # print("Community Battlefield:")
    # print(COMMUNITY)

    ####### See who won each sub-battlefield and award points #######
    C_PAYOFF=np.zeros(3)
    P_PAYOFF=np.zeros(3)
    C_people_bud=0 #For tracking what percent of people go to Conservationalists next game
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

    print("C_Payoff=", C_PAYOFF)
    print("P_Payoff=", P_PAYOFF)


    ####### See who won the game and set budget for next game#######
    C_final_score=sum(C_PAYOFF)
    P_final_score=sum(P_PAYOFF)
    if C_final_score>P_final_score:
        print("Conservationalist won the round with a payoff of ", C_final_score)
        winners="Conservationalists"
    else:
        print("Poachers won the round with a payoff of ", P_final_score)
        winners="Poachers"


    ####### Set budgets for next game #######
    game_number=game_number+1
    print("The number of games played is:", game_number)

    if C_people_bud>0 and P_people_bud>0:
        C[2]=round(C_people_bud*POPULATION)
        C[0]=4*C_PEOPLE
        P[2]=round(P_people_bud*POPULATION)
        P[0]=6*P_PEOPLE
        print(C,P)
    else:
        C[2]=round(C_people_bud*POPULATION)
        P[2]=round(P_people_bud*POPULATION)
        print("The game is over with winners being", winners )


























        