def solution(dartResult):
    ans=[]
    nchange={"S":1,"D":2,"T":3}
    
    dartResult=dartResult.replace("10","A")
    
    for i in dartResult:
        if i.isdigit() or i=="A":
            ans.append(10 if i=='A' else int(i))
        elif i in ["S","D","T"]:
            ans.append(ans.pop()**nchange[i])
        elif i=="*":
            num=ans.pop()
            if (len(ans)):  #*가 첫 번째가 아닌 경우
                ans[-1]*=2
            ans.append(num*2)
        else:   # i가 "#"
            ans[-1]*=-1
            
    return sum(ans)

"""
def solution(dartResult):
    n=''
    score=[]
        
    for i in dartResult:
        if i.isdigit():
            n+=i
        elif i in ["S","D","T"]:
            if i=="S":
                score.append(int(n))
            elif i=="D":
                score.append(int(n)**2)
            elif i=="T":
                score.append(int(n)**3)
            n=""
        elif i=='*':
            if len(score)>1:
                score[-2]*=2
            score[-1]*=2
        elif i=='#':
            score[-1]*=-1
      
    return sum(score)



"""