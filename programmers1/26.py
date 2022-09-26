def measure(num):
    nums=1
    for i in range(1,num):
        if num%i==0:
            nums+=nums
    return nums

def solution(left,right):
    answer=0
    for i in range(left,right+1):
        if measure(i)%2==0:
            answer+=i
        else:
            answer-=i
    return answer