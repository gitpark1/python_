def solution(array, commands):
    answer = []
    for x in commands:
        res=sorted(array[x[0]-1:x[1]])
        answer+=[res[x[2]-1]]
    return answer