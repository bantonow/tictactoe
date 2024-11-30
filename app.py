board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_draw(board):
    return all([cell != ' ' for row in board for cell in row])

def is_game_over(board):
    return check_winner(board, 'X') or check_winner(board, 'O') or is_draw(board)

def minimax(board, is_maximizing):
    if check_winner(board, 'X'):
        return 1  # X wins
    if check_winner(board, 'O'):
        return -1  # O wins
    if is_draw(board):
        return 0  # Draw
    
    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(board, False)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(board, True)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = float('-inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'  # Assume AI is X
                score = minimax(board, False)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

def print_board(board):
    for i, row in enumerate(board):
        print(' | '.join(row))
        if i < len(board) - 1:  # Add a separator after every row except the last one
            print('-' * 9)
    print('\n')

def play_game():
    player = 'O'  # Assume the human player is O
    ai = 'X'      # AI is X
    
    while not is_game_over(board):
        print_board(board)
        
        if player == 'O':
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] == ' ':
                board[row][col] = 'O'
                player = 'X'
        else:
            print("AI's turn...")
            move = find_best_move(board)
            if move:
                board[move[0]][move[1]] = 'X'
                player = 'O'
    
    print_board(board)
    if check_winner(board, 'X'):
        print("AI wins!")
    elif check_winner(board, 'O'):
        print("You win!")
    else:
        print("It's a draw!")

play_game()
