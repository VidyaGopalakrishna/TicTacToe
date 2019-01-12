

import turtle
import time
import random

the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]

columnone = -240.0
columntwo = -40.0
columnthree = 168.0
rowone = 150.0
rowtwo = -50.0
rowthree = -250.0
location = {0:(columnone,rowone),1:(columntwo,rowone), 2: (columnthree, rowone),
            3:(columnone,rowtwo), 4: (columntwo,rowtwo), 5:(columnthree, rowtwo),
            6:(columnone,rowthree), 7:(columntwo,rowthree), 8:(columnthree, rowthree)
            }

def o_figure(x,y):
    '''
    signature: int,int -> NoneType
    Given the current state of the game,
    draws the O piece at the position
    indicated by the parameter.
    '''
    turtle.color("navy")
    turtle.pensize(10)
    turtle.setheading(0)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()
    turtle.setheading(0)
    turtle.color("purple")
    
def x_figure(x,y):
    '''
    signature: int,int -> NoneType
    Given the current state of the game,
    draws the X piece at the position
    indicated by the parameter.
    '''
    turtle.color("mediumvioletred")
    turtle.pensize(10)
    turtle.setheading(0)
    turtle.goto(x,y+100)
    turtle.pendown()
    turtle.right(60)
    turtle.forward(100)
    turtle.penup()
    turtle.left(60)
    turtle.backward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.pendown()
    turtle.forward(50)
    turtle.backward(100)
    turtle.penup()
    turtle.right(60)
    turtle.pendown()
    turtle.penup()
    turtle.setheading(0)
    turtle.color("purple")

def draw_board(board):
    """
    signature: list(str) -> NoneType
    Given the current state of tshe game, draws
    the board on the screen, including the
    lines and the X and O pieces at the position
    indicated by the parameter.
    Hint: Write this function first!
    """
    turtle.bgcolor("ivory")
    turtle.color("dim grey")
    turtle.pensize(10)
    to_angle = 0
    turtle.setheading(to_angle)
    coordinate = 0
    turtle.heading()
    turtle.penup()
    turtle.backward(400)
    turtle.goto(-350.0, 100.0)
    turtle.pendown()
    turtle.forward(600)
    turtle.penup()
    turtle.goto(-350.0, -100.0)
    turtle.pendown()
    turtle.forward(600)
    turtle.right(90)
    turtle.penup()
    turtle.goto(-150.0,250.0)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(85.0,250.0)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.update()
    for i in range(len(board)):
        coordinate = location[i]
        if the_board[i] == "O":
            o_figure(coordinate[0],coordinate[1])
        if the_board[i] == "X":
            x_figure(coordinate[0],coordinate[1])
def do_user_move(board, x, y):
    """
    signature: list(str), int, int -> bool
    Given a list representing the state of the board
    and an x,y screen coordinate pair indicating where
    the user clicked, update the board
    with an O in the corresponding position. Your
    code will need to translate the screen coordinate
    (a pixel position where the user clicked) into the
    corresponding board position (a value between 0 and
    8 inclusive, identifying one of the 9 board positions).
    The function returns a bool indicated if
    the operation was successful: if the user
    clicks on a position that is already occupied
    or outside of the board area, the move is
    invalid, and the function should return False,
    otherise True.
    """
    columnonerange = (-350.0,-150.0)
    columntworange = (-150.0, 89.999)
    columnthreerange = (90.1111, 250.0)
    rowonerange = (83.337,250.0)
    rowtworange = (-83.337,83.33)
    rowthreerange = (-250.0,-83.337)
    location_ranges = {0:(columnonerange,rowonerange),1:(columntworange,rowonerange), 2: (columnthreerange, rowonerange),
                        3:(columnonerange,rowtworange), 4: (columntworange,rowtworange), 5:(columnthreerange, rowtworange),
                        6:(columnonerange,rowthreerange), 7:(columntworange,rowthreerange), 8:(columnthreerange, rowthreerange)
                        }
    for i in location_ranges:
        xrange = location_ranges[i][0]
        if xrange[1] >= x >= xrange[0]:
            for j in location_ranges:
                yrange = location_ranges[j][1]
                if board[j] == "_" and yrange[1] >= y >= yrange[0] and not check_game_over(the_board):
                    if i == j:
                        board[j] = "O"
                        return True
    if check_game_over(the_board):
        restart(the_board)
    #print("user clicked at "+str(x)+","+str(y))   
