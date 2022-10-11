def solution(n):
    big_num=n
    n_count=bin(n).count('1')
    while(1):
        big_num+=1
        if big_count:=bin(big_num).count('1')==n_count:
            break
    return big_num