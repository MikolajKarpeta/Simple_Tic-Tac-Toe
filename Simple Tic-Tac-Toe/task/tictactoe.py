# write your code here

grid = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]

game_map = {(1, 1): 0, (1, 2): 1, (1, 3): 2,
            (2, 1): 3, (2, 2): 4, (2, 3): 5,
            (3, 1): 6, (3, 2): 7, (3, 3): 8}

which_move = 0
who_is_playing = "X"
X_win = False
O_win = False

X_win_condition = ["X","X","X"]
O_win_condition = ["O","O","O"]

print(f"""---------
| {grid[0]} {grid[1]} {grid[2]} |
| {grid[3]} {grid[4]} {grid[5]} |
| {grid[6]} {grid[7]} {grid[8]} |
---------""")
while True:

    move = input().split()
    x, y = move
    try:
        x, y = int(x), int(y)
        move = (x, y)
    except:
        print("You should enter numbers!")
    else:
        if move not in game_map:
            print("Coordinates should be from 1 to 3!")
        elif grid[game_map[move]] == "X" or grid[game_map[move]] == "O":
            print("This cell is occupied! Choose another one!")
        elif who_is_playing == "X":
            grid[game_map[move]] = "X"
            who_is_playing = "O"
            which_move += 1
        elif who_is_playing =="O":
            grid[game_map[move]] = "O"
            who_is_playing = "X"
            which_move += 1

    Row = [grid[0:3], grid[3:6], grid[6:9]]
    Column = [grid[0::3], grid[1::3], grid[2::3]]
    Diagnoal = [grid[0::4], grid[2:7:2]]
    Win_conditions = Row + Column + Diagnoal

    print(f"""---------
| {grid[0]} {grid[1]} {grid[2]} |
| {grid[3]} {grid[4]} {grid[5]} |
| {grid[6]} {grid[7]} {grid[8]} |
---------""")
    if X_win_condition in Win_conditions:
        X_win = True
    if O_win_condition in Win_conditions:
        O_win = True

    if O_win:
        print("O wins")
        break
    elif X_win:
        print("X wins")
        break
    elif which_move == 9:
        print("Draw")
        break

