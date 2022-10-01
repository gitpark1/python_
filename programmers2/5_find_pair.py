def solution(s):
    check=0
    
    for x in s:
        if check<0:
            return False
        if x=='(':
            check+=1
        elif x==')':
            check-=1
    
    return True if check==0 else False