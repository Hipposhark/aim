import pygame
from pygame.locals import*
from colors import*
from math import*


pygame.init()
pygame.mixer.init()

scrw = 1920
scrh = 1020

pygame.font.init()
def show_text(msg, x, y, color, size, _bold = False, _italic = False):
    fontobj= pygame.font.SysFont("freesans", size, bold = _bold, italic = _italic)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))

##controls
escape = False

top_left_corner = (-320, -320)
bottom_left_corner = (-320, 1020)
top_right_corner = (2240, -320)
bottom_right_corner = (2240, 1020)

top_left_point = (640,274)
bottom_left_point = (640,609)
top_right_point = (1280,274)
bottom_right_point = (1280,609)

before_point = (0, 0)
mouse_x_move = 0
mouse_y_move = 0



middle_bullet_coords = []
top_bullet_coords = []
bottom_bullet_coords = []
left_bullet_coords = []
right_bullet_coords = []

bullet_coord = (959, 510)
bullet_wall = ""

GAMESTATE = "menu"  ##menu, play
GUNSTATE = "" ##deagle, intervention, ak47

shoot = False
reload = False
hold = False


##deagle variables
deagle_reload_file = "Guns Stuff\Deagle Stuff\deagle_reload.wav"
deagle_shot_file = "Guns Stuff\Deagle Stuff\deagle_shot.wav"
deagle_zoom_in_file = ""
deagle_zoom_out_file = ""
deagle_recoil_margin = 100
deagle_recoil_subtraction = 10
deagle_recoil_time = 1
deagle_accurate = True
deagle_ammo_capacity = 8

deagle_reload_time_1 = 122 ##number of frames the sound lasts

deagle_gun_idle_image = "Guns Stuff\Deagle Stuff\deagle_idle.png"
deagle_shot_animation_sequence = ["Guns Stuff\Deagle Stuff\shooting sequence\deagle_shot_1.png", "Guns Stuff\Deagle Stuff\shooting sequence\deagle_shot_2.png", "Guns Stuff\Deagle Stuff\shooting sequence\deagle_shot_3.png", "Guns Stuff\Deagle Stuff\shooting sequence\deagle_shot_4.png", "Guns Stuff\Deagle Stuff\shooting sequence\deagle_shot_5.png", "Guns Stuff\Deagle Stuff\shooting sequence\deagle_shot_6.png", "Guns Stuff\Deagle Stuff\shooting sequence\deagle_shot_7.png", "Guns Stuff\Deagle Stuff\shooting sequence\deagle_shot_8.png"]
deagle_reload_animation_sequence = ['Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_1.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_2.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_3.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_4.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_5.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_6.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_7.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_8.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_9.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_10.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_11.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_12.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_13.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_14.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_15.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_16.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_17.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_18.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_19.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_20.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_21.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_22.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_23.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_24.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_25.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_26.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_27.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_28.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_29.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_30.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_31.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_32.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_33.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_34.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_35.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_36.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_37.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_38.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_39.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_40.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_41.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_42.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_43.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_44.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_45.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_46.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_47.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_48.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_49.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_50.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_51.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_52.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_53.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_54.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_55.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_56.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_57.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_58.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_59.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_60.png', 'Guns Stuff\\Deagle Stuff\\reloading sequence\\deagle_reload_61.png']


##gun variables CHANGE AFTER DONE WITH MENU
reload_file = deagle_reload_file
shot_file = deagle_shot_file
zoom_in_file = ""
zoom_out_file = ""
recoil_margin_1 = deagle_recoil_margin
recoil_margin_2 = deagle_recoil_margin
recoil_subtraction = deagle_recoil_subtraction
recoil_time_1 = deagle_recoil_time
recoil_time_2 = deagle_recoil_time
accurate = deagle_accurate
ammo_capacity_1 = deagle_ammo_capacity
ammo_capacity_2 = deagle_ammo_capacity

reload_time_1 = deagle_reload_time_1
reload_time_2 = deagle_reload_time_1

gun_idle_image = pygame.image.load(deagle_gun_idle_image)
shot_animation_sequence = deagle_shot_animation_sequence
reload_animation_sequence = deagle_reload_animation_sequence

display_surface = pygame.display.set_mode((scrw, scrh ))

deagle_border = c_black()
ak47_border = c_black()
intervention_border = c_black()


play_border = c_black()
play = False

##control variables
shift = False
shift_height_1 = 0
shift_height_2 = 0
jump = False
jump_height = 0
moving_left = False
moving_right = False
movement_velocity = 0


