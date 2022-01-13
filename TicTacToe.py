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
    if pos[0] == pos[1] == pos[2]:
        game = "over"
    elif pos[3] == pos[4] == pos[5]:
        game = "over"
    elif pos[6] == pos[7] == pos[8]:
        game = "over"  
         
    elif pos[0] == pos[3] == pos[6]:
        game = "over" 
    elif pos[1] == pos[4] == pos[7]:
        game = "over"
    elif pos[2] == pos[5] == pos[8]:
        game = "over"
        
    elif pos[0] == pos[4] == pos[8]:
        game = "over"
    elif pos[2] == pos[4] == pos[6]:
        game = "over"
        
    else:
        game = "tie"
    return game
def turn():
    game_state()
    while True:
        location = int(input("where would you like to go(1-9)"))
        if pos[location -1] != "X" and pos[location -1] != "O":
            pos[location-1] = token
            break;
        else:
            print("Enter a location that hasnt been used")
            continue
def bot():
    game_state()
    while True:
        location = random.randrange(len(pos))
        if pos[location -1] != "X" and pos[location -1] != "O":
                pos[location-1] = bot_token
                break;
        else:
            continue
def main(game_state):
    selection()
    game = game_state()
    if first == True:
        show_grid(pos)
        i=1
        for i in range (4):
            turn()
            show_grid(pos)
            print()
            bot()
            show_grid(pos)
            print()
        print(game)
            
    else:
        show_grid(pos)
        i=1
        for i in range (4):
            bot()
            show_grid(pos)
            print()
            turn()
            show_grid(pos)
            print()
        print(game)
main(game_state)