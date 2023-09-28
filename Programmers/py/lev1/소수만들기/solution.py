def solution(nums):
    cnt = 0
    range_list = []
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            for s in range(j+1, len(nums)):
                sum = nums[i]+nums[j]+nums[s]
                range_list = list(range(1,sum+1))
                tmp = [sum%range_list[n] for n in range(len(range_list))]
                if tmp.count(0) == 2:
                    cnt+=1
    return cnt