####################################################################################################################################################################################################
##FUNCTIONS
##calculates distance between 2 points
def dist(point_1, point_2):
  return sqrt(((point_1[0]-point_2[0])**2)+((point_1[1]-point_2[1])**2))

##calculates if a point is in a given list of points of a polygon
def inside_trap(polygon, pt):
      ans = False
      for i in range(len(polygon)):
         x0, y0 = polygon[i]
         x1, y1 = polygon[(i + 1) % len(polygon)]
         if not min(y0, y1) < pt[1] <= max(y0, y1):
            continue
         if pt[0] < min(x0, x1):
            continue
         cur_x = x0 if x0 == x1 else x0 + (pt[1] - y0) * (x1 - x0) / (y1 - y0)
         ans ^= pt[0] > cur_x
      return ans

##finds the intersection of 2 sets of 2 line creating points
def intersect(point_1, point_2, point_3, point_4):

    if (point_2[0]-point_1[0]) == 0:
        if (point_4[0]-point_3[0]) != 0:
            slope_2 = ((point_4[1]-point_3[1])/(point_4[0]-point_3[0]))
            y_int_2 = (point_3[1]-slope_2*(point_3[0]))
            return (point_2[0], point_2[0]*slope_2+y_int_2)
        else:
            return (point_2[0], point_3[1])
    elif (point_4[0]-point_3[0]) == 0:
        if (point_2[0]-point_1[0]) != 0:
            slope_1 = ((point_2[1]-point_1[1])/(point_2[0]-point_1[0]))
            y_int_1 = (point_1[1]-slope_1*(point_1[0]))
            return (point_4[0], point_4[0]*slope_1+y_int_1)
        else:
            return (point_4[0], point_2[1])

    elif (((point_2[1]-point_1[1])/(point_2[0]-point_1[0])) - ((point_4[1]-point_3[1])/(point_4[0]-point_3[0]))) == 0:##prevents divide by 0 error
        slope_1 = ((point_2[1]-point_1[1])/(point_2[0]-point_1[0]))
        slope_2 = ((point_4[1]-point_3[1])/(point_4[0]-point_3[0]))
        y_int_1 = (point_1[1]-slope_1*(point_1[0]))
        y_int_2 = (point_3[1]-slope_2*(point_3[0]))

        x = (point_1[0]+point_3[0])/2
        y = slope_1*x+y_int_1

    else:
        slope_1 = ((point_2[1]-point_1[1])/(point_2[0]-point_1[0]))
        slope_2 = ((point_4[1]-point_3[1])/(point_4[0]-point_3[0]))
        y_int_1 = (point_1[1]-slope_1*(point_1[0]))
        y_int_2 = (point_3[1]-slope_2*(point_3[0]))
        x = ((y_int_2 - y_int_1)/(slope_1 - slope_2))
        y = slope_1*x+y_int_1
    return (x, y)

##finds the line where the bullet_point passes through the vanishing point of the wall.
def bullet_line(bullet_point, first_point_1, first_point_2, second_point_1, second_point_2, side="right"):
    vanishing_point = intersect(first_point_1, first_point_2, second_point_1, second_point_2)
    if side == "left":
        point_2 = intersect(first_point_1, second_point_1, vanishing_point, bullet_point)
        point_1 = intersect (first_point_2, second_point_2, vanishing_point, bullet_point)
    else:
        point_1 = intersect(first_point_1, second_point_1, vanishing_point, bullet_point)
        point_2 = intersect (first_point_2, second_point_2, vanishing_point, bullet_point)
    return [point_1, point_2]


##finds the angle with 3 given points
def angle(A, B, C):
      a = dist(B, C)
      b = dist(C, A)
      c = dist(A, B)
      return degrees(acos(( (a**2)+(c**2)-(b**2))/(2*c*a)))

##finds the leg lengths of a right triangle given the hypotenuse length and the measure of an adjacent angle
def triangle_lengths(angle, hypotenuse_length):
      y = hypotenuse_length*(cos(radians(angle)))
      x = hypotenuse_length*(sin(radians(angle)))
      return (x, y)

####################################################################################################################################################################################################
##SOUND STUFF

pygame.mixer.set_num_channels(8)
voice = pygame.mixer.Channel(5)
####################################################################################################################################################################################################