def check_game_over(board):
    """
    signature: list(str) -> bool
    Given the current state of the board, determine
    if the game is over, by checking for
    a three-in-a-row pattern in horizontal,
    vertical, or diagonal lines; and also if the
    game has reached a stalemate, achieved when
    the board is full and no further move is possible.
    If there is a winner or if there is a stalemante, display
    an appropriate message to the user and clear the board
    in preparation for the next round. If the game is over,
    return True, otherwise False.
    """
    winning_combinations = [[board[0],board[1],board[2]],[board[0],board[3],board[6]],
                            [board[8],board[7],board[6]],[board[8],board[4],board[0]],
                            [board[8],board[5],board[2]],[board[4],board[2],board[6]],
                            [board[4],board[7],board[1]],[board[4],board[5],board[3]]
                            ]
    for possible_combo in winning_combinations:
        for i in range (len(possible_combo)):
            if possible_combo[0]==possible_combo[1] == possible_combo[2]:
                if possible_combo[0] == "X":
                    turtle.goto(-280,321.0)
                    turtle.write("Computer Wins!", move=False, align="left", font=("Calibri(body)", 64, "bold"))
                    return True
            if possible_combo[0]==possible_combo[1] == possible_combo[2]:
                if possible_combo[0] == "O":
                    turtle.goto(-180,321.0)
                    turtle.write("You Win!", move=False, align="left", font=("Calibri(body)", 64, "bold"))
                    return True
    for i in range(len(board)):
        if board[i] == "_":
            return False
    turtle.goto(-380.0,321.0)
    turtle.write("Stalemate. Nobody Wins!", move=False, align="left", font=("Calibri(body)", 60, "bold"))
    return True

def restart(board):
    '''
    signature: list(str) -> bool
    Given the current state of the game,
    clear the board to start a new game,
    if board is clear, return True
    '''
    for i in range(len(board)):
        if board[i] != "_":
            board[i] = "_"
    turtle.clear()
    draw_board(board)
    return True
        
def winner(board):
    '''
    signature: int,int -> bool
    Given the current state of the game,
    determine if there is a winner,
    if so, return True
    '''
    
    if (board[0]!="_" and ("X" == board[0] == board[1] == board[2] or "X" == board[0] == board[3] == board[6])) or (board[8]!="_" and ("X" == board[6] == board[7] == board[8] or "X" == board[0] == board[4] == board[8] or "X" == board[2] == board[5] == board[8])) or (board[4]!="_" and ("X" == board[2] == board[4] == board[6] or "X" == board[1] == board[4] == board[7] or "X" == board[3] == board[4] == board[5])):
        return True                                                                                                                                                                                                                                                                 

    if (board[0]!="_" and ("O" == board[0] == board[1] == board[2] or "O" == board[0] == board[3] == board[6])) or (board[8]!="_" and ("O" == board[6] == board[7] == board[8] or "O" == board[0] == board[4] == board[8] or "O" == board[2] == board[5] == board[8])) or (board[4]!="_" and ("O" == board[2] == board[4] == board[6] or "O" == board[1] == board[4] == board[7] or "O" == board[3] == board[4] == board[5])):
        return True

    else:
         return False
                                                                                                                                                                                                                                                                        
def do_computer_move(board):
    """
    signature: list(str) -> NoneType
    Given a list representing the state of the board,
    select a position for the computer's move and
    update the board with an X in an appropriate
    position. The algorithm for selecting the
    computer's move shall be as follows: if it is
    possible for the computer to win in one move,
    it must do so. If the human player is able 
    to win in the next move, the computer must
    try to block it. Otherwise, the computer's
    next move may be any random, valid position
    (selected with the random.randint function).
    """

    for i in range(len(board)):
        copy_of_board = board.copy()
        if copy_of_board[i] == "_":
            copy_of_board[i] = "X"
            if winner(copy_of_board):
                board[i] = "X"
                return
    for i in range(len(board)):
        copy_of_board = board.copy()
        if copy_of_board[i] == "_":
            copy_of_board[i] = "O"
            if winner(copy_of_board):
                board[i] = "X"
                return
    while True:
        x = random.randint(0,8)
        if board[x] == "_":
            board[x] = "X"
            return
def clickhandler(x, y):
    """
    signature: int, int -> NoneType
    This function is called by turtle in response
    to a user click. The parameters are the screen
    coordinates indicating where the click happened.
    The function will call other functions. You do not
    need to modify this function, but you do need
    to understand it.
    """
    if do_user_move(the_board,x,y):
        draw_board(the_board)
        if not check_game_over(the_board):
            do_computer_move(the_board)
            draw_board(the_board)
            check_game_over(the_board)

def main():
    """
    signature: () -> NoneType
    Runs the tic-tac-toe game. You shouldn't
    need to modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    turtle.mainloop()
main()
