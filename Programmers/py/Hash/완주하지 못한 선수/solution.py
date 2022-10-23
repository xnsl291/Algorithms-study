#설명: https://blog.naver.com/baan3721/222849749015
#counter 사용
from collections import Counter

def solution(participant,completion):
    cnt = Counter(participant)
    for i in completion:
        cnt[i]-=1
    return [i for i,v in cnt.items() if v>0]