screen = pygame.display.set_mode((scrw , scrh))
clock = pygame.time.Clock()
pygame.mouse.set_pos(959, 510)
while True:
    if escape == False and GAMESTATE == "play":
        pygame.mouse.set_visible(False)

    
    
    screen.fill(c_black("light"))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if GAMESTATE == "play":
            if event.type == MOUSEMOTION and escape == False:
                if shift != True:
                    accurate = False

                mouse_x_move = event.pos[0]-before_point[0]
                mouse_y_move = event.pos[1]-before_point[1]
                before_point = event.pos
                if event.pos[0] <= 440:
                    mouse_x_move = 0
                    mouse_y_move = 0
                    before_point = (959, 510)
                    pygame.mouse.set_pos(959, 510)
                elif event.pos[1] <= 274:
                    mouse_x_move = 0
                    mouse_y_move = 0
                    before_point = (959, 510)
                    pygame.mouse.set_pos(959, 510)
                elif event.pos[1] >= 809:
                    mouse_x_move = 0
                    mouse_y_move = 0
                    before_point = (959, 510)
                    pygame.mouse.set_pos(959, 510)
                elif event.pos[0] >= 1480:
                    mouse_x_move = 0
                    mouse_y_move = 0
                    before_point = (959, 510)
                    pygame.mouse.set_pos(959, 510)
            if event.type == MOUSEBUTTONDOWN and escape == False and reload == False and ammo_capacity_1 != 0:
                ##activates shoot as true and adds bullet to list to calculate its wall and intersecting line later
                if event.button == 1:
                    if recoil_time_1 > 0:
                        accurate = False
                    recoil_time_1 = recoil_time_2
                    gun_shot_sound = pygame.mixer.Sound(shot_file)
                    gun_shot_sound.play()
                    ammo_capacity_1-=1
                    shoot = True

            if event.type == KEYDOWN and escape == False:
                if event.key == K_r:
                    if reload == False and ammo_capacity_1 < ammo_capacity_2:
                        reload_time_1-=1
                        
                        reload = True
                        gun_reload_sound = pygame.mixer.Sound(reload_file)
                        voice.play(gun_reload_sound)
                if event.key == K_m:
                    GAMESTATE = "menu"

##                if event.key == K_SPACE and jump == False:
##                    jump == True
##
                if event.key == K_LSHIFT:
                    shift = True
                    shift_height_1 = 100
                    shift_height_2 = 25
                if event.key == K_a:
                    moving_left = True
                if event.key == K_d:
                    moving_right = True
                    



                    
                    

            if event.type == KEYUP:
                if event.key == K_r:
                    reload_time_1 = reload_time_2
                    if voice.get_busy() == False:

                        
                        voice.stop()
                        
                        reload = False
                    else:
                        voice.stop()
                        reload = False

                if event.key == K_LSHIFT:
                    shift_height_1 = -100
                    shift_height_2 = -25
                    shift = False
                if event.key == K_a:
                    moving_left = False
                if event.key == K_d:
                    moving_right = False





        ##MENU CODE
        ##MENU CODE
        ##MENU CODE
        ##MENU CODE
        if GAMESTATE == "menu":
            ##wait for other stuff
            if event.type == MOUSEMOTION:
                ##Guns
                if GUNSTATE == "":
                    ##deagle
                    if event.pos[0] >= 48 and event.pos[0] <= 624 and event.pos[1] >= 51 and event.pos[1] <= 816:
                        deagle_border = c_yellow()


                    else:
                        deagle_border = c_black()
                        ak47_border = c_black()
                        intervention_border = c_black()
                ##play button
                if event.pos[0] >= 768 and event.pos[0] <= 1152 and event.pos[1] >= 850 and event.pos[1] <= 918:
                    play_border = c_yellow()
                else:
                    play_border = c_black()


            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if GUNSTATE == "":
                        if deagle_border == c_yellow():
                            GUNSTATE = "deagle"
                            deagle_border = c_yellow()

                        if ak47_border == c_yellow():
                            GUNSTATE = "ak47"
                            ak47_border = c_yellow()


                        if intervention_border == c_yellow():
                            GUNSTATE = "intervention"
                            intervention_border = c_yellow()


                    if GUNSTATE != "" and play_border == c_yellow():
                        play = True


                    if GUNSTATE != "" and play == True:
                        play = False
                        pygame.mouse.set_pos(959, 510)
                        mouse_x_move = 0
                        mouse_y_move = 0
                        GAMESTATE = "play"








        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                if escape == False:
                    escape = True
                else:
                    escape = False





