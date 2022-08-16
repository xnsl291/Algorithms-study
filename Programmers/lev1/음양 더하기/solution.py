#solution 1
def solution1(absolutes,signs):
    signs_= [ -1 if i == False else 1 for i in signs ]
    return sum([i*v for i,v in zip(absolutes, signs_)])

#solution2
def solution2(absolutes,signs):
    return sum(a if s else -a for a,s in zip(absolutes,signs))
