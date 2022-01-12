#W02 Prove: Developer - Solo Code Submission
#Camden Miller
#1/12/22
import random
def show_grid(l1,l2,l3,l4,l5,l6,l7,l8,l9):
    line1 = (f"{l1}|{l2}|{l3}")
    
    line2 = (f"{l4}|{l5}|{l6}")
    
    line3 = (f"{l7}|{l8}|{l9}")
    
    XsandOs_board = (f"{line1}\n-+-+-\n{line2}\n-+-+-\n{line3}")
    print (XsandOs_board)
def user_input():
    user_inputed = input("enter a number based on where you want to go ")
    return user_inputed
def bot_input():
    print()
def edit_grid(user_input):
    if user_input == "1":
        global l1
        l1 = "X"
    if user_input == 2:
        global l2
        l2 = "X"
    if user_input == 3:
        global l3
        l3 = "X"        
    if user_input == 4:
        global l4
        l4 = "X"
    if user_input == 5:
        global l5
        l5 = "X"
    if user_input == 6:
        global l6
        l6 = "X"
    if user_input == 7:
        global l7
        l7 = "X"
    if user_input == 8:
        global l8
        l8 = "X"
    if user_input == 9:
        global l9
        l9 = "X"
def main(l1,l2,l3,l4,l5,l6,l7,l8,l9):
    order = random.randint(1,1)
    if order == 1:
        show_grid(l1,l2,l3,l4,l5,l6,l7,l8,l9)
        user_input()
        edit_grid(user_input)
        bot_input()
        show_grid(l1,l2,l3,l4,l5,l6,l7,l8,l9)
main(l1,l2,l3,l4,l5,l6,l7,l8,l9)