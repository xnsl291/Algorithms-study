#정리링크: https://blog.naver.com/baan3721/222840517018
#중첩 for문 활용해서 숫자 3개 뽑은 후, 그 수가 소수인지를 판별
def solution1(nums):

    cnt = 0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            for s in range(j+1, len(nums)):
                sum_num = nums[i]+nums[j]+nums[s]
                if len( [m for m in range(2,sum_num) if sum_num%m==0]) == 0:
                    cnt+=1
    return cnt
    
# update ver. 
# combination 사용 (3개씩 숫자 조합)
# 소수판별 - 조합의 합 % (1~합)=0 인것의 개수가 2인 경우의 수 찾기 

from itertools import combinations
def solution2(nums):
    cnt = 0
    for i in combinations(nums,3):
        if len([j for j in range(1,sum(i)+1) if sum(i) % j ==0]) == 2:
            cnt+=1
    return cnt
