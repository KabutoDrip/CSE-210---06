#W02 Prove: Developer - Solo Code Submission
#Camden Miller
#1/12/22
import random
def create_grid(user_input,bot_input):
    l1,c1,r1 = 1,2,3 
    l2,c2,r2 = 4,5,6
    l3,c3,r3 = 7,8,9
    return l1,c1,r1,l2,c2,r2,l3,c3,r3
    

    
def show_grid(l1,c1,r1,l2,c2,r2,l3,c3,r3):
    line1 = (f"{l1}|{c1}|{r1}")
    
    line2 = (f"{l2}|{c2}|{r2}")
    
    line3 = (f"{l3}|{c3}|{r3}")
    
    XsandOs_board = (f"{line1}\n-+-+-\n{line2}\n-+-+-\n{line3}")
    print (XsandOs_board)
def user_input():
    print()
def bot_input():
    print()
def main(l1,c1,r1,l2,c2,r2,l3,c3,r3):
    order = random.randint(0,1)
    if order == 1:
        user_input()
        show_grid(l1,c1,r1,l2,c2,r2,l3,c3,r3)
        bot_input()
    create_grid(user_input,bot_input)
main(1,2,3,4,5,6,7,8,9)