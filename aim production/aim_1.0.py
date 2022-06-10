import os
import keyboard
import random
import time


def clear():
    _ = os.system("cls")

game_end = False
round_end = False
win = True


while game_end == False and win == True:
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
            
        print(screen)                                                                                            
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
                        time.sleep(0.2)
                        break
                    elif aim_pos != target_pos:
                        round_end = True
                        game_end = True
                        win = False
                        break
            except:
                break

if win == False:
    print("nub you have lost!!!")









































