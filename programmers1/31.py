def solution(arr):
    answer=[]
    num=arr[0]
    answer.append(num)
    for i in arr:
        if num!=i:
            answer.append(i)
            num=i
    
    return answer

    "abc abcd abcde"
    "AbC AbCd AbCdE"