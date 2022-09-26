def solution(n):
    num=3
    count=0
    ans=[]
    answer=0

    while n>=num:
        num*=3
        count+=1

    for i in range(count,-1,-1):
        if not n//(3**i):
            ans.append(0)
        else:
            ans.append(n//3**i)
        n=n%3**i

    for i,number in enumerate(ans):
        answer+=3**i*number


    return answer