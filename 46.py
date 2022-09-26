from itertools import combinations
from math import sqrt
def solution(nums):
    answer = -1
    comb_num=list(combinations(nums,3))
    sum_num=list(map(sum,comb_num))
    count=0
      
    for i in sum_num:
        check=True
        for x in range(2,int(sqrt(i))+1):
            if(i%x==0):
                check=False
                break
        if check:
            count+=1
        

    return count