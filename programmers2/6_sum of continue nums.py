def solution(n):
    #1~n까지의 합 n(n+1)//2
    # a + a+1 + a+2 ..... a+k-1 = n이 되는 모든 경우의 수
    # k(2a+k-1)//2 = n
    # 2a+k-1=2n/k , 2a=2n/k-(k-1), a =n/k -(k-1)//2 , a,k 모두 자연수 즉 k는 n의 약수이자 홀수
    #  return len([i for i in range(1,n+1,2) if n%i==0] )
    # 수학공식을 적용하여 푸는 방법은 정확하게 이해가 되지 X
    
    count=0
    for i in range(1,(n//2)+1):
        # n//2이상의 수의 연속된 합으로는 n을 표현 불가(n보다 더 커짐)
        sum=0
        while sum<n:
            sum+=i
            i+=1
        if sum==n:
            count+=1
    
    return count+1
            
    