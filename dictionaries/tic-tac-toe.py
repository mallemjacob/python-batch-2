theBoard = {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}


score = {
    'X' : 0,
    'O' : 0,
    'Tie': 0    
}

def updateScore(turn):
    if turn == 'X' or turn  == 'O':
        score[turn] = score[turn] + 1
    else:
        score['Tie'] = score['Tie'] + 1

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

def checkWin(turn):
    return theBoard[1] == theBoard[2] == theBoard[3] == turn or theBoard[4] == theBoard[5] == theBoard[6] == turn or theBoard[7] == theBoard[8] == theBoard[9] == turn or theBoard[1] == theBoard[5] == theBoard[9] == turn or theBoard[3] == theBoard[5] == theBoard[7] == turn or theBoard[1] == theBoard[4] == theBoard[7] == turn or theBoard[2] == theBoard[5] == theBoard[8] == turn or theBoard[3] == theBoard[6] == theBoard[9] == turn 

def checkFill(move):
    return theBoard[move] == ' '

def displayScore(display):
    return display

turn = 'X'
display = True

while True:
    print('Play or quit!')
    print('Enter q to quit or s to start!')
    userMove = input()
    if userMove == 'q':
        break
    elif userMove == 's':
        for i in range(9):
            printBoard(theBoard)
            print('Turn for ' + turn + '. Move on which space?')
            # print('Or enter to quit')
            move = input() #5
            # if move == '':
            #     display = not display
            #     break
            move = int(move)
            if move >= 1 and move <= 9 and (checkFill(move)):        
                theBoard[move] = turn
                if not checkWin(turn):
                    if turn == 'X':
                        turn = 'O'
                    else:
                        turn = 'X'
                else:
                    updateScore(turn)
                    break
            else:
                print('Wrong move!')

        if displayScore(display):
            print('***** SCORE CARD *****')
            for key, val in score.items():
                if key == 'Tie':
                    print(f"{key} : {val}", end='  ')
                else:
                    print(f"{key} Wins: {val}", end='  ')

            print('\n')
            printBoard(theBoard)

print('THE END!')