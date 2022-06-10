import os
import sys
import keyboard
import random
from time import*



def clear():
    _ = os.system("cls")

def type(string):
    for char in string:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()


game_end = False
round_end = False
win = True
score = -100 ##player score

##loading
sleep(3)
loop = 0
while loop < 2:
    clear()
    print("loading |")
    sleep(0.1)
    clear()
    print('loading \\')
    sleep(0.1)
    clear()
    print("loading -")
    sleep(0.1)
    clear()
    print("loading /")
    sleep(0.1)
    loop+=1
##start of game
clear()
sleep(0.5)
type("WELCOME TO\n")
sleep(0.5)
type("A.I.M\n")
sleep(0.5)
type("A GAME BY HIPPO PRODUCTIONS\n")
sleep(0.5)
start = input("Start?(y/n): ")
if start == "y":
    pass
else:
    game_end = True
clear()

if game_end == False:
    
    sleep(1)
    rules = input("Do you wish to see the rules?(y/n): ")
    clear()
    sleep(0.5)
    if rules == "y":
        type(" How to play\n")
        sleep(0.3)
        print("=============")
        sleep(0.3)
        print("- Use the keys 'a' and 'd' to move the aim '+' left and right.\n")
        sleep(0.3)
        print("- Once you move the aim onto the target 'o', you can press 's' to shoot.\n")
        sleep(0.3)
        print("- If you miss, the game's over.\n")
        sleep(0.3)
        print("- You will be timed, but you get to choose which mode you get to play on.\n")
        sleep(0.3)
        print("- Your goal is to last as long as possible.\n")
        sleep(0.3)
        print("- Your score will be recorded: for every shot you hit, you gain 100 points.\n")
        continyou = input("Continue?(y/n): ")
        if continyou == "y":
            pass
    clear()
    mode = input("Mode?(easy/medium/hard): ") ##Selects mode
    if mode == "easy":
        counter = 5
    elif mode == "medium":
        counter = 3.5
    elif mode == "hard":
        counter = 2.7
    sleep(0.5)
    clear()
    print("starting in... ")
    print("5")
    sleep(0.5)
    print("4")
    sleep(0.5)
    print("3")
    sleep(0.5)
    print("2")
    sleep(0.5)
    print("1")
    clear()

while game_end == False :
    start_time = time()  ##game time during beeginning of a round
    
    score+=100
    if game_end == False:
        round_end = False
    pixel_list = ["|", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "+", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "|"] ##20 spaces between aim and walls
    target = "O"
    target_pos = random.choice((random.randint(1, 20), random.randint(22, 41)))
    pixel_list[target_pos] = target ## adds random target to list
    aim_pos = 21
    while round_end == False:
        clear()
        screen = ""
        pixel_list[target_pos] = target ##adds target to pixel
        if target_pos == aim_pos:
            pixel_list[target_pos] = "X" #if aim goes over target
        for pixels in pixel_list:## creates screen
            screen+=pixels
        time_now = time()
        print(screen)
        print("Your time left: " + str(counter - int(time_now-start_time)))
        print("Score: " + str(score))
        on_target = False
        while True: 
            try: 
                if keyboard.is_pressed('a'):
                    if aim_pos-1 == target_pos:## checks if the aim position is on the target position
                        on_target = True
                    if pixel_list[1] == "+": ##doesn't break through wall
                        break
                    pixel_list[aim_pos] = " " ##updates list
                    pixel_list[aim_pos-1] = "+"
                    aim_pos-=1
                    break
                elif keyboard.is_pressed('d'):
                    if aim_pos+1 == target_pos:## checks if the aim position is on the target position
                        on_target = True
                    if pixel_list[-2] == "+": ##doesn't break through wall
                        break
                    pixel_list[aim_pos] = " " ##updates list
                    pixel_list[aim_pos+1] = "+"
                    aim_pos+=1
                    break
                elif keyboard.is_pressed("s"):
                    if aim_pos == target_pos:
                        round_end = True
                        sleep(0.2)
                        break
                    elif aim_pos != target_pos:
                        round_end = True
                        game_end = True
                        win = False
                        break
                elif keyboard.is_pressed("p"):
                    pause_time = time()
                    continyou = input("press 'y' to continue: ")
                    if continyou == "y":
                        unpause_time = time()
                        paused_time = int(unpause_time-pause_time)+1
                        start_time+=paused_time
                        break
                        
            except:
                break
    end_time = time()
    if int(end_time - start_time) > counter:
        game_end = True 

if score != -100:
    if win == False:
        print("You missed!!!!\nScore: " + str(score))
    elif win == True:
        print("You shot it but ran out of time.\nScore: " + str(score))
else:
    clear()
    print("good day then")







































