#W02 Prove: Developer - Solo Code Submission
#Camden Miller
#1/12/22
import random
pos = [1,2,3,4,5,6,7,8,9]
def show_grid(pos):
    line1 = (f"{pos[0]}|{pos[1]}|{pos[2]}")
    
    line2 = (f"{pos[3]}|{pos[4]}|{pos[5]}")
    
    line3 = (f"{pos[6]}|{pos[7]}|{pos[8]}")
    
    XsandOs_board = (f"{line1}\n-+-+-\n{line2}\n-+-+-\n{line3}")
    print (XsandOs_board)
def selection():
    x_or_o = input("would you like to play as (x) or (o)")
    if x_or_o == "x":
        global token
        global bot_token
        token = "X"
        bot_token = "O"
    elif x_or_o =="o":
        token = "O"
        bot_token = "X"
    else:
        print("You messed up so you will play as O")
    if random.randint(0,1) == 0:
        global first
        first = True
        
    else:
        first = False
    print (token,first)
def game_state():
    game = ""
    if pos[1] == pos[2] == pos[3]:
        game = "over"
    return game
def turn():
    while True:
        location = int(input("where would you like to go(1-9)"))
        if pos[location -1] != "X" and pos[location -1] != "O":
            pos[location-1] = token
            break;
        else:
            print("Enter a location that hasnt been used")
            continue
def bot():
    location = random.randint(0,8)
    pos[location] = bot_token
def main(game_state):
    selection()
    game = game_state()
    if first == True:
        show_grid(pos)
        while game != "over":
            turn()
            show_grid(pos)
            print()
            bot()
            show_grid(pos)
            print()
    else:
        show_grid(pos)
        while game != "over":
            bot()
            show_grid(pos)
            print()
            turn()
            show_grid(pos)
            print()
main(game_state)