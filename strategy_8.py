import numpy as np
import random
from ordered_subbattlefield_contribution import Largest, Second_and_Third_Largest

def Strategy_8(r, keep_playing, Payoff_Bank, payoff_matrix, budget, strat, percent_contribution_cat):  
    
    
    ##### Strategy 8 #####
    max_percent=max(percent_contribution_cat[0], percent_contribution_cat[1], percent_contribution_cat[2])
    if percent_contribution_cat[0]==percent_contribution_cat[1]==percent_contribution_cat[2]:
          for j in range(3):
              for i in range(3):
                  strat[j][i]=budget[j]/3
    else:   
        if  percent_contribution_cat[0]==percent_contribution_cat[1]==max_percent or\
            percent_contribution_cat[0]==percent_contribution_cat[2]==max_percent or\
            percent_contribution_cat[1]==percent_contribution_cat[2]==max_percent:
                
            if percent_contribution_cat[0]==percent_contribution_cat[1]==max_percent:
                r=random.randint(0, 100)
                if r<50:
                    max_pos=0
                    sec_max_pos=1
                else:
                    max_pos=1
                    sec_max_pos=0
            if percent_contribution_cat[0]==percent_contribution_cat[2]==max_percent:
                r=random.randint(0, 100)
                if r<50:
                    max_pos=0
                    sec_max_pos=2
                else:
                    max_pos=2
                    sec_max_pos=0
            if percent_contribution_cat[1]==percent_contribution_cat[2]==max_percent:
                r=random.randint(0, 100)
                if r<50:
                    max_pos=1
                    sec_max_pos=2
                else:
                    max_pos=2
                    sec_max_pos=1
        else:
            if percent_contribution_cat[0]==max_percent:
                max_pos=0
            if percent_contribution_cat[1]==max_percent:
                max_pos=1
            if percent_contribution_cat[2]==max_percent:
                max_pos=2
                
            ordered_percent=[percent_contribution_cat[0], percent_contribution_cat[1], percent_contribution_cat[2]]
            ordered_percent.sort()
            sec_max_percent=ordered_percent[1]
            
        if  (percent_contribution_cat[0]==max_percent and percent_contribution_cat[0]!=percent_contribution_cat[1]) or\
            (percent_contribution_cat[0]==max_percent and percent_contribution_cat[0]!=percent_contribution_cat[2]) or\
            (percent_contribution_cat[1]==max_percent and percent_contribution_cat[0]!=percent_contribution_cat[1]) or\
            (percent_contribution_cat[1]==max_percent and percent_contribution_cat[1]!=percent_contribution_cat[2]) or\
            (percent_contribution_cat[2]==max_percent and percent_contribution_cat[0]!=percent_contribution_cat[2]) or\
            (percent_contribution_cat[2]==max_percent and percent_contribution_cat[1]!=percent_contribution_cat[2]):
                
            
                if  percent_contribution_cat[0]==percent_contribution_cat[1]==sec_max_percent or\
                    percent_contribution_cat[0]==percent_contribution_cat[2]==sec_max_percent or\
                    percent_contribution_cat[1]==percent_contribution_cat[2]==sec_max_percent:
                        
                    if percent_contribution_cat[0]==percent_contribution_cat[1]==sec_max_percent:
                        r=random.randint(0, 100)
                        if r<50:
                            sec_max_pos=1
                        else:
                            sec_max_pos=0
                    if percent_contribution_cat[0]==percent_contribution_cat[2]==sec_max_percent:
                        r=random.randint(0, 100)
                        if r<50:
                            sec_max_pos=2
                        else:
                            sec_max_pos=0
                    if percent_contribution_cat[1]==percent_contribution_cat[2]==sec_max_percent:
                        r=random.randint(0, 100)
                        if r<50:
                            sec_max_pos=2
                        else:
                            sec_max_pos=1
                else:
                    if percent_contribution_cat[0]==sec_max_percent:
                        sec_max_pos=0
                    if percent_contribution_cat[1]==sec_max_percent:
                        sec_max_pos=1
                    if percent_contribution_cat[2]==sec_max_percent:
                        sec_max_pos=2
                        
                        
        ratio=percent_contribution_cat[max_pos]/percent_contribution_cat[sec_max_pos]
        
        for i in range(3):
            sec_strategy=budget[i]/(1+ratio)
            strat[i][sec_max_pos]=sec_strategy
            strat[i][max_pos]=ratio*sec_strategy
            
    keep_playing='no'        
    print("Strategy 8 was played")
    return(strat, keep_playing)
            
    
    