def solution(s):
    num_list=list(map(int,s.split()))
    
    result=[str(min(num_list)),str(max(num_list))]
    return " ".join(result)

solution("1 2 3 4")