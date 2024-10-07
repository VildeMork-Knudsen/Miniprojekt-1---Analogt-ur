import pygame
import math 
from datetime import datetime

#Initializing pygame
pygame.init()

#Colors
pink = (219, 112, 147)
dark_pink = (227, 11, 92)
light_pink = (255, 208, 215)

#Setting up the screen, defining center and making a pygame caption
screen_size = (400, 400)
screen = pygame.display.set_mode((screen_size))
center = [screen_size[0]//2, screen_size[1]//2]
pygame.display.set_caption("Analogt ur")

#Main loop
run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    #Updating the display
    pygame.display.flip()

    #Filling the screen with color 
    screen.fill(light_pink)

    #Making the clock circle and defining a radius
    clock_circle = pygame.draw.circle(screen, pink, (center[0],center[1]), 190)
    clock_radius = 200

    #Creating a font to be able to draw number markings + picking a size 
    font = pygame.font.Font(None, 40)      

    #Number markings   
    for i in range(1,13):  
        #Converting into radians to be able to use cos and sin
        #Adding each iteration with 30 (360/12), which is how much
        #we want the numbers to move position each time
        #Subtracting 90 so that the numbers are placed from the top, 
        #and not to the right (which is 0 degrees this our case)           
        angle = math.radians(i * 30 - 90) 

        x = center[0] + (clock_radius - 43) * math.cos(angle)
        y = center[1] + (clock_radius - 43) * math.sin(angle)

        #Rendering the clock numbers with the font created further up by converting
        #the numbers into a string (render expects a string)
        #True makes the numbers look better on the screen
        number_markings_text = font.render(str(i), True, dark_pink)
        #Ensuring that each number is positioned correctly based on the center
        #by getting the rectangular boundry for each number
        text_rect = number_markings_text.get_rect(center = (x,y))

        #Placing the numbers on the screen with blit with the surface and positions
        #as parameters
        screen.blit(number_markings_text, text_rect)

    #Minute markings 
    for i in range(60):
        #Making a variable for line thickness so that it can be changed
        line_thickness = 2
        #Here the iterations are added with 6 (360/60)
        angle = math.radians(i * 6 - 90) 

        #Creating inner and outer x and y points in order to draw the line
        outer_x = center[0] + (clock_radius - 12) * math.cos(angle)
        outer_y = center[1] +(clock_radius - 12) * math.sin(angle)

        inner_x = center[0] + (clock_radius - 20) * math.cos(angle)
        inner_y = center[1] + (clock_radius - 20) * math.sin(angle)

        #For each 5th minute marking, we want the line to be thicker 
        if i % 5 == 0:
            inner_x = center[0] + (clock_radius - 25) * math.cos(angle) 
            inner_y = center[1] + (clock_radius - 25) * math.sin(angle)
            line_thickness = 4 
            
        pygame.draw.line(screen, dark_pink, (outer_x, outer_y), (inner_x, inner_y), line_thickness)

    #Getting current time in hours, minutes and seconds with the datetime library
    now = datetime.now()
    seconds = now.second
    minutes = now.minute
    hours = now.hour % 12 

    #Draw hour hand 
    hour_angle = math.radians((hours + minutes / 60) * 30 - 90)
    hour_x = center[0] + (clock_radius - 90) * math.cos(hour_angle)
    hour_y = center[1] + (clock_radius - 90) * math.sin(hour_angle)
    pygame.draw.line(screen, light_pink,(center[0],center[1]),(hour_x,hour_y), 4)

    #Draw minute hand
    minute_angle = math.radians(minutes * 6 - 90)
    minute_x = center[0] + (clock_radius - 60) * math.cos(minute_angle)
    minute_y = center[1] + (clock_radius - 60) * math.sin(minute_angle)
    pygame.draw.line(screen, light_pink,(center[0],center[1]),(minute_x,minute_y), 4)

    #Draw second hand 
    second_angle = math.radians(seconds * 6 - 90)
    second_x = center[0] + (clock_radius - 60) * math.cos(second_angle)
    second_y = center[1] + (clock_radius - 60) * math.sin(second_angle)
    pygame.draw.line(screen, dark_pink,(center[0],center[1]),(second_x,second_y), 2)
    
    #Drawing a small circle in the middle of the clock
    pygame.draw.circle(screen, light_pink, (center[0], center[1]),7)
        
    #60 itereations per second 
    pygame.time.Clock().tick(60)

#Quit pygame
pygame.quit()