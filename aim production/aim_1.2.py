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

##start of game
type("WELCOME TO\n")
sleep(1)
type("A.I.M\n\n\n")
sleep(1)
start = input("Start?(y/n): ")
if start == "y":
    pass
else:
    game_end = True
clear()

if game_end == False:
    mode = input("Mode?(easy/medium/hard): ") ##Selects mode
    if mode == "easy":
        counter = 5
    elif mode == "medium":
        counter = 3.5
    elif mode == "hard":
        counter = 2
    sleep(0.5)
    clear()
    print("starting in... ")
    print("5")
    sleep(0.9)
    print("4")
    sleep(0.9)
    print("3")
    sleep(0.9)
    print("2")
    sleep(0.9)
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








































