#A kinda crappy recursive Sierpinski program
#Written by j.moriarty, Fall 2021
#a few lines have been removed for class purposes...

import pygame
pygame.init()#initializes Pygame
pygame.display.set_caption("sierpinski")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
screen.fill((61, 9, 4))#paint background dark red

#midpoint function definition----------------------------------------------------
def midpoint(p1, p2):
    ans = (p1 + p2)/2
    return ans

#sierpinski function definition(recursive version)-------------------------------
def sierpinski(x1, y1, x2, y2, x3, y3, counter, isEven):
    #this counter is set up so the recursion doesn't run forever
    counter+=1
    if counter>6:
        return 0
    
    #find midpoint of each side, draw a trignale there
    
    #draw first triangles
    if counter<255 and isEven == 1:
        pygame.draw.polygon(screen, (189, 105, 15), ( ( midpoint(x1, x2) , midpoint(y1, y2) ) , ( midpoint(x2, x3), midpoint(y2, y3) ) , ( midpoint(x3, x1), midpoint(y3, y1) )  ))
    #draw second triangles   
    elif counter < 255 and isEven == -1:
        pygame.draw.polygon(screen, (145, 40, 7), ( ( midpoint(x1, x2) , midpoint(y1, y2) ) , ( midpoint(x2, x3), midpoint(y2, y3) ) , ( midpoint(x3, x1), midpoint(y3, y1) )  ))
    #draw triangles
    else:
        pygame.draw.polygon(screen, (0, 0, 0), ( ( midpoint(x1, x2) , midpoint(y1, y2) ) , ( midpoint(x2, x3), midpoint(y2, y3) ) , ( midpoint(x3, x1), midpoint(y3, y1) )  )) 
    
    
    isEven *=-1 #helps swap colors with every other call of function
    
    #RECURSIVE CALL (function is calling itself) create 3 new triangles (top, left, right)
    #top
    sierpinski(x1, y1, midpoint(x1, x2) , midpoint(y1, y2),midpoint(x3, x1), midpoint(y3, y1), counter, isEven )
    #left
    sierpinski(x2, y2, midpoint(x1, x2) , midpoint(y1, y2),midpoint(x3, x2) ,midpoint(y3, y2), counter, isEven )
    #right
    sierpinski(x3, y3, midpoint(x1, x3) , midpoint(y1, y3),midpoint(x2, x3) ,midpoint(y2, y3), counter, isEven )

#end sierpinski function definition----------------------------------------------------------------------------


#"main" function---------------------------------------------------------------------------------------------
  
#coordinate points for base triangle
#top middle    
x1 = 400
y1 = 100
#bottom left
x2 = 100
y2 = 600
#bottom right
x3 = 700
y3 = 600
pygame.draw.polygon(screen, (245, 177, 32), ((x1, y1), (x2, y2), (x3, y3))) #base triangle
sierpinski(x1, y1, x2, y2, x3, y3, 0,1)#function call

print("all done!")

#this part is just here so the pygame window doesn't close until we want it to
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: #close game window
        break
    pygame.display.flip()

#end game loop##############################################
pygame.quit()