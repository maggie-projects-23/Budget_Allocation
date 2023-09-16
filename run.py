import numpy as np
import random
import matplotlib.pyplot as plt
from budget_allocation_code import Budget_Allocation_Game


#### Note for only one round to be played, uncomment out "C[2]=0' and 'P[2]=0'(lines 189 and 190)



####### Decide if the players have memory of previous strategies(s) #######
##Uncomment which one you want ##

# ### No Memory###
# memory="no memory"


### Memory of last game  ###
memory="last game"


# ### Memory of all previous games  ###
# memory="all previous games"



####### Initialize player's budgets and  #######

    ########Insure that the the proportions match in next budget #######
    ########computations for budget_allocation_code ########
    
POPULATION=100 #total people in the community/area of interest
C_PEOPLE=round(.1*POPULATION) #how many people are influenced on by the conservationists 
C_MONETARY=1*C_PEOPLE #Monetary budget for conservationists  Each person contributes so much to the budget.
C_NONMONETARY=200 #Non-monetary budget for conservationists 

P_PEOPLE=POPULATION-C_PEOPLE#how many people are influenced on by the poachers
P_MONETARY=1*P_PEOPLE #Monetary budget for poachers. Each person contributes so much to the budget.
P_NONMONETARY=10 #Non-monetary budget for poachers

C=[C_MONETARY, C_NONMONETARY, C_PEOPLE] #Initial budgets for Conservationists 
P=[P_MONETARY, P_NONMONETARY, P_PEOPLE] #Initial budgets for Conservationists 
# print(C,P)


####### Battlefield's Payoffs #######
PAYOFF_BANK=100
payoff_worth=np.array([.15,.30,.55]) #[Laws payoff, Reserve payoff, Community payoff]

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


#### Run the Game #####
r = 10 #overwritten for last game  memory and all games memory cases by uncommenting out lines 28
r_2 = 10 #overwritten for last game  memory and all games memory cases by uncommenting out lines 80


##### Get Histogram for length played and number won #####
C_wins_rounds_num=[]
P_wins_rounds_num=[]

for i in range(10000):
    
    C=[C_MONETARY, C_NONMONETARY, C_PEOPLE] #Initial budgets for Conservationists 
    P=[P_MONETARY, P_NONMONETARY, P_PEOPLE] #Initial budgets for Poachers

    winners, rounds_num = Budget_Allocation_Game(r,r_2, memory, POPULATION, \
                              C, P, PAYOFF_BANK, payoff_worth, Laws_payoff ,Reserves_payoff, Community_payoff, Payoff_matrix)
   
    if winners == "Conservationists":
        C_wins_rounds_num.append(rounds_num)
    else:
        P_wins_rounds_num.append(rounds_num)
    

fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

bins = np.linspace(1, 45, 45)
ax.set_xticks(range(46))
plt.xlim([0, 45])
plt.hist([C_wins_rounds_num, P_wins_rounds_num], bins, align='left', color=['teal', 'deeppink'], \
         label=['Conservationists', 'Poachers'])

plt.legend(loc='upper right')
plt.title('Distribution of Game Wins Based on the Number of Rounds in the Game')
plt.xlabel('Number of Rounds in the Game')
plt.ylabel('Number of Wins')
plt.show() 


# ##### Box Plot for win distrubutions ####

# C_final_scores_matrix=[]
# P_final_scores_matrix=[]

# for j in range(10,100,10): #For even battlefields, use [10,20,30,40,60,70,80,90]:
#     C_final_scores_list=[]
#     P_final_scores_list=[]
#     for i in range(10,100,10): #For even battlefields, use [10,20,30,40,60,70,80,90]: 
#         r = j #conservationists strategy
#         r_2 = i #Poachers strategy
#         winners, last_game_C_PAYOFF, last_game_P_PAYOFF, rounds_num = Budget_Allocation_Game(r,r_2, memory, POPULATION, \
#                           C, P, PAYOFF_BANK, payoff_worth, Laws_payoff ,Reserves_payoff, Community_payoff, Payoff_matrix)
    
#         C_final_scores_list.append(sum(last_game_C_PAYOFF))
#         P_final_scores_list.append(sum(last_game_P_PAYOFF))
#     C_final_scores_matrix.append(C_final_scores_list)  
#     P_final_scores_matrix.append(P_final_scores_list)  

# ### Make and show the Box Plot for Conservationalists##
# fig = plt.figure(figsize =(10, 7))
# ax = fig.add_subplot(111)
     
# # Creating plot
# plt.boxplot(C_final_scores_matrix, vert = 0)
    
 
# # Adding title
# plt.title("Conservationalists Payoff Distribtutions")

 
# # Removing top axes and right axes
# # ticks
# ax.get_xaxis().tick_bottom()
# ax.get_yaxis().tick_left()

# #label axes
# plt.xlabel("Payoff Values")
# plt.ylabel("Strategy Number")
     
# # show plot
# plt.show()


# ### Make and show the Box Plot for Poachers##
# fig = plt.figure(figsize =(10, 7))
# ax = fig.add_subplot(111)
     
# # Creating plot
# plt.boxplot(P_final_scores_matrix, vert = 0)
    
 
# # Adding title
# plt.title("Poachers Payoff Distribtutions")
 
# # Removing top axes and right axes
# # ticks
# ax.get_xaxis().tick_bottom()
# # ax.get_yaxis().tick_left()

# # ax.set_yticklabels(['1', '2','3', '4', '6', '7', '8', '9']) #Use if battlefields have equal payoff

# #label axes
# plt.xlabel("Payoff Values")
# plt.ylabel("Strategy Number")
     
# # show plot
# plt.show()




















    
    
    
    
    
    
    
    
    
