import math
def solution(n):
    ans=[]
    for i in range(2,n+1):
        test=True
        for a in range(2,int(math.sqrt(i))+1):
            if(i%a==0):
                test=False
                break

        if test:
            ans.append(i)
    return len(ans)