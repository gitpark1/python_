def solution(strings, n):
    strings.sort() 
    return sorted(strings, key=lambda x:x[n])

    ##람다식을 키값으로 정렬에 잘 활용해보기