from SimpleGraphics import *

x_intercept = float(input("Enter your x-coordinate (0-800): "))
y_intercept = float(input("Enter your y-intercept (0-600): "))
                    

setOutline("black")
setFill("yellow")
ellipse(x_intercept-200,y_intercept-200,400,400)

setOutline("black")
setWidth(5)
arc(x_intercept-150,y_intercept+50,300,80,180,180)

setOutline("black")
setWidth(5)
line(x_intercept-160,y_intercept+100,x_intercept-140,y_intercept+80)
line(x_intercept+140,y_intercept+80,x_intercept+160,y_intercept+100)

setOutline("black")
setFill("red")
setWidth(5)
ellipse(x_intercept-150,y_intercept-120,50,100)
ellipse(x_intercept+50,y_intercept-120,50,100)

#My name as a nose. in the original design, the nose stays at the center of the face
#so that for every coordinate the user put in. The (x,y) will be the center of the face
setColor("blue")
text(x_intercept,300,"Quang Nguyen")

