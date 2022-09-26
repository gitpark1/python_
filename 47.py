def solution(N, stages):
    men=len(stages)
    reach=[0]*N
    lose=[0]*N          #실패한 사람수
    
    for i in stages:
        if i>N:
            continue
        lose[i-1]+=1
    
    master=men-sum(lose)    #올클한 사람수
        
    for i in range(len(lose)):
        reach[i]=sum(lose[i:])+master   #도달한 사람수
        
    res=[y if y==0 else x/y for x,y in zip(lose,reach) ]
    ans={str(i+1):num for i,num in enumerate(res)}
    return [int(x[0]) for x in sorted(ans.items(),key=lambda x:x[1],reverse=True)]
    