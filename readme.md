
# WireWorld:

### What is it?
Wireworld is a cellular automaton first proposed by Brian Silverman in 1987, as part of his program Phantom Fish Tank. It subsequently
became more widely known as a result of an article in the "Computer Recreations" column of Scientific American. Wireworld is particularly
suited to simulating transistors, and Wireworld is Turing-complete.

Rule Set:
1. empty(white) → empty,
2. electron head(blue) → electron tail(red)
3. electron tail(red) → conductor(yellow)
4. conductor(yellow) → electron head(blue) if exactly one or two of the neighbouring cells are electron heads, otherwise remains conductor(yellow).

![Alt text](https://github.com/mmgrant73/wireworld/blob/master/wireworld.png?raw=true "Image-WireWorld")

[For more infomation:](https://en.wikipedia.org/wiki/Wireworld) 

### Programming:
This was written using the Processing Programming Language in Python Mode.  Processing is an open source framework that lets a user write programs 
with a visual context using javascript, java or python.  Processing has promoted software literacy, particularly within the visual arts, and 
visual literacy within technology.  And personally I think it is a great for people just getting into programming. 
[For more infomation:](https://processing.org/) 

### How to run it?
To use this program, just download the Processing IDE at https://processing.org/download/ , clone this respository.  Install and open the IDE and open 
the wireworld.pyde file.

### How to use it?
The program will begin with two wireworld example.  The top two are diode example and the bottom one represent an XOR gate.  You can do your own wireworld
example by clicking on the stop button which will stop the program in its current state.  Then click on the clear button which clears the board.  To set up
your example, just click on a square to adjust it to the color your want.  It will cycle through white, blue, red, yellow, etc for each click.  When you are
ready to run your example, click on the start button. 

Buttons:
1. Start/Stop: allows you to start or pause the program
2. Restart: Will start the program over from the start, fill the board with the two examples it started with
3. Clear: Will clear the grid to all white boxes but keep the ant at its current location

Customization:
You can set the gridsize if you choose.  At the top of the program there are two variables numrows, numcols that determine its size.  They are set by 
default to 20 X 30.  You can also set the screen size which is defined by screenx and screeny variables at the top of the program.  By default the screen
is set to 600 X 400.  You can also adjust the framerate, which will affect the speed of the program.  By default it is set to 5fps

Note: If you like this type of program, I have a project Conways' Game of Life and Langton's Ant which is other cellular automation programs.
