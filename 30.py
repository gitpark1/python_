def gcd(n,m):
    ans=0
    if n==m:
        return n
    elif n>m:
        n-=m
        ans=gcd(n,m)
    else:
        m-=n
        ans=gcd(n,m)
    return ans

def lcm(n,m):
    return n*m//gcd(n,m)

def solution(n, m):
    answer = [gcd(n,m),lcm(n,m)]
    return answer