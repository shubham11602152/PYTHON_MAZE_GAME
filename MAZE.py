# A Simple Maze Game .
import turtle

wn = turtle.Screen() # wn-[window] , screen()-Gives us our screen.
wn.bgcolor("black")  # bgcolor()-Background colour.
wn.title("A Maze Game") # title()-Display title of the game.
wn.setup(700,700)    # setup()-setting up screen pixels need by our game

# Create Pen
class pen(turtle.Turtle) :
    def __init__(self) :
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

# Create Levels List
levels = [""]

# Define First Level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X  XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX        XXXX  XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",
    "X                XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXX                     X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XX   XXXXX              X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX    XXXXXXXXXXXX  XXXXX",
    "XXXX        XXXX        X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]
# Add maze to mazes list
levels.append(level_1)

# Create Level Setup Function
def setup_maze(level_1) :
    for y in range(len(level_1)) :
        for x in range(len(level_1[y])):
            # Get the character at each x,y coordinate
            # NOTE the order of y and x in  the next line
            character = level_1[y][x]
            # Calculate the screen x,y coordinates
            screen_x =  -288 + (x * 24)
            screen_y =   288 - (y * 24)

            # Check if it is an X (representing a wall)
            if character == "X" :
                pen.goto(screen_x , screen_y)
                pen.stamp()

# Create class instances
pen =  pen()

#set up the level
setup_maze(levels[1])

# Main Game Loop
while True :
    pass
