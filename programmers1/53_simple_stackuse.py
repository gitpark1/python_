def solution(board, moves):
    item=[]
    count=0
    
    for x in moves:
        for i in range(len(board)):
            if not board[i][x-1]==0:    #0이면 다음 줄로 이동
                item.append(board[i][x-1])  #바구니에 추가
                
                if len(item)>1:             #바구니 개수확인
                    if item[-1]==item[-2]:  #2개가 같으면
                        item.pop()
                        item.pop()
                        count+=2
                
                board[i][x-1]=0             #보드에서 인형제거
                break
    
    return count