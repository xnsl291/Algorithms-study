def solution(nums):
    target = len(nums)//2
    num_set = set(nums)
    
    return len(num_set) if target>len(num_set) else target
