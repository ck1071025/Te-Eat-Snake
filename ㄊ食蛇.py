#Written by ck 11208 李逸馳
#It is recommended to run this program with 細明體, font size at least 18, using windows OS
import random
import time
import os
import msvcrt
import threading
import copy
import sys
#.....○○○○○○0
#....○○○○○○○1
#...○○○●○○○○2
#..○○○○○○○○○3
#.○○○○○○○○○○4
#○○○○○○○○○○○5
#.○○○■○○○○○○6
#..○○○□○○○○○7
#...○○□○○○○○8
#....○○○○○○○9
#.....○○○○○○10
key = "b'e'"
dire = 1
over = 0
score = 0
ogdire = 1
v = 0
print("ㄊ食蛇 by 11208 李逸馳. Usw edxzaw keys to control. Eat the fruit, and avoid going out of bounds or bumping into yourself!")
def keypress():
    global key
    global dire
    global over
    global ogdire
    global v
    while over == 0:
        if v == 0:
            continue;
        key = msvcrt.getch().decode('ASCII')
        if key.lower() == 'e':
            if ogdire != 4:
                dire = 1
            else:
                dire = ogdire
        if key.lower() == 'd':
            if ogdire != 5:
                dire = 2
            else:
                dire = ogdire
        if key.lower() == 'x':
            if ogdire != 6:
                dire = 3
            else:
                dire = ogdire
        if key.lower() == 'z':
            if ogdire != 1:
                dire = 4
            else:
                dire = ogdire
        if key.lower() == 'a':
            if ogdire != 2:
                dire = 5
            else:
                dire = ogdire
        if key.lower() == 'w':
            if ogdire != 3:
                dire = 6
            else:
                dire = ogdire
def end():
    os.system("cls")
    if over == 1:
        print("Game over! You bumped into yourself. " + "Score: " + str(score))
    if over == 2:
        print("Game over! You went out of bounds. " + "Score: " + str(score))
    gengengengengen = input("Input anything to end the game.")
    sys.exit()
def that():
    print("Customization:")
    sec = 87
    while sec == 87:
        sec = (input("How many seconds between two frames(0.05 ~ 5)? Leave blank to use default value(0.5)."))
        if sec == "":
            sec = float(0.5)
        try:
            sec = float(sec)
        except ValueError:
            print("Invalid Input!")
            sec = 87
            continue;
        else:
            if sec < 0.05 or sec > 5:
                print("Invalid Input!")
                sec = 87
                continue;
    sidelen = 87
    while sidelen == 87:
        sidelen = (input("Side length of the field(1~20)? Leave blank to use default value(6)."))
        if(sidelen == ""):
            sidelen = 6
        try:
            sidelen = int(sidelen)
        except ValueError:
            print("Invalid Input!")
            sidelen = 87
            continue;
        else:
            if sidelen < 1 or sidelen > 20:
                print("Invalid Input!")
                sidelen = 87
                continue;
    #grid = [[0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0]]
    temp = []
    for qq in range(sidelen * (-1) + 1, sidelen):
        temp.append([0] * (sidelen * 2 - 1 - abs(qq)))
    grid = copy.deepcopy(temp)
    fry = random.randint(0,sidelen * 2 - 2)
    frx = random.randint(0,sidelen * 2 - 2 - abs(fry - sidelen + 1))
    snx = -1
    sny = sidelen * 2 - 1
    wholex = []
    wholey = []
    global dire
    global over
    global score
    global ogdire
    global v
    longer = 0
    aaa.start()
    while True:
        os.system("cls")
        if longer == 1:
            if len(wholex) == 0:
                wholex.append(snx)
                wholey.append(sny)
            else:
                wholex.append(wholex[len(wholex) - 1])
                wholey.append(wholey[len(wholey) - 1])
        for l in range(len(wholex) - longer - 1, 0, -1):
                wholex[l] = wholex[l - 1]
                wholey[l] = wholey[l - 1]
        if(len(wholex) > 0):
            wholex[0] = snx
            wholey[0] = sny
        if(True):
            longer = 0
        if dire == 1:
            if sny > sidelen - 1:
                snx += 1
            sny -= 1
        if dire == 2:
            snx += 1
        if dire == 3:
            if sny < sidelen - 1:
                snx += 1
            sny += 1
        if dire == 4:
            if sny > sidelen - 2:
                snx -= 1
            sny += 1
        if dire == 5:
            snx -= 1
        if dire == 6:
            if sny < sidelen:
                snx -= 1
            sny -= 1
        ogdire = dire
        v = 87
        if sny > sidelen * 2 - 2 or sny < 0 or snx < 0 or snx > sidelen * 2 - 2 - abs(sny - sidelen + 1):
            over = 2
            end()
            break;
        for gen in range(len(wholex)):
            if(wholex[gen] == snx and wholey[gen] == sny):
                over = 1
                end()
                break;
        if snx == frx and sny == fry:
            score += 1
            longer = 1
            fry = random.randint(0,sidelen * 2 - 2)
            frx = random.randint(0,sidelen * 2 - 2 - abs(fry - sidelen + 1))
        #grid = [[0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0]]
        grid = copy.deepcopy(temp)
        for i in range(len(wholex)):
            grid[wholey[i]][wholex[i]] = 1
        grid[fry][frx] = 2
        grid[sny][snx] = 3
        for o in range(sidelen * 2 - 1):
            for w in range(abs(sidelen - 1 - o)):
                print(".", sep = "", end = "")
            for p in range(len(grid[o])):
                if grid[o][p] == 0:
                    print("○", sep = "", end = "")
                if grid[o][p] == 1:
                    print("□", sep = "", end = "")
                if grid[o][p] == 2:
                    print("●", sep = "", end = "")
                if grid[o][p] == 3:
                    print("■", sep = "", end = "")
            print("")
        print("Score:", score)
        time.sleep(sec)
aaa = threading.Thread(target = keypress)
bbb = threading.Thread(target = that)
bbb.start()      
    

