def solution(n, arr1, arr2):
    answer = []
    
    i_list=[(list(bin(x))[2:]) for x in arr1]
    i2_list=[(list(bin(x))[2:]) for x in arr2]

    for x,ch in enumerate(i_list):
        if len(ch)<n:
            while(len(i_list[x])<n):
                i_list[x]=['0']+i_list[x]
            
    for x,ch in enumerate(i2_list):
        if len(ch)<n:
            while(len(i2_list[x])<n):
                i2_list[x]=['0']+i2_list[x]

    for a,b in zip(i_list,i2_list):
        sf_list=[]
        for i in range(n):
            if a[i]=='0' and b[i]=='0':
                sf_list.append(' ')
            else:
                sf_list.append('#')
        answer.append(sf_list)
        
    for x,s_list in enumerate(answer):
        answer[x]="".join(s_list)
    return answer