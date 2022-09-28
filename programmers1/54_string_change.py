def solution(new_id):
    test_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'
               ,'u','v','w','x','y','z','-','_','.','0','1','2','3','4','5','6','7','8','9']
    
    f_id=new_id.lower()
    s_id=[x for x in f_id if x in test_list]    #이렇게 하지 않고 isdigit, isalpha를 활용해서 할 수도 있다.

    s_id="".join(s_id)
    
    count=0
    for x in s_id[:]:
        if x=='.':
            count+=1
        elif count>1:
            s_id=s_id.replace('.'*count,'.',1)
            count=0
        else:
            count=0
    
    s_id=s_id.strip('.')
        
    if not len(s_id):
        s_id+='a'
    
    if len(s_id)>15:
        s_id=s_id[:15]
    if s_id[-1]=='.':
        s_id=s_id[:-1]
        
    if len(s_id)<3:
        while len(s_id)<3:
            s_id+=s_id[-1]
        
    return s_id

    #정규표현식 활용해보기