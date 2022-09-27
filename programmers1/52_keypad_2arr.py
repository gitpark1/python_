def solution(numbers, hand):
    
    keypad=[[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    lfinger=[3,0]
    rfinger=[3,2]
    ans=''
    
    for x in numbers:
        if x in [1,4,7]:
            lfinger=keypad[x]
            ans+='L'
        
        elif x in [3,6,9]:
            rfinger=keypad[x]
            ans+='R'
            
        else:
            ldis=abs(lfinger[0]-keypad[x][0])+abs(lfinger[1]-keypad[x][1])
            rdis=abs(rfinger[0]-keypad[x][0])+abs(rfinger[1]-keypad[x][1])
            
            if ldis<rdis:
                lfinger=keypad[x]
                ans+='L'
            
            elif rdis<ldis:
                rfinger=keypad[x]
                ans+='R'
            
            else:
                if hand=='right':
                    rfinger=keypad[x]
                    ans+='R'
                else:
                    lfinger=keypad[x]
                    ans+='L'
            
                                                      
    return ans