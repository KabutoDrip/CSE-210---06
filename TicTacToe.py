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
    user_inputed = int(input("enter a number based on where you want to go "))
    return user_inputed
def bot_input():
    print()
def edit_grid(user_input,l1,l2,l3,l4,l5,l6,l7,l8,l9):
    if user_input == 1:
        l1 = "X"
    if user_input == 2:
        l2 = "X"
    if user_input == 3:
        l3 = "X"        
    if user_input == 4:
        l4 = "X"
    if user_input == 5:
        l5 = "X"
    if user_input == 6:
        l6 = "X"
    if user_input == 7:
        l7 = "X"
    if user_input == 8:
        l8 = "X"
    if user_input == 9:
        l9 = "X"
    else:
        l1 = "X" 
    print(l1,l2,l3,l4,l5,l6,l7,l8,l9)
    return l1,l2,l3,l4,l5,l6,l7,l8,l9

def main():
    order = random.randint(1,1)
    if order == 1:
        l1,l2,l3,l4,l5,l6,l7,l8,l9 = 1,2,3,4,5,6,7,8,9
        show_grid("1","2","3","4","5","6","7","8","9")
        user_input()
        l1,l2,l3,l4,l5,l6,l7,l8,l9 = edit_grid(user_input,l1,l2,l3,l4,l5,l6,l7,l8,l9)
        show_grid(l1,l2,l3,l4,l5,l6,l7,l8,l9)
main()