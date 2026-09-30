from SimpleGraphics import *

#Set color for grass
setOutline(96,170,80)
setFill(96,170,80)
rect(0,400,800,200)

#Set color for the sky
setOutline(135,206,235)
setFill(135,206,235)
rect(0,0,800,400)

#Set color for the wall
setOutline("black")
setFill(245,222,179)
setWidth(2)
rect(200,250,399,250)

#Set color for the roof
setOutline("black")
setFill(178,60,50)
polygon(185,250,615,250,400,160,185,250)

#Set color for the door
setOutline("black")
setFill(120,76,44)
rect(260,350,80,150)

#Set color for grass the window
setOutline("black")
setFill(255,225,120)
rect(440,300,120,120)

#Two lines (vertical and horizontal) on the window
setOutline("black")
setWidth(2)
line(440,360,560,360)
line(500,300,500,420)

#Set color for the sun
setOutline(255,200,40)
setFill(255,200,40)
pieSlice(599,-200,400,400,180,270)

#Set color for the clouds
setOutline(250,250,255)
setFill(250,250,255)
ellipse(60,60,80,80)
ellipse(60,80,80,80)
ellipse(100,100,80,80)
ellipse(130,130,80,80)
ellipse(140,80,80,80)
ellipse(120,80,80,80)
ellipse(70,130,80,80)
ellipse(150,120,80,80)
ellipse(120,140,80,80)


#Sign the name
text(749,569,'Quang Nguyen')
