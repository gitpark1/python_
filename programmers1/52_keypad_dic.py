def solution(numbers, hand):

    keypad={'1':[0,0],'2':[0,1],'3':[0,2],
            '4':[1,0],'5':[1,1],'6':[1,2],
            '7':[2,0],'8':[2,1],'9':[2,2],
            '*':[3,0],'0':[3,1],'#':[3,2]
           }

    lfinger=keypad['*']
    rfinger=keypad['#']
    ans=""

    for x in numbers:
        numpos=keypad[str(x)]       #눌러야 할 숫자의 위치

        if x in [1,4,7]:
            lfinger=numpos
            ans+='L'

        elif x in [3,6,9]:
            rfinger=numpos
            ans+='R'

        else:   #x in [2,5,8,0]
            ldis=0
            rdis=0

            for a,b,c in zip(lfinger,rfinger,numpos):
                ldis+=abs(a-c)
                rdis+=abs(b-c)

            if ldis<rdis:   #왼쪽이 더 가깝다면
                lfinger=numpos
                ans+='L'

            elif rdis<ldis: #오른쪽이 더 가깝다면
                rfinger=numpos
                ans+='R'

            else:   #거리가 같다면
                if hand=="right":
                    rfinger=numpos
                    ans+='R'
                else:
                    lfinger=numpos
                    ans+='L'

    return ans