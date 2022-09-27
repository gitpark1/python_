board=[[' ' for x in range(3)]for y in range(3)]

while True:

    for r in range(3):
        print("  "+board[r][0]+"|  "+board[r][1]+"| "+board[r][2])
        if (r!=2):
            print("---|---|---")

    x=int(input("x좌표 입력"))
    y=int(input("y좌표 입력"))

    if (board[x][y])!= ' ':
        print("잘못된 위치")
        continue
    else:
        board[x][y] ='x'

    done =False
    for i in range(3):
        for j in range(3):
            if board[i][j]==' 'and not done:
                print(i,j)
                board[i][j]='o'
                done=True
                break