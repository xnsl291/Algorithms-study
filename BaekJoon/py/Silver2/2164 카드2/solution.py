# solution1 - recursive
# 맞는것 같은데 백준은 왜 틀렸다고 하지,,,? 
import sys
def card(lst):
    answer = [lst[i] for i in range(len(lst)) if i%2!=0]
    return card(answer) if len(answer)>1 else answer[0]

input_num = int(sys.stdin.readline())
print( input_num if input_num==1 else card(list(range(1,input_num+1))))



