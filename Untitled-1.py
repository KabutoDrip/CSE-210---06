#W02 Prove: Developer - Solo Code Submission
#Camden Miller
#1/12/22
def main():
    create_grid()
    
def create_grid():
    l=1
    c=2
    r=3
    line1 = (f"{l}|{c}|{r}")
    l,c,r = l+3, c+3, r+3
    line2 = (f"{l}|{c}|{r}")
    l,c,r = l+3, c+3, r+3
    line3 = (f"{l}|{c}|{r}")
    XsandOs_board = (f"{line1}\n-+-+-\n{line2}\n-+-+-\n{line3}")
    print (XsandOs_board)
def user_start_input():
   print()
main()