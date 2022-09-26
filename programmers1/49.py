
def solution(lottos, win_nums):

    zero_count=lottos.count(0)
    test=[x for x in lottos if x in win_nums]
    best=len(test)+zero_count
    result=[]
    result.append(7-best if best!=0 else 6)
    result.append(7-len(test) if len(test)!=0 else 6)

    return result