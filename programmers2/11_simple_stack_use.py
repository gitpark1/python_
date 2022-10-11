def solution(s):
    stack=[]
    
    for x in s:
        stack.append(x)
        if len(stack)>1 and stack[-2]==stack[-1]:
            stack.pop()
            stack.pop()
    return 1 if len(stack)==0 else 0


    """
    def solution(s):
    answer = []
    for i in s:     
        if not(answer):                       리스트가 비어있는 경우에는 False로 리스트가 차있는 경우에는 True로 처리
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)    
    return not(answer)
    """