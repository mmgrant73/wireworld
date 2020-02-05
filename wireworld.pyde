import random
import copy
'''
Wireworld - Wireworld is a cellular automaton first proposed by Brian Silverman in 1987.
             Wireworld is Turing-complete and can be used to simulate transistors

Rules:
A Wireworld cell can be in one of four different states, usually numbered 0–3 in software, modeled by colors in the examples here:
empty (black),
electron head (blue),
electron tail (red),
conductor (yellow).

As in all cellular automata, time proceeds in discrete steps called generations (sometimes "gens" or "ticks"). Cells behave as follows:
empty → empty,
electron head → electron tail,
electron tail → conductor,
conductor → electron head if exactly one or two of the neighbouring cells are electron heads, otherwise remains conductor.
'''
# Screen size (screenx, screeny)
screenx = 600
screeny = 400
# Size of the grid (numrows, numcols)
numrows = 30
numcols = 20
# Margin from the edges to the grid (marginx, marginy)
marginx = 40
marginy = 40
# Frames per second
fps = 5
# Number of times the ant has moved
generation = 0
# keeps the state of rather the program is running or stopped
status = 0
# antpos - grid location of the ant, antdir - holds the direction the ant is pointing
antpos = [0,0]
antdir = 0
# gets the pixel value for the start of the grid
lifex = (screenx-(marginx*2))/numrows
lifey = (screeny-(marginy*2))/numcols
# is an array that represent the state of the grid. 1 = white and 0 = red
# thus boxlist[1][1] = 0 means the box at grid col 1 and row 1 is white
boxlist = []
rowlist = []
templist = []
start1 = 0

def setup():
    global boxlist, fps
    size(600,400)  # might have to adjust based on the number of cells
    frameRate(fps)  # can adjusted recomment values 1-10
    background(0, 0, 0)
    setupboard()
    
def draw():
    global lifex,lifey,numcols,numrows,marginx,marginy,boxlist,status,options, start1
    background(0, 0, 0)
    drawlife()
    if(status == 0):
        docycle()
    if(start1 == 0):
        setupexample()
        start1 = 1
    drawbuttons()
    drawtext()
    
def setupboard():
    global numcols, numrows, boxlist, rowlist
    list2 = rowlist
    for l in range(numcols):
        list2 = []
        for k in range(numrows):
            list2.append(0)
        boxlist.append(list2)
        #templist = copy.deepcopy(list2)
        templist.append(list2)

def zeroboard():
    for l in range(numcols):
        for k in range(numrows):
            boxlist[l][k] = 0
            templist[l][k] = 0

def setupexample():
    # diode 1
    boxlist[2][1] = 1
    boxlist[2][2] = 3
    boxlist[2][3] = 3
    boxlist[2][4] = 3
    boxlist[2][5] = 3
    boxlist[2][6] = 3
    boxlist[1][7] = 3
    boxlist[2][7] = 3
    boxlist[3][7] = 3
    boxlist[1][8] = 3
    boxlist[3][8] = 3
    boxlist[2][9] = 3
    boxlist[2][10] = 3
    boxlist[2][11] = 3
    boxlist[2][12] = 3
    boxlist[2][13] = 3
    boxlist[2][14] = 3
    
    # diode 2
    boxlist[6][1] = 1
    boxlist[6][2] = 3
    boxlist[6][3] = 3
    boxlist[6][4] = 3
    boxlist[6][5] = 3
    boxlist[6][6] = 3
    boxlist[5][7] = 3
    boxlist[6][8] = 3
    boxlist[7][7] = 3
    boxlist[5][8] = 3

    boxlist[7][8] = 3
    boxlist[6][9] = 3
    boxlist[6][10] = 3
    boxlist[6][11] = 3
    boxlist[6][12] = 3
    boxlist[6][13] = 3
    boxlist[6][14] = 3

    # XOR Gate
    boxlist[11][1] = 1
    boxlist[10][2] = 3
    boxlist[12][2] = 2
    boxlist[10][3] = 3
    boxlist[12][3] = 3
    boxlist[10][4] = 3
    boxlist[12][4] = 3
    boxlist[10][5] = 3
    boxlist[12][5] = 3
    boxlist[10][6] = 3
    boxlist[12][6] = 3
    boxlist[10][7] = 3
    boxlist[12][7] = 3
    boxlist[10][8] = 3
    boxlist[12][8] = 3
    boxlist[10][9] = 3
    boxlist[12][9] = 3
    boxlist[11][10] = 3
    boxlist[11][11] = 3
    boxlist[11][12] = 3
    boxlist[11][13] = 3
    boxlist[11][14] = 3
    boxlist[11][15] = 3
    boxlist[12][16] = 3
    boxlist[13][15] = 3
    boxlist[13][16] = 3
    boxlist[13][17] = 3
    boxlist[13][18] = 3

    boxlist[17][1] = 1
    boxlist[16][2] = 3
    boxlist[18][2] = 2
    boxlist[16][3] = 3
    boxlist[18][3] = 3
    boxlist[16][4] = 3
    boxlist[18][4] = 3
    boxlist[16][5] = 3
    boxlist[18][5] = 3
    boxlist[16][6] = 3
    boxlist[18][6] = 3
    boxlist[16][7] = 3
    boxlist[18][7] = 3
    boxlist[16][8] = 3
    boxlist[18][8] = 3
    boxlist[16][9] = 3
    boxlist[18][9] = 3
    boxlist[17][10] = 3
    boxlist[17][11] = 3
    boxlist[17][12] = 3
    boxlist[17][13] = 3
    boxlist[17][14] = 3
    boxlist[17][15] = 3
    boxlist[16][16] = 3
    boxlist[15][15] = 3
    boxlist[15][16] = 3
    boxlist[15][17] = 3
    boxlist[15][18] = 3
    
    boxlist[14][15] = 3
    boxlist[14][18] = 3
    boxlist[14][19] = 3
    boxlist[14][20] = 3
    boxlist[14][21] = 3
    boxlist[14][22] = 3
    
  
def docycle():
    global numcols, numrows, boxlist, generation
    generation += 1
    #templist = []
    for l in range(numcols):
        for k in range(numrows):
            if(boxlist[l][k] == 3):
                num = getneigbor(l,k)
                #print("num ", num)
                if(num == 1 or num == 2):
                    templist[l][k] = 1
                else:
                    templist[l][k] = 3
                continue
            elif(boxlist[l][k] == 2):
                templist[l][k] = 3
                continue
            elif(boxlist[l][k] == 1):
                templist[l][k] = 2
                continue
    boxlist = copy.deepcopy(templist)
                    
def getneigbor(l, k):
    num = 0
    if(boxlist[l-1][k-1] == 1):
        num += 1
    if(boxlist[l-1][k] == 1):
        num += 1
    if(boxlist[l-1][k+1] == 1):
        num += 1
    if(boxlist[l][k-1] == 1):
        num += 1
    if(boxlist[l][k+1] == 1):
        num += 1
    if(boxlist[l+1][k-1] == 1):
        num += 1
    if(boxlist[l+1][k] == 1):
        num += 1
    if(boxlist[l+1][k+1] == 1):
        num += 1
    return num
        
def drawlife():
    # Draws the board
    for l in range(numcols):
        for k in range(numrows):
            if(boxlist[l][k] == 0):
                fill(255, 255, 255)
            elif(boxlist[l][k] == 1):
                fill(0, 0, 255)
            elif(boxlist[l][k] == 2):
                fill(255, 0, 0)
            else:
                fill(250, 250, 0)
            rect(marginx+(k*lifex),marginy+(l*lifey),lifex,lifey)
            
def drawbuttons():
    # Draws Buttons to screen
    #buttons - stop/start, settings, loadfile, reset
    global screenx, screeny, numrows, numcols, marginx, marginy, options
    fill(20,200,20)
    rect(marginx,screeny-(marginy*3/4),screenx/10,marginy/2)
    rect(screenx-marginx-screenx/10,screeny-(marginy*3/4),screenx/10,marginy/2)
    rect(screenx-marginx-screenx*2/10,screeny-(marginy*3/4),screenx/10,marginy/2)
    
def drawtext():
    # Draws Text to the screen
    global generation, marginx, marginy, options
    textSize(12);
    fill(200,200,200)
    text("WireWorld",100, marginy/1.5)
    text("Count "+str(generation), 450, marginy/1.5) 
    text("Restart",marginx+10,screeny-(marginy*3/4)+15)
    if(status==0):
        text("Stop",screenx-marginx-screenx/10+15,screeny-(marginy*3/4)+15)
    else:
        text("Start",screenx-marginx-screenx/10+15,screeny-(marginy*3/4)+15)
    text("Clear",screenx-marginx-screenx*2/10+15,screeny-(marginy*3/4)+15)
    
def boardclick(x,y):
    global numcols,numrows,marginx,marginy,boxlist,lifex,lifey
    for l in range(numcols):
        for k in range(numrows):
            if(x>marginx+(k*lifex) and x<marginx+(k*lifex)+lifex and y>marginy+(l*lifey) and y<marginy+(l*lifey)+lifey):
                boxlist[l][k] += 1
                if(boxlist[l][k] > 3):
                    boxlist[l][k] = 0
                    
def mousePressed():
    global numrows, numcols, marginx, marginy, screenx, screeny, boxlist, generation, status, start1, templist
    x=mouseX
    y=mouseY
    if(x>screenx-marginx-screenx*2/10 and x<screenx-marginx-screenx*2/10+screenx/10 and y>screeny-(marginy*3/4) and y<screeny-(marginy*3/4)+marginy/2):
        # Clear Button
        generation = 0
        status = 1
        start1 = 1
        zeroboard()
        return
    if(x>marginx and x<marginx+screenx/10 and y>screeny-(marginy*3/4) and y<screeny-(marginy*3/4)+marginy/2):
        # Restart
        generation = 0
        status = 0
        start1 = 0
        boxlist=[]
        setupboard()
        return
    if(x>screenx-marginx-screenx/10 and x<screenx-marginx and y>screeny-(marginy*3/4) and y<screeny-(marginy*3/4)+marginy/2):
        # Start/Stop button
        if(status==0):
            status = 1
        else:
            status = 0
        return
    boardclick(x,y)
