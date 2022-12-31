#solution1 - recursive
def card(lst):
    answer = [lst[i] for i in range(len(lst)) if i%2!=0]
    return card(answer) if len(answer)>1 else answer[0]


lst = list(range(1,int(input())+1))
print(card(lst))


