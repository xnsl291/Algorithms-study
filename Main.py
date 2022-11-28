# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def game(num):
    victory = False 
    if(( num //3 + num%3)%2 !=0 ):
        victory = True
    return victory


total_num = int(input())
candy_nums =  list(input().split() ) 
record = [ game(int(candy_nums[i])) for i in range(total_num) ] 
if (sum(record) < (total_num - sum(record))):
    print(total_num - sum(record))
else :
    print( sum(record) if (sum(record) > (total_num - sum(record))) else "tie")