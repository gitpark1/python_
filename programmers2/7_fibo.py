def fib(n):
    f_num,s_num=0,1
    for i in range(n):
        f_num,s_num=s_num,f_num+s_num
    return f_num
        
    
def solution(n):
    return fib(n)%1234567
    
# 피보나치 수의 경우 재귀함수로 구현하는 것보다는 for문으로 구현하는 것이 자원을 훨씬 적게 사용한다.
#