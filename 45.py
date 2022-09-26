def solution(answers):
    answer = []
    
    a1=[1,2,3,4,5]
    a2=[2,1,2,3,2,4,2,5]
    a3=[3,3,1,1,2,2,4,4,5,5]
    
    count=[0,0,0]
    
    for i,ans in enumerate(answers):
        if ans==a1[i%5]:
            count[0]+=1
        if ans==a2[i%8]:
            count[1]+=1
        if ans==a3[i%10]:
            count[2]+=1
    m=max(count)

    return [x+1 for x in range(len(count)) if count[x]==m]        
            