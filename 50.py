def solution(n, lost, reserve):
    answer = 0
    count=0
    
    for x in reserve[:]:
        if x in lost:
            lost.remove(x)
            reserve.remove(x)
    
    length=len(lost)
    
    for x in sorted(reserve):
        if x-1 in lost:
            count+=1
            lost.remove(x-1)
        elif x+1 in lost:
            count+=1        
            lost.remove(x+1)
    return n-length+count