##DETERMINES GUN POINT
##DETERMINES GUN POINT
##DETERMINES GUN POINT
##DETERMINES GUN POINT
##DETERMINES GUN POINT
##DETERMINES GUN POINT
##DETERMINES GUN POINT
##DETERMINES GUN POINT
    bullet_coord = (959, 510)
    if accurate == False:
        recoil_margin_1 = recoil_margin_2
        accurate = True

    bullet_coord = list(bullet_coord)
    if recoil_margin_1 > 0:
        recoil_margin_1 -= randint(recoil_subtraction-15, recoil_subtraction+15)
        side_to_side = choice([1, -1])
        bullet_coord[0] = bullet_coord[0]+(randint(0, 20)*side_to_side)

        bullet_coord[1]-=recoil_margin_1

    elif recoil_margin_1 <= 0:
        recoil_margin_1 = 0
    bullet_coord = tuple(bullet_coord)

##Does recoil stuff
    if recoil_time_1 > 0:
        recoil_time_1-=(1/60)
    if recoil_time_1 < 0:
        recoil_time_1 = 0

##Does reload stuff
    if reload_time_1 <122:
        reload_time_1-=1
        
    if reload_time_1 == 0:
        ammo_capacity_1 = ammo_capacity_2
        reload_time_1 = reload_time_2
        
## calculates shift distance
    if shift == True:

        bottom_small_dist = dist(intersect(bottom_left_point, bottom_left_corner, top_left_point, top_left_corner), bottom_left_point)
        bottom_long_dist = dist(intersect(bottom_left_point, bottom_left_corner, top_left_point, top_left_corner), bottom_left_corner)
        ratio = bottom_small_dist/bottom_long_dist
        shift_height_2 = ratio*100

        
##        top_left_corner = list(top_left_corner)
##        bottom_left_corner = list(bottom_left_corner)
##        top_right_corner = list(top_right_corner)
##        bottom_right_corner = list(bottom_right_corner)
##        top_left_corner[1] += shift_height_2
##        bottom_left_corner[1] += shift_height_2
##        top_right_corner[1] += shift_height_2
##        bottom_right_corner[1] += shift_height_2
##        top_left_corner = tuple(top_left_corner)
##        bottom_left_corner = tuple(bottom_left_corner)
##        top_right_corner = tuple(top_right_corner)
##        bottom_right_corner = tuple(bottom_right_corner)
        
    

##GAMESTATES
##GAMESTATES
##GAMESTATES
##GAMESTATES
##GAMESTATES
##GAMESTATES
##GAMESTATES
##GAMESTATES
##GAMESTATES
    
    if GAMESTATE == "play":
        ##changing points of middle wall as mouse moves
        top_left_point = list(top_left_point)
        top_left_point[0]-=mouse_x_move
        top_left_point[1]-=mouse_y_move+shift_height_1
        top_left_point = tuple(top_left_point)

        bottom_left_point = list(bottom_left_point)
        bottom_left_point[0]-=mouse_x_move
        bottom_left_point[1]-=mouse_y_move+shift_height_1
        bottom_left_point = tuple(bottom_left_point)

        top_right_point = list(top_right_point)
        top_right_point[0]-=mouse_x_move
        top_right_point[1]-=mouse_y_move+shift_height_1
        top_right_point = tuple(top_right_point)

        bottom_right_point = list(bottom_right_point)
        bottom_right_point[0]-=mouse_x_move
        bottom_right_point[1]-=mouse_y_move+shift_height_1
        bottom_right_point = tuple(bottom_right_point)

        ##draws diagonal lines
        pygame.draw.line(screen, c_black(), top_left_corner, top_left_point, 2)
        pygame.draw.line(screen, c_black(), bottom_left_corner, bottom_left_point, 2)
        pygame.draw.line(screen, c_black(), bottom_right_corner, bottom_right_point, 2)
        pygame.draw.line(screen, c_black(), top_right_corner, top_right_point, 2)
        ##draws horizontal and vertical lines
        pygame.draw.line(screen, c_black(), top_left_point, top_right_point, 2)
        pygame.draw.line(screen, c_black(), top_left_point, bottom_left_point, 2)
        pygame.draw.line(screen, c_black(), top_right_point, bottom_right_point, 2)
        pygame.draw.line(screen, c_black(), bottom_left_point, bottom_right_point, 2)







        ####################################################################################################################################################################################################
        ##CALCULATING THE WALL OF THE BULLET
        """
        after a bullet is shot, algorithims will determine the wall it is on, and figure
        out the position of the line which it pases it through, with both point of that
        line lying on the horizontal/vertical sides of the wall. This information will
        be used to help move the bullet hole's position as the player looks around.

        adds [bullet_point, vertical_distance, left_wall_edge_height/right_wall_edge_height, [(x1, y1), (x2, y2)], [(x3, y3), (x3, y3)]] to the points list
        - bullet_point = the calculated bullet coordinates
        - vertical distance = the unchanging distance of the vertical line segment passing the bullet point and touching the 2 wall sides
        - first coordinate is the calculate horizontal line points

        """
        if shoot == True:
            ##middle wall
            if bullet_coord[0] > top_left_point[0] and bullet_coord[0] < top_left_point[0] + 640:
                if bullet_coord[1] > top_left_point[1] and bullet_coord[1] < top_left_point[1] + 335:
                    middle_bullet_coords.append(bullet_coord)
            ##top wall
            if inside_trap([top_left_corner, top_right_corner, top_right_point, top_left_point], bullet_coord) == True:
                line_h = bullet_line(bullet_coord, top_left_point, top_left_corner, top_right_point, top_right_corner)
                ##vanishing point
                vanishing_point = intersect((-320,-320),(top_left_point),top_right_corner,(top_right_point))
                ##find the vertical distance
                vertical_distance = dist(intersect(top_right_corner, (top_right_point), (bullet_coord), (bullet_coord[0]+1, bullet_coord[1])),bullet_coord)
                ##find top edge of the wall's height
                top_wall_edge_height = dist(top_right_point, intersect(line_h[0], line_h[1], (top_right_point),(top_left_point)))
                ##find the top distance with similarity
                top_distance = ((vertical_distance*dist(vanishing_point, top_right_point))/top_wall_edge_height)-dist(vanishing_point, top_right_point)
                ##find the point on the top wall edge vertical of the bullet point
                right_triangle_lengths = triangle_lengths(angle(vanishing_point, top_right_point, top_left_point), top_distance)
                top_wall_edge_point = (top_right_point[0] + right_triangle_lengths[0], top_right_point[1] - right_triangle_lengths[1])
                line_v = [top_wall_edge_point, (top_wall_edge_point[0]-1000, top_wall_edge_point[1])]
                ##calculates theoretical bullet coords
                bullet_coord = intersect(line_h[0], line_h[1],line_v[0], line_v[1])
                top_bullet_coords.append([bullet_coord, vertical_distance, top_wall_edge_height, line_h, line_v])
                
                
                bullet_coord = (959, 510)


            ##bottom wall
            if inside_trap([bottom_left_point, bottom_right_point, bottom_right_corner, bottom_left_corner], bullet_coord) == True:
                line_h = bullet_line(bullet_coord, bottom_left_point, bottom_left_corner, bottom_right_point, bottom_right_corner)
                ##vanishing point
                vanishing_point = intersect((-320,1020),(bottom_left_point),bottom_right_corner,(bottom_right_point))
                ##find the vertical distance
                vertical_distance = dist(intersect(bottom_right_corner,(bottom_right_point), (bullet_coord), (bullet_coord[0]+1, bullet_coord[1])),bullet_coord)
                ##find top edge of the wall's height
                bottom_wall_edge_height = dist(bottom_right_point, intersect(line_h[0], line_h[1], (bottom_right_point),(bottom_left_point)))
                ##find the top distance with similarity
                top_distance = ((vertical_distance*dist(vanishing_point, bottom_right_point))/bottom_wall_edge_height)-dist(vanishing_point, bottom_right_point)
                ##find the point on the top wall edge vertical of the bullet point
                right_triangle_lengths = triangle_lengths(angle(vanishing_point, bottom_right_point, bottom_left_point), top_distance)
                top_wall_edge_point = (bottom_right_point[0] + right_triangle_lengths[0], bottom_right_point[1] - right_triangle_lengths[1]) 
                line_v = [top_wall_edge_point, (top_wall_edge_point[0]-1000, top_wall_edge_point[1])]
                ##calculates theoretical bullet coords
                bullet_coord = intersect(line_h[0], line_h[1],line_v[0], line_v[1])
                bottom_bullet_coords.append([bullet_coord, vertical_distance, bottom_wall_edge_height, line_h, line_v])

                bullet_coord = (959, 510)



            ##left wall
            if inside_trap([top_left_corner, top_left_point, bottom_left_point, bottom_left_corner], bullet_coord) == True:
                line_h = bullet_line(bullet_coord, top_left_corner, top_left_point, bottom_left_corner, bottom_left_point)

                ##vanishing point
                vanishing_point = intersect((-320,-320),(top_left_point),bottom_left_corner,(bottom_left_point))
                ##find the vertical distance
                vertical_distance = dist(intersect((-320,-320), (top_left_point), (bullet_coord), (bullet_coord[0], bullet_coord[1]+1)),bullet_coord)
                ##find right edge of the wall's height
                right_wall_edge_height = dist(top_left_point, intersect(line_h[0], line_h[1], (top_left_point),(bottom_left_point)))
                ##find the top distance with similarity
                top_distance = ((vertical_distance*dist(vanishing_point, top_left_point))/right_wall_edge_height)-dist(vanishing_point, top_left_point)

                ##find the point on the top wall edge vertical of the bullet point
                right_triangle_lengths = triangle_lengths(angle(vanishing_point, top_left_point, bottom_left_point), top_distance)
                top_wall_edge_point = (top_left_point[0] + right_triangle_lengths[0], top_left_point[1] + right_triangle_lengths[1])

                line_v = [top_wall_edge_point, (top_wall_edge_point[0], top_wall_edge_point[1]+1)]

                ##calculates theoretical bullet coords
                bullet_coord = intersect(line_h[0], line_h[1],line_v[0], line_v[1])
                left_bullet_coords.append([bullet_coord, vertical_distance, right_wall_edge_height, line_h, line_v])

                bullet_coord = (959, 510)

            ##right wall
            if inside_trap([top_right_point, top_right_corner, bottom_right_corner, bottom_right_point], bullet_coord) == True:
                line_h = bullet_line(bullet_coord, top_right_point, top_right_corner, bottom_right_point, bottom_right_corner)

                ##vanishing point
                vanishing_point = intersect((top_right_point),top_right_corner,(bottom_right_point),bottom_right_corner)
                ##find the vertical distance
                vertical_distance = dist(intersect(top_right_point, top_right_corner, (bullet_coord), (bullet_coord[0], bullet_coord[1]+1)),bullet_coord)
                ##find left edge of the wall's height
                left_wall_edge_height = dist(top_right_point, intersect(line_h[0], line_h[1], (top_right_point),(bottom_right_point)))
                ##find the top distance with similarity
                top_distance = ((vertical_distance*dist(vanishing_point, top_right_point))/left_wall_edge_height)-dist(vanishing_point, top_right_point)
                ##find the point on the top wall edge vertical of the bullet point
                right_triangle_lengths = triangle_lengths(angle(vanishing_point, top_right_point, bottom_right_point), top_distance)
                top_wall_edge_point = (top_right_point[0] + right_triangle_lengths[0], top_right_point[1] + right_triangle_lengths[1])
                line_v = [top_wall_edge_point, (top_wall_edge_point[0], top_wall_edge_point[1]+1)]

                ##calculates theoretical bullet coords
                bullet_coord = intersect(line_h[0], line_h[1],line_v[0], line_v[1])
                right_bullet_coords.append([bullet_coord, vertical_distance, left_wall_edge_height, line_h, line_v])


                bullet_coord = (959, 510)

        ####################################################################################################################################################################################################
        ##DISPLAY EACH BULLET
        ##middle wall
        for i in range(0, len(middle_bullet_coords), 1):
            middle_bullet_coords[i] = list(middle_bullet_coords[i])
            middle_bullet_coords[i][0] = middle_bullet_coords[i][0]-mouse_x_move
            middle_bullet_coords[i][1] = middle_bullet_coords[i][1]-mouse_y_move-shift_height_1
            middle_bullet_coords[i] = tuple(middle_bullet_coords[i])
            
            pygame.draw.circle(screen, c_red(), middle_bullet_coords[i], 2)

        ##top wall
        """
        [bullet_point, vertical_distance, top_wall_edge_height, [(x1, y1), (x2, y2)], [(x3, y3), (x3, y3)]]
        """
        for i in range(0, len(top_bullet_coords), 1):
            ##first displays the lines
            top_bullet_coords[i][3][0] = list(top_bullet_coords[i][3][0])
            top_bullet_coords[i][3][0][0] = top_bullet_coords[i][3][0][0]-mouse_x_move
            top_bullet_coords[i][3][0][1] = top_bullet_coords[i][3][0][1]-mouse_y_move
            top_bullet_coords[i][3][0] = tuple(top_bullet_coords[i][3][0])

            ##vanishing point
            vanishing_point = intersect((-320,-320),(top_left_point),top_right_corner,(top_right_point))

            ##find the top distance with similarity
            top_distance = ((top_bullet_coords[i][1]*dist(vanishing_point, top_right_point))/top_bullet_coords[i][2])-dist(vanishing_point, top_right_point)

            ##find the point on the top wall edge vertical of the bullet point
            right_triangle_lengths = triangle_lengths(angle(vanishing_point, top_right_point, top_left_point), top_distance)

            top_wall_edge_point = (top_right_point[0] + right_triangle_lengths[1], top_right_point[1] - right_triangle_lengths[0])
            line_v = [top_wall_edge_point, (top_wall_edge_point[0]+10, top_wall_edge_point[1])]

            ##calculates theoretical bullet coords
            top_bullet_coords[i][4] = line_v
            top_bullet_coords[i][0] = intersect(top_bullet_coords[i][3][0], top_bullet_coords[i][3][1], line_v[0], line_v[1])
            pygame.draw.circle(screen, c_red(), top_bullet_coords[i][0], 2)
            ##pygame.draw.line(screen, c_red(), top_bullet_coords[i][4][0], top_bullet_coords[i][4][1], 2)

        ##bottom wall
        """
        [bullet_point, vertical_distance, bottom_wall_edge_height, [(x1, y1), (x2, y2)], [(x3, y3), (x3, y3)]]
        """
        for i in range(0, len(bottom_bullet_coords), 1):
            ##first displays the lines

            bottom_bullet_coords[i][3][0] = list(bottom_bullet_coords[i][3][0])
            bottom_bullet_coords[i][3][0][0] = bottom_bullet_coords[i][3][0][0]-mouse_x_move
            bottom_bullet_coords[i][3][0][1] = bottom_bullet_coords[i][3][0][1]-mouse_y_move
            bottom_bullet_coords[i][3][0] = tuple(bottom_bullet_coords[i][3][0])


            ##vanishing point
            vanishing_point = intersect((-320,1020),(bottom_left_point),bottom_right_corner,(bottom_right_point))

            ##find the top distance with similarity
            top_distance = ((bottom_bullet_coords[i][1]*dist(vanishing_point, bottom_right_point))/bottom_bullet_coords[i][2])-dist(vanishing_point, bottom_right_point)
            ##find the point on the top wall edge vertical of the bullet point
            right_triangle_lengths = triangle_lengths(angle(vanishing_point, bottom_right_point, bottom_left_point), top_distance)

            top_wall_edge_point = (bottom_right_point[0] - right_triangle_lengths[1], bottom_right_point[1] + right_triangle_lengths[0])
            line_v = [top_wall_edge_point, (top_wall_edge_point[0]+10, top_wall_edge_point[1])]
            ##calculates theoretical bullet coords
            bottom_bullet_coords[i][4] = line_v
            bottom_bullet_coords[i][0] = intersect(bottom_bullet_coords[i][3][0], bottom_bullet_coords[i][3][1], line_v[0], line_v[1])
            pygame.draw.circle(screen, c_red(), bottom_bullet_coords[i][0], 2)



        ##left wall
        """
        [bullet_point, vertical_distance, right_wall_edge_height, [(x1, y1), (x2, y2)], [(x3, y3), (x3, y3)]]
        """
        for i in range(0, len(left_bullet_coords), 1):
            ##first displays the lines
            left_bullet_coords[i][3][1] = list(left_bullet_coords[i][3][1])
            left_bullet_coords[i][3][1][0] = left_bullet_coords[i][3][1][0]-mouse_x_move
            left_bullet_coords[i][3][1][1] = left_bullet_coords[i][3][1][1]-mouse_y_move
            left_bullet_coords[i][3][1] = tuple(left_bullet_coords[i][3][1])


            ##vanishing point
            vanishing_point = intersect((-320,-320),(top_left_point),bottom_left_corner,(bottom_left_point))

            ##find the top distance with similarity
            top_distance = ((left_bullet_coords[i][1]*dist(vanishing_point, top_left_point))/left_bullet_coords[i][2])-dist(vanishing_point, top_left_point)

            ##find the point on the top wall edge vertical of the bullet point
            right_triangle_lengths = triangle_lengths(angle(vanishing_point, top_left_point, bottom_left_point), top_distance)

            top_wall_edge_point = (top_left_point[0] - right_triangle_lengths[0], top_left_point[1] - right_triangle_lengths[1])
            line_v = [top_wall_edge_point, (top_wall_edge_point[0], top_wall_edge_point[1]+1)]

            ##calculates theoretical bullet coords and swaps in list
            left_bullet_coords[i][4] = line_v
            left_bullet_coords[i][0] = intersect(left_bullet_coords[i][3][0], left_bullet_coords[i][3][1], line_v[0], line_v[1])
            pygame.draw.circle(screen, c_red(), left_bullet_coords[i][0], 2)
            ##pygame.draw.line(screen, c_red(), left_bullet_coords[i][3][0], left_bullet_coords[i][3][1], 2)

        ##right wall
        """
        [bullet_point, vertical_distance, left_wall_edge_height, [(x1, y1), (x2, y2)], [(x3, y3), (x3, y3)]]
        """
        for i in range(0, len(right_bullet_coords), 1):
            ##first displays the lines
            right_bullet_coords[i][3][0] = list(right_bullet_coords[i][3][0])
            right_bullet_coords[i][3][0][0] = right_bullet_coords[i][3][0][0]-mouse_x_move
            right_bullet_coords[i][3][0][1] = right_bullet_coords[i][3][0][1]-mouse_y_move
            right_bullet_coords[i][3][0] = tuple(right_bullet_coords[i][3][0])

            ##vanishing point
            vanishing_point = intersect((top_right_point),top_right_corner,(bottom_right_point),bottom_right_corner)
            ##find the top distance with similarity
            top_distance = ((right_bullet_coords[i][1]*dist(vanishing_point, top_right_point))/right_bullet_coords[i][2])-dist(vanishing_point, top_right_point)
            ##find the point on the top wall edge vertical of the bullet point
            right_triangle_lengths = triangle_lengths(angle(vanishing_point, top_right_point, bottom_right_point), top_distance)

            top_wall_edge_point = (top_right_point[0] + right_triangle_lengths[0], top_right_point[1] + right_triangle_lengths[1])
            line_v = [top_wall_edge_point, (top_wall_edge_point[0], top_wall_edge_point[1]+1)]

            ##calculates theoretical bullet coords and swaps in list
            right_bullet_coords[i][4] = line_v
            right_bullet_coords[i][0] = intersect(right_bullet_coords[i][3][0], right_bullet_coords[i][3][1], line_v[0], line_v[1])
            pygame.draw.circle(screen, c_red(), right_bullet_coords[i][0], 2)


        ################################################################################################################################################################################################
        ##drawing the crosshair
        pygame.draw.rect(screen, c_green("light"), (959, 505, 2, 10))
        pygame.draw.rect(screen, c_green("light"), (955, 509, 10, 2))

        ##reseting the mouse changes to 0
        mouse_x_move = 0
        mouse_y_move = 0




        ##DISPLAYS ANIMATION BOIS
        ##DISPLAYS ANIMATION BOIS
        ##DISPLAYS ANIMATION BOIS
        ##DISPLAYS ANIMATION BOIS
        ##DISPLAYS ANIMATION BOIS
        ##DISPLAYS ANIMATION BOIS

        if recoil_time_1 > 0:
            display_surface.blit(pygame.image.load(shot_animation_sequence[-round((len(shot_animation_sequence)*recoil_time_1)//recoil_time_2)-1]), (1280, 520))
        elif reload == True and reload_time_1 > 0 and reload_time_1<126:
            display_surface.blit(pygame.image.load(reload_animation_sequence[-(reload_time_1//2)]), (1280, 220))
        elif reload == False and shoot == False:
            display_surface.blit(gun_idle_image, (1280, 700))

        

        show_text(str(ammo_capacity_1)+"/"+str(ammo_capacity_2), 1800, 900, c_white, 60, _bold = True, _italic = False)

    ################################################################################################################################################################################################
    ##MENU WHERE YOU CHOOSE THE GUN
    ##MENU WHERE YOU CHOOSE THE GUN
    ################################################################################################################################################################################################
    else:
        pygame.mouse.set_visible(True)
        middle_bullet_coords = []
        top_bullet_coords = []
        bottom_bullet_coords = []
        left_bullet_coords = []
        right_bullet_coords = []

        ##deagle
        pygame.draw.rect(screen, deagle_border, (48, 51, 576, 765), 10)
        pygame.draw.rect(screen, c_white, (48, 51, 576, 765))
        deagle_model = pygame.image.load("Guns Stuff\Deagle Stuff\deagle_model.png")
        display_surface.blit(deagle_model, (48, 51))
        show_text("Desert", 154, 470, c_black(), 140, _bold = True, _italic = False)
        show_text("Eagle", 170, 640, c_black(), 140, _bold = True, _italic = False)




        ##play button
        pygame.draw.rect(screen, play_border, (768, 850, 384, 68), 10)
        pygame.draw.rect(screen, c_white, (768, 850, 384, 68))
        show_text("p  l  a  y", 887, 850, c_black(), 50, _bold = True, _italic = False)

        top_left_point = (640,274)
        bottom_left_point = (640,609)
        top_right_point = (1280,274)
        bottom_right_point = (1280,609)



    ##displaying that game is paused
    if escape == True:
        pygame.mouse.set_visible(True)
        show_text("game paused", 640, 100, c_black(), 150, _bold = True, _italic = False)
        show_text("game paused", 635, 100, c_white, 151, _bold = True, _italic = False)
        
    shift_height_1 = 0
    shift_height_2 = 0

    clock.tick(60)
    shoot = False
    pygame.display.update()
