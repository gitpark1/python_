def solution(nums):
    set=[]
    for i in nums:
        if i not in set:
            set.append(i)
    return len(nums)//2 if len(nums)//2<=len(set) else len(set)
        