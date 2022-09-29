def solution(survey, choices):
    att={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    ans=""
    tuple_list=[]
    
    for i,at in enumerate(survey):
        if choices[i]<4:
            att[at[0]]+=4-choices[i]
        elif choices[i]>4:
            att[at[1]]+=choices[i]-4
    
    dic_list=list(att.items())
    
    for i in range(0,len(dic_list),2):
        ans+=dic_list[i][0] if dic_list[i][1]>=dic_list[i+1][1] else dic_list[i+1][0]
    
    
    return ans
solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])