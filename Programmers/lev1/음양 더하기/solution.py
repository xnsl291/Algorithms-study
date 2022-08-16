def solution(absolutes,signs):
    signs_= [ -1 if i == False else 1 for i in signs ]
    return sum([i*v for i,v in zip(absolutes, signs_)])
