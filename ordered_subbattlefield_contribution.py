#Determines largest contributing sub-battlefield
def Largest(Payoff_Bank, payoff_matrix):
    max_laws=max(payoff_matrix[0][0],payoff_matrix[1][0], payoff_matrix[2][0])
    max_reserves=max(payoff_matrix[0][1],payoff_matrix[1][1], payoff_matrix[2][1])
    max_community=max(payoff_matrix[0][2],payoff_matrix[1][2], payoff_matrix[2][2])
    return(max_laws, max_reserves, max_community)

#Determines second largest contributing sub-battlefield
def Second_and_Third_Largest(Payoff_Bank, payoff_matrix):
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
           

