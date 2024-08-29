import  random 
import time 
def comp_ch():
    return random.choice(['rock','paper','scissors'])
#com_ch & comc ->computer choice , userch->user choice
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
def score(cscore,uscore,r):
    
    print("Your score =          ",uscore)
    print("Computer's score =      ",cscore)
    print()
    print("Total number of rounds =",r)
    print()
#r-> number of rounds
def rspgame():
    cscore=0
    uscore=0
    r=0
    compc=comp_ch()
    
    print("...WELCOME TO ROCK PAPER SCISSORS GAME...")
    print()
    time.sleep(0.6)
    print("This game include 2 participants. One is computer and another is you. ")
    time.sleep(0.6)
    print()

    print("INSTRUCTION:")
    time.sleep(0.6)
    print("You have to select one choice from Rock, Paper and Scissors and computer will choose one from these 3 as well .")
    time.sleep(1.0)
    print("If your and computer's choice matches then it will be considered as a tie otherwise \nROCK wins over SCISSORS \nSCISSORS win over PAPER \nPAPER wins over STONE")
    time.sleep(1.2)
    print()
    print("LET'S PLAY ROCK PAPER AND SCISSORS")
    time.sleep(0.6)
    print()
    print("To EXIT the game, type 'EXIT' .")
    time.sleep(0.4)
    while True:
    
        userch=input("Enter your choice 'ROCK','PAPER','SCISSORS' :\n").strip().lower()
        r+=1
        if userch not in ['rock','paper','scissors','exit']:
            print("INVALID CHOICE. \nPlease enter from 'ROCK','PAPER','SCISSORS'.")
            r-=1
            continue
        if userch=='exit':
            time.sleep(0.4)
            print("EXITING ...")
            break
        winn=win(userch,compc)
        print("Computer's choice is",compc,".")
        time.sleep(0.4)
        if winn=='tie':
            print("It's a tie.")
        elif winn=='user':
            uscore+=1
            print(f"BRAVO! You win round -> {r}")
            print()
        else:
            cscore+=1
            print(f"Alas! You lost \nComputer wins round -> {r}")
            print()
        print("CURRENT SCORE is...")
        score(cscore,uscore,r)
#pagain-> to play another round
        while True:
            print("Do you want to play another round?")

            pagain=input("Yes/No:").strip().lower()
            print()
            if pagain not in ['yes','no']:
                print("Enter valid option:")
                continue
            elif pagain =='yes':
                break
            else:
                print("Thanks for playing")
                time.sleep(0.3)
                print("Final Score :")
                score(cscore,uscore,r)
                time.sleep(0.3)
                print("EXITING...")
                break
        if pagain=='no':
            print("KINDLY SHARE YOUR EXPERIENCE")
            fd=input(":")
            print("Thanks for your feedback")
            break
#fd -> feedback


rspgame()
