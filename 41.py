from itertools import combinations

def solution(numbers):
    answer = []
    for a,b in combinations(numbers,2):
        res=a+b
        if res not in answer:
            answer.append(res)
    return sorted(answer)