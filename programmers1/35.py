def solution(s, n):
    list(s)
    t_list=[ord(x) for x in s]
    for i,num in enumerate(t_list):
        if (64<num<91 and num+n>90) or (96<num<123 and num+n>122):
            t_list[i]=num+n-26
        elif num==32:
            continue
        else:
            t_list[i]=num+n
            
    return "".join([chr(x) for x in t_list])