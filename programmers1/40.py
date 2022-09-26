def solution(s):
    answer = 0
    nums={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}    
    ans=[]
    change=""
    for ch in s:
        if ch.isdigit():
            if change in nums:      
                ans.append(nums[change])
                change=""
            ans.append(int(ch))
        else:
            if change in nums:      
                ans.append(nums[change])
                change=""
            change+=ch
    
    if change in nums:      
                ans.append(nums[change])
    return int("".join(list(map(str,ans))))
