def solution(d, budget):
    answer = 0
    s_list=sorted(d)
    for i in s_list:
        budget-=i
        if budget<0:
            break;
        answer+=1
    return answer