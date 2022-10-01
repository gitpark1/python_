def solution(s):
    
    z_count=0
    ch_count=0
    
    while len(s) !=1:
        a=s.count('0')
        s_string='1'*(len(s)-a)
        s=bin(len(s_string))[2:]
        ch_count+=1
        z_count+=a
    return [ch_count,z_count]