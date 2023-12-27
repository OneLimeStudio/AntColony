import random
import pygame
import math
import time

screenWidth = 1280
screenHeight = 720
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True


#VARIABLES
antSize = 20 #pixels



def DrawPath(path: list):
    
    for i in range(len(path)):
       
        pygame.draw.rect(screen,(255,255,255), pygame.Rect(path[i][0],path[i][1],antSize,antSize))
        pygame.draw.rect(screen,(255,255,255), pygame.Rect(path[i][0]+20,path[i][1],antSize,antSize))
        pygame.draw.rect(screen,(255,255,255), pygame.Rect(path[i][0]+30,path[i][1],antSize,antSize))
        print(path[i][0],path[i][1])

class Ant():

    def __init__(self,position:list) -> None:
        self.position = position
        self.path = []
        self.pathFound = False
    def lookFood(self):
        
    
       # for i in range(self.position[0] - antSize,self.position[0]+antSize):
        #    for j in range(self.position[1] - antSize,self.position[1]+antSize):
       
        self.position[0] = random.choice([self.position[0] - antSize,self.position[0],self.position[0] + antSize])
        self.position[1] = random.choice([self.position[1] - antSize,self.position[1],self.position[1] + antSize])
        #print(self.position)
        

        
    def Draw(self):
        pygame.draw.rect(screen,(255,0,255), pygame.Rect(self.position[0],self.position[1],antSize,antSize))

    def pheromone(self):
        if self.pathFound == False:
            self.path.append(self.position)
    def checkFood(self,food : list):
        for obj in food:
            x = self.position[0]
            y = self.position[1]
            # pygame.draw.rect(screen, (0,255,0), (x,y,antSize+50,antSize+50), 0)
            # for i in range(4):
            #     pygame.draw.rect(screen, (0,0,0), (x-i,y-i,antSize+50,antSize+50), 1)
            
            distance = math.sqrt((x - obj.position[0])**2 +(y - obj.position[1])**2 )
            #print(math.sqrt((2*antSize)**2),distance)
            if(distance <= math.sqrt((2*antSize)**2)+ 4):
                #print("Truee")
                pygame.draw.rect(screen,(255,255,255), pygame.Rect(self.position[0],self.position[1],antSize,antSize))    
                self.pathFound = True
                #print(self.path)
                DrawPath(self.path)



class Food():
    def __init__(self,position : list) -> None:
        self.position = position
        

    def Draw(self):
        pygame.draw.rect(screen,(0,0,255), pygame.Rect(self.position[0],self.position[1],antSize,antSize))

    
ok = 400
food = []
ants = []
hasRun = True

while running:
    screen.fill("black")
    ok += 10
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if hasRun == True:
        for i in range(4):
            radius = (screenHeight/2) * math.sqrt(random.random())
            theta = random.random() * 2 * 3.14159 
            x = (screenWidth/2) + radius * math.cos(theta)
            y = (screenHeight/2) + radius * math.sin(theta)
            #food.append(Food([random.randint(0,screenWidth),random.randint(0,screenHeight)]))
            food.append(Food([x,y]))
            ants.append(Ant([screenWidth/2,screenHeight/2]))


            food[i].Draw()
            hasRun = False
    else:
        for obj in food:
            obj.Draw()
    # for obj in ants:
    #     obj.lookFood()
    #     obj.Draw()
    #     obj.pheromone()
    #     obj.checkFood(food)
    #     if obj.pathFound == True:
    #         DrawPath(obj.path)
    obj =ants[0] 
    obj.lookFood()
    obj.Draw()
    obj.pheromone()
    obj.checkFood(food)   
    if obj.pathFound == True:
        print("OKKK")
        DrawPath(obj.path)
    
    pygame.draw.rect(screen,(0,255,255), pygame.Rect(screenWidth/2,screenHeight/2,20,20))
  
    pygame.display.flip()

    clock.tick(30)


pygame.quit()

