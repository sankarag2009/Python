
# this is the game to my kids to paly Rock Paper Scissors
from enum import IntEnum
from random import randrange


class option(IntEnum):
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
    if((UserSelection==option.ROCK.value and systemselection==option.SCISSORS.value) or 
    (UserSelection==option.PAPER.value and systemselection==option.ROCK.value) or
    (UserSelection==option.SCISSORS.value and systemselection==option.PAPER.value)):
        print("You Won")
    else:
        print("System Won")

if __name__ == "__main__": 
    wanttoplay = True
    while wanttoplay==True:
        play()
        wonp=str(input("do you want to contineu (Y/N) "))
        if(wonp in ["n", "no"] ):
            wanttoplay = False
        elif(wonp in ["y", "yes"] ):
            wanttoplay = True
        else:
            print("Invalid oputput")

            wonp=str(input("do you want to contineu (Y/N) ")).lower
    
             