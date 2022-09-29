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

"""
def solution(survey, choices):
    answer = ''
    RTCFJMAN = [0,0,0,0,0,0,0,0]
    str = "RTCFJMAN"
    for i in range(len(survey)):
        RTCFJMAN[str.index(survey[i][1])] += choices[i]-4           
        - 순수하게 두가지 성격중 많이 나타내는 성격을 표현하기 때문에, 비동의와 동의의 크기비교를 통해서 구할수 있다.
        - 이 코드를 다시 해석해볼것


    if(RTCFJMAN[0]>=RTCFJMAN[1]): answer+= "R"
    else: answer+="T"
    if(RTCFJMAN[2]>=RTCFJMAN[3]): answer+= "C"
    else: answer+="F"
    if(RTCFJMAN[4]>=RTCFJMAN[5]): answer+= "J"
    else: answer+="M"
    if(RTCFJMAN[6]>=RTCFJMAN[7]): answer+= "A"
    else: answer+="N"


    return answer
    """
