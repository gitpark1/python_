def solution(participant, completion):
    
    h_sum=0
    h_dic={}
    
    for x in participant:
        h_dic[hash(x)]=x
        h_sum+=hash(x)
        
    for x in completion:
        h_sum-=hash(x)
    ##asdfasda  
    return h_dic[h_sum]