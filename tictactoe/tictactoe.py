"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for row in board:
        count += row.count(X) + row.count(O)
    return O if count % 2 == 1 else X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if cell is None:
                actions.add((row_index, cell_index))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row_index = action[0]
    cell_index = action[1]
    if board[row_index][cell_index] is not None:
        raise NameError("NotValidMoveError")
    new_board = copy.deepcopy(board)
    new_board[row_index][cell_index] = player(new_board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == X and board[2][2] == X) and board[1][1] == X or (board[0][2] == X  and board[2][0] == X) and board[1][1] == X:
        return X
    elif (board[0][0] == O and board[2][2] == O) and board[1][1] == O or (board[0][2] == O and board[2][0] == O) and board[1][1] == O:
        return O
    for i in range(0,2):
        for row in board:
            if all(row[i] == X or cell == X for cell in row for row in board):
                return X
            elif all(row[i] == O or cell == O for cell in row for row in board):
                return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        
        return True
    for row in board:
        if any(cell == None for cell in row):
            return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board) == X else -1 if winner(board) == O else 0

def min_value(board):
    if terminal(board):
        return utility(board)
    v = 10000
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def p(board):
    if terminal(board):
        return utility(board)
    v = -10000
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
 
    if terminal(board):
        return None
    if board == initial_state():
        return (1,1) 
    scores = []
    action_list = []
    for action in actions(board):
        if player(board) == X:
            print('X')
            scores.append(min_value(result(board, action)))  
        elif player(board) == O:
            print('O')
            scores.append(max_value(result(board, action)))
        action_list.append(action)
    print(scores, action_list)
    if player(board) == X:
        return action_list[scores.index(max(scores))] 
    elif player(board) == O:
        return action_list[scores.index(min(scores))] 
print(minimax(initial_state()))