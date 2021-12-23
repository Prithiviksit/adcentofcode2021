import numpy as np
from collections import Counter
from functools import reduce
from math import prod
import pandas as pd

# score_1=0
# score_2=0
# pos1=10
# pos2=6

# def deterministic_dice():
#     s=0
#     while True:
#         s=s%100+1
#         yield s

# dice1=deterministic_dice()

# i=0
# while(score_1<1000 and score_2<1000):
#     pos1= (pos1+next(dice1)+next(dice1)+next(dice1)-1)%10+1
#     i+=3
#     score_1+=pos1
#     if score_1>=1000:
#         break
#     pos2= (pos2+next(dice1)+next(dice1)+next(dice1)-1)%10+1
#     i+=3
#     score_2+=pos2


# print(score_1,score_2,pos1,pos2,i)
################################ Part 2 #########################################

#x=[*np.ndindex((3,3,3))]

toss=[[x,y,z] for x in [1,2,3] for y in [1,2,3] for z in [1,2,3]]
num=dict(Counter(map(sum,toss)))
print(num)





def win(score1,score2,pos1,pos2,player):
    p=[]
    if player==1:
        for key in num:
            pos1new=(pos1 +key-1)%10+1
            score1new=score1+pos1new
            if score1new>=21:
                #return([[key,pos1new,player,score1new,score2]])
                return([[key,player]])
            else:
                #p+=[[key,pos1new,player,score1]+x for x in win(score1new,score2,pos1new,pos2,2)]
                p+=[[key]+x for x in win(score1new,score2,pos1new,pos2,2)]
    elif player==2:
        for key in num:
            pos2new=(pos2 +key-1)%10+1
            score2new=score2+pos2new
            if score2new>=21:
                #return([[key,pos2new,player,score2new,score1]])
                return([[key,player]])
            else:
                #p+=[[key,pos2new,player,score2]+x for x in win(score1,score2new,pos1,pos2new,1)]
                p+=[[key]+x for x in win(score1,score2new,pos1,pos2new,1)]
    return(p)

result=win(0,0,10,6,1)

print(result[78978])
print(result[-2])

print(len(result))

def calc_univ(v):
    num_univ=prod(map(lambda x: num[x],v[:-1]))
    return([v[-1],num_univ])

print(calc_univ(result[78978]))
print(calc_univ(result[-2]))

dt=list(map(calc_univ,result))
pd.set_option('display.float_format', '{:.2f}'.format)
print(pd.DataFrame(dt,columns=["Player","Num_Univ"]).groupby("Player").sum())














# def win(step,score):
#     global p1
#     for key in num:
#         if score+key>=21:
#             return([step+1,score+key])
#         else:
#             p1+=win(step+1,score+key)
#     return(p1)
# result=win(step1,score1)
# print(result)








