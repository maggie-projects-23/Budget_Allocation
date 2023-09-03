import numpy as np
import random

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


######################## Playing the Game!  ########################
game_number=1

while C[2]>0 and P[2]>0:
    ####### Players distribute resources #######
            #Columns are the following: Monetary, Non-Monetary, People. Rows are Player 1 and Player 2
    LAWS=np.array([[random.randint(0,C[0]), random.randint(0,P[0])]\
        ,[random.randint(0,C[1]), random.randint(0,P[1])]\
        ,[random.randint(0,C[2]), random.randint(0,P[2])] ])
    RESERVES=np.array([[random.randint(0,C[0]-LAWS[0][0]), random.randint(0,P[0]-LAWS[0][1])]\
        ,[random.randint(0,C[1]-LAWS[1][0]), random.randint(0,P[1]-LAWS[1][1])]\
        ,[random.randint(0,C[2]-LAWS[2][0]), random.randint(0,P[2]-LAWS[2][1])] ])
    COMMUNITY=np.array([[C[0]-LAWS[0][0]-RESERVES[0][0], P[0]-LAWS[0][1]-RESERVES[0][1]]\
        ,[C[1]-LAWS[1][0]-RESERVES[1][0], P[1]-LAWS[1][1]-RESERVES[1][1]]\
        ,[C[2]-LAWS[2][0]-RESERVES[2][0], P[2]-LAWS[2][1]-RESERVES[2][1]] ])

    print("Laws Battlefield:")
    print(LAWS)
    print("Reserves Battlefield:")
    print(RESERVES)
    print("Community Battlefield:")
    print(COMMUNITY)

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
        print("Conservationalist won the game with a payoff of ", C_final_score)
        winners="Conservationalists"
    else:
        print("Poachers won the game with a payoff of ", P_final_score)
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


























        