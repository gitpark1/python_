def solution(brown, yellow):
    answer = []
    brown-=4
    sum=brown//2
    for i in range(1,sum):
        sum-=1
        if(i*sum==yellow):
            return [sum+2,i+2]
