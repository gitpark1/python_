def solution(s):
    answer = ''
    test=s.split(" ")
    for x in test:
        if len(x)!=0 :
            x=x.capitalize()
        answer+=x
        answer+=' '
    return answer[:-1] 

solution("TEST")
    #문제 조건 : s의 길이는 1이상, s는 알파벳, 숫자, 공백문자로 이루어져 있음, 공백문자가 연속해서 나올수도 있음, 숫자로만 이루어진 단어는 존재X?