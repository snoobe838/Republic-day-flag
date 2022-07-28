# Importing Necessary Modules
import turtle
import winsound
import time
import pyglet

# Creating a Window for the animation and setting its properties
window = turtle.Screen()
window.setup(width = 800, height = 600)
window.bgcolor('black')

# Playing Music
winsound.PlaySound('indian.wav',winsound.SND_ASYNC)


# adding an image
window.addshape('72nd Republic day 2.gif')
img = turtle.Turtle()
img.speed(2)
img.shape('72nd Republic day 2.gif')
img.goto(-240,0)


# Creating a flag


flag = turtle.Turtle()
flag.color('white')
flag.penup()
flag.setposition(-60,270)
flag.pendown()

length = 400
width = 80

def rectangle(color):
    flag.fillcolor(color)
    flag.begin_fill()
    flag.forward(length)
    flag.right(90)
    flag.forward(width)
    flag.right(90)
    flag.forward(length)
    flag.right(180)
    flag.end_fill()

rectangle("orange")
rectangle("white")
rectangle("green")

wheel = turtle.Turtle()
wheel.color("#002147")
wheel.penup()
wheel.width(2.5)
wheel.goto(146,111)
wheel.pendown()
wheel.circle(39)
wheel.penup()
wheel.goto(146,150)
wheel.pendown()

for i in range(26):
    wheel.forward(38)
    wheel.backward(38)
    wheel.right(13.8)

# Writing Text

text = turtle.Turtle()
text.speed(50)
text.hideturtle()

def write(message, pos, fonttext, fontsize,spacing,formatting, color):
    x, y = pos
    text.color(color)
    style = (fonttext,fontsize, formatting)
    text.penup()
    for char in message:
        text.goto(x, y)
        x = x+spacing
        text.pendown()
        text.write(char,font = style)
        text.penup()
        time.sleep(0.2)

write('Hello from SNOOBE',(-70,-50),'Courier',32,25,'italic','White')

button = turtle.Turtle()
button.hideturtle()
button.color('black')
button.goto(70,-280)
button.penup()

for i in range(2):
    button.pendown()
    button.color('white')
    button.begin_fill()
    button.forward(160)
    button.left(90)
    button.forward(60)
    button.left(90)
    button.penup()
    button.end_fill()
button.penup()
write("Host Flag",(80,-265),'Courier',20,15,"bold","#002147")

def button_click(x,y):
    if x>70 and x<230 and y > -280 and y< -220:
        file = "Indian-Flag.gif"
        animation = pyglet.resource.animation(file)
        sprite = pyglet.sprite.Sprite(animation)
        flag_hosting_window = pyglet.window.Window(width=sprite.width, height = sprite.height)
        green = (0)
        pyglet.gl.glClear(green)
        @flag_hosting_window.event
        def on_draw():
            flag_hosting_window.clear()
            sprite.draw()
        pyglet.app.run()
    else:
        file1 = "background.gif"
        animation1 = pyglet.resource.animation(file1)
        sprite1 = pyglet.sprite.Sprite(animation1)
        finalwindow = pyglet.window.Window(width=sprite1.width, height=sprite1.height)
        green = (0)
        pyglet.gl.glClear(green)

        @finalwindow.event
        def on_draw():
            finalwindow.clear()
            sprite1.draw()

        pyglet.app.run()

turtle.onscreenclick(button_click,1)
turtle.listen()

turtle.done()
