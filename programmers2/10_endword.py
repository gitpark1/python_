def solution(n, words):
    ans=[]
    loop=1
    num=0
    ch=words[0][0]
    for word in words:
        if word[0]==ch: ## 끝말확인
            if word not in ans:         ##처음 나온 단어
                ans.append(word)
                num+=1
                if num==n:              ##1바퀴 돈 경우
                    num=0
                    loop+=1
                ch=word[-1]
            else : ##중복, 탈락
                return [num+1,loop]
        else : ##끝말x, 탈락
            return [num+1,loop]
    else:   ##틀린사람 x
        return [0,0]
            
            
            

"""
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
"""