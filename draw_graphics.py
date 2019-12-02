#Name: Xueying Liu

from graphics import *
from time import *
import math
import random


# draw cloud on the left and right side of the sky based on the points using function. this function should return alist of circles.
def draw_cloud(win, x1,x2,y1,y2):
    cloud_list = []
    for i in range(11):
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        p = Point(x,y)

        cloud = Circle(p,2)
        cloud.setFill("white")
        cloud.setOutline("white")
        cloud.draw(win)
        cloud_list.append(cloud)
    return cloud_list

# draw the trunk of the tree with two points as a rectangle, calculate the circle above the tree trunk.
def draw_house_body(win, p1, p2):
    # drawing rectangle as house body.
    arectangle = Rectangle(p1,p2)
    arectangle.setFill("red")
    arectangle.setOutline("red")
    arectangle.draw(win)
    
    return
    
def draw_house(win,p1,p2,p3):
    # finding width and height of the rectangle.
    width = abs(p1.x - p2.x)
    height = abs(p1.y - p2.y)
    # finding the points for the roof polygon.
    # hint : for x values of the roof, add p1.x and p2.x by (width/3)
  
    # drawing the roof
    roof = Polygon(Point(p1.x, p2.y), Point(p1.x + width/3, p3.y), Point(p2.x + width/3,p3.y), p2)
    roof.setFill("brown")
    roof.setOutline("brown")
    roof.draw(win)
    # draw the front polygon
    front_polygon = Polygon(Point(p1.x + width,p1.y), p2, Point(p2.x + width/3, p3.y), Point(p2.x + 2*width/3,p2.y), Point(p2.x + 2*width/3,p1.y))
    front_polygon.setFill("pink")
    front_polygon.setOutline("pink")
    front_polygon.draw(win)
    return
    
    
def main():

    # Initializing Speed
    Speed = 0.4

    # creating the graphic window
    win = GraphWin("Blue sky and green field!", 800, 600)
    win.setCoords(0, 0, 40, 30)

    # set the background color  (width is 40, height is 30)
    BackGround = Rectangle(Point(0,15), Point(40, 30))
    BackGround.setFill("light blue")
    BackGround.draw(win)
    backGround_mood = "morning"

    # set the Ground color
    Ground = Rectangle(Point(0,0) , Point(40, 15))
    Ground.setFill("light Green")
    Ground.draw(win)

    # draw the sun
    sun = Circle(Point(20,25), 2)
    sun.setFill("Yellow")
    sun.setOutline("Yellow")
    sun.draw(win)

    # draw the mountain1
    Mountain1 = Polygon(Point(0,15), Point(15, 28), Point(30,15))
    Mountain1.setFill("dark green")
    Mountain1.draw(win)

    # draw the mountain2
    Mountain2 = Polygon(Point(10,15), Point(23,26), Point(40,15))
    Mountain2.setFill("dark green")
    Mountain2.draw(win)

    # === call draw_cloud function for the left side of the sky ===
    m1 = draw_cloud(win, 5,10,20,21)
  
    # === call draw_cloud function for the right side of the sky ===
    m2 = draw_cloud(win, 24,29,22,23)

    # === set text for asking user to click a point ===
    pntMsg = Point(20, 29)
    txtMsg = Text(pntMsg, "Please click the left bottom point of the house.")
    txtMsg.setStyle("bold")
    txtMsg.setTextColor("red")
    txtMsg.draw(win)
    
    # === get the lower point from user ===
    p1 = win.getMouse()
    p1.draw(win)
    p1.setFill("brown")
    
    # === change the text to ask user to click another point ===
    txtMsg.setText("Now click the upper right point of the house.")
    
    # === get the upper point from user ===

    # get point p2
    p2 = win.getMouse()
    p2.draw(win)
    p2.setFill("brown")
    
    # === call function to draw the house body ===
    draw_house_body(win, p1, p2)

    # === change the text to ask user to click another point ===
    txtMsg.setText("Now click the roof top point of the house.")
    # === get the roof top point from user ===
    
    # get point p3
    p3 = win.getMouse()
    p3.draw(win)
    p3.setFill("brown")

    # === call function to draw the roof and front of the house ===
    draw_house(win, p1, p2, p3)

    # === change the text inside text box ===
    txtMsg.setText("Please click a button.")

    # === View button ===
    button_1 = Rectangle(Point(2,3), Point(6, 5))
    button_1.setFill("yellow")
    button_1.draw(win)
    ViewMsg = Text(Point(4, 4), "Views")
    ViewMsg.setStyle("bold")
    ViewMsg.setTextColor("black")
    ViewMsg.draw(win)
    
    # === Wind buttton ===
    button_2 = Rectangle(Point(7,3), Point(11, 5))
    button_2.setFill("yellow")
    button_2.draw(win)
    ViewMsg = Text(Point(9, 4), "Wind")
    ViewMsg.setStyle("bold")
    ViewMsg.setTextColor("black")
    ViewMsg.draw(win)

    # === Speed Button ===
    button_3 = Rectangle(Point(12,3), Point(16, 5))
    button_3.setFill("yellow")
    button_3.draw(win)
    ViewMsg1 = Text(Point(14, 4), "Speed(0.4)")
    ViewMsg1.setStyle("bold")
    ViewMsg1.setTextColor("black")
    ViewMsg1.draw(win)

    # === Exit Button ===
    button_4 = Rectangle(Point(17,3), Point(21, 5))
    button_4.setFill("yellow")
    button_4.draw(win)
    ViewMsg = Text(Point(19, 4), "Exit")
    ViewMsg.setStyle("bold")
    ViewMsg.setTextColor("black")
    ViewMsg.draw(win)
    
    # check if user clicks any of the three buttons
    while True:
        
        pClick = win.getMouse()
        
        if (pClick.x > 17.0) & (pClick.x < 21.0) & (pClick.y > 3.0) & (pClick.y < 5.0) : 
            # conditions for pClick on button 4
            break
    
        elif (pClick.x > 2.0) & (pClick.x < 6.0) & (pClick.y > 3.0) & (pClick.y < 5.0) : 
            # conditions for pClick on button 1
            
            # Change scnes from morning to noon
            if backGround_mood == "morning":
                txtMsg.setText("Noon")
                sun.setFill("dark orange")
                sun.setOutline("dark orange")
                BackGround.setFill("dark blue")
                for i in range(11):
                    cloud = m1[i]
                    cloud.setFill("light grey")
                    cloud.setOutline("light grey")
                    cloud = m2[i]
                    cloud.setFill("light grey")
                    cloud.setOutline("light grey")
                backGround_mood = "noon"
            
            # Change scnes from noon to evening
            elif backGround_mood == "noon":
                txtMsg.setText("Evening")
                sun.setFill("navy")
                sun.setOutline("navy")
                BackGround.setFill("navy")
                for i in range(11):
                    cloud = m1[i]
                    cloud.setFill("grey")
                    cloud.setOutline("grey")
                    cloud = m2[i]
                    cloud.setFill("grey")
                    cloud.setOutline("grey")
                backGround_mood = "evening"

            # Change scnes from evening to morning
            elif backGround_mood == "evening":
                txtMsg.setText("Morning")
                sun.setFill("yellow")
                sun.setOutline("yellow")
                BackGround.setFill("light blue")
                for i in range(11):
                    cloud = m1[i]
                    cloud.setFill("white")
                    cloud.setOutline("white")
                    cloud = m2[i]
                    cloud.setFill("white")
                    cloud.setOutline("white")
                backGround_mood = "morning"
                txtMsg.setText("Please click a button.")
                
        elif (pClick.x > 7.0) & (pClick.x < 11.0) & (pClick.y > 3.0) & (pClick.y < 5.0) : 
            # conditions for pClick on button 2

            # Move clouds to right
            for i in range(4):
                for i in range(11):
                    cloud = m1[i]
                    cloud.move(Speed,0)
                    cloud = m2[i]
                    cloud.move(Speed,0)
                sleep(0.1)
                
        elif (pClick.x > 12.0) & (pClick.x < 16.0) & (pClick.y > 3.0) & (pClick.y < 5.0): 
            # conditions for pClick on button 3

            # Change speed and speed button text.
            Speed = round(Speed + 0.3,2)
            speed_str = str(Speed)
            ViewMsg1.setText("Speed("+speed_str+")")

    txtMsg.setText("Good Bye!")
    win.close()
    

main()
