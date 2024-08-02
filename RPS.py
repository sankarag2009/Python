
# this is the game to my kids to paly Rock Paper Scissors
from enum import Enum
from random import randrange


class option(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

def play():
    UserSelection=int(input("Enter Your Choince 1:ROCK  2:PAPER 3:SCISSORS: "))
    systemselection=randrange(1,4)
    print(f"System selected {systemselection}" )
    if (UserSelection==systemselection):
        print("Tie")
        return
    if((UserSelection==option.ROCK and systemselection==option.SCISSORS) or 
    (UserSelection==option.PAPER and systemselection==option.ROCK) or
    (UserSelection==option.SCISSORS and systemselection==option.PAPER)):
        print("You Won")
    else:
        print("System Won")

if __name__ == "__main__": 
    wanttoplay = True
    while wanttoplay==True:
        play()
        wonp=str(input("do you want to contineu (Y/N) "))
        if(wonp in ["N", "n", "No", "no", "nO", "NO"] ):
            wanttoplay = False
             