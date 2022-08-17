#링크: https://blog.naver.com/baan3721/222840517018
#중첩 for문 활용해서 숫자 3개 뽑은 후, 그 수가 소수인지를 판별
def solution(nums):

    cnt = 0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            for s in range(j+1, len(nums)):
                sum_num = nums[i]+nums[j]+nums[s]
                
                if len( [m for m in range(2,sum_num) if sum_num%m==0]) == 0:
                    cnt+=1
    return cnt
