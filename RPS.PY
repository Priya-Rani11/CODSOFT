import  random 
import time 
def comp_ch():
    return random.choice[('rock','paper','scissors')]

def win(userch,compc):
    if compc==userch:
        return "tie"
    #r->p r->s p->s p->r s->p s->r
    #for user r->s p->r s->p
    elif (userch=="rock" and compc=="scissors") or \
    (userch=="paper" and compc=="rock") or \
    (userch=="scissors"and compc=="paper"):
        return "user"
    else:
        return "computer"
#compscore and userscore
def score(cscore,uscore):
    print("CURRENT SCORES ARE...")
    print("user's score =         ",uscore,".")
    print("computer's score =     ",cscore,". ")

def rspgame():
    cscore=0
    uscore=0
    compc=comp_ch()
    print("wELCOME TO ROCK PAPER SCISSORS GAME")
    time.sleep(0.4)
    print("This game include 2 participants. One is computer and another is you. ")
    time.sleep(0.4)
    print("INSTRUCTION:")
    time.sleep(0.4)
    print("You have to select one choice from Rock Paper and Scissors whereas computer will choose one from these 3 .")
    time.sleep(0.4)
    print("If your and computer's choice matches then it will considered as tie otherwise \nROCK win over SCISSORS \nSCISSORS win over PAPER \nPAPER win over STONE")
    time.sleep(0.4)
    print("LET'S PLAY ROCK PAPER AND SCISSORS")
    time.sleep(0.4)
    print("To EXIT the game, type 'EXIT' .")
    time.sleep(0.4)
    while True:
    
        userch=input("Enter your choice 'ROCK','PAPER','SCISSORS' :\n").strip().lower()
        if userch not in ['rock','paper','scissors','exit']:
            print("INVALID CHOICE. \n Please enter 'ROCK','PAPER','SCISSORS'.")
            continue
        if userch=='exit':
            time.sleep(0.4)
            print("EXITING ...")
            break
        print("Computer's choice is",compc,".")
        