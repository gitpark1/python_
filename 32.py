def solution(s):
    t_list=s.split(' ')
    sample=''
    for i in t_list:
        for x in range(len(i)):
            if x%2==0:
                sample+=i[x].upper()
            else:
                sample+=i[x].lower()
        sample+=' '
    answer=sample[:-1]
    return answer

#def toWeirdCase(s):
  #" ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))