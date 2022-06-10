from random import*

c_white = (255, 255, 255)


def c_rand():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def c_black(shade = "dark"):
    if shade == "dark":
        return (0, 0, 0)
    elif shade == "light":
        return (169,169,169)
def c_red(shade = "normal"):
    if shade == "dark":
        return (153, 0, 0)
    elif shade == "light":
        return (255, 153, 153)
    else:
        return (255, 0, 0)

def c_green(shade = "normal"):
    if shade == "dark":
        return (0, 153, 0)
    elif shade == "light":
        return (153, 255, 153)
    else:
        return (0, 255, 0)

def c_blue(shade = "normal"):
    if shade == "dark":
        return (0, 0, 153)
    elif shade == "light":
        return (51, 153, 255)
    else:
        return (0, 0, 255)

def c_yellow(shade = "normal"):
    if shade == "dark":
        return (153, 153, 0)
    elif shade == "light":
        return (255, 255, 153)
    else:
        return (255, 255, 0)

def c_purple(shade = "normal"):
    if shade == "dark":
        return (76, 0, 153)
    elif shade == "light":
        return (204, 153, 255)
    else:
        return (127, 0, 255)

def c_orange(shade = "normal"):
    if shade == "dark":
        return (153, 76, 0)
    elif shade == "light":
        return (255, 204, 153)
    else:
        return (255, 128, 0)







