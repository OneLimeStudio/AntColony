import random
import pygame
import math
import time

screenWidth = 1920
screenHeight = 1080
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True


#VARIABLES
antSize = 20 #pixels



def DrawPath(path: list):
    
    # for i in range(len(path)):
       
    #     pygame.draw.rect(screen,(255,255,255), pygame.Rect(path[i][0],path[i][1],antSize,antSize))
    #     time.sleep(0.1)
    #     print(path[i][0],path[i][1])
    pass
class Ant():

    def __init__(self,position:list) -> None:
        self.position = position
        self.path = []
        self.pathFound = False
        self.count = -1
        
    def lookFood(self):
        
    
     
       
        self.position[0] = random.choice([self.position[0] - antSize,self.position[0],self.position[0] + antSize])
        self.position[1] = random.choice([self.position[1] - antSize,self.position[1],self.position[1] + antSize])
        #print(self.position)
        
    def goBack(self):
        if(self.pathFound == True):
            pygame.draw.rect(screen,(255,255,255), pygame.Rect(self.path[self.count][0],self.path[self.count][1],antSize,antSize))
            print(self.path[self.count][0])
            if self.count == -1*len(self.path):
                pass
            else:
                self.count -=1
            
            
                

        
    def Draw(self):
        if self.pathFound == False:
            pygame.draw.rect(screen,(255,0,255), pygame.Rect(self.position[0],self.position[1],antSize,antSize))

    def pheromone(self):
        if self.pathFound == False:
            #print(self.path)
            self.path += [[self.position[0],self.position[1]]]

            
    def checkFood(self,food : list):
    
        if(self.pathFound == False):
            for obj in food:
                x = self.position[0]
                y = self.position[1]
      
                distance = math.sqrt((x - obj.position[0])**2 +(y - obj.position[1])**2 )
     
                if(distance <= math.sqrt((2*antSize)**2)+ 4 and self.pathFound == False):
    
                    pygame.draw.rect(screen,(255,255,255), pygame.Rect(self.position[0],self.position[1],antSize,antSize))    
                    self.pathFound = True
     
                
       

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
        for i in range(5):
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
    for obj in ants:
        obj.lookFood()
        obj.Draw()
        obj.pheromone()
        obj.checkFood(food)
        obj.goBack()
        if obj.pathFound == True:
            DrawPath(obj.path)
    # obj =ants[0] 
    # obj.lookFood()
    # obj.Draw()
    # obj.pheromone()
    
    # obj.checkFood(food)   
    # obj.goBack()
    # if obj.pathFound == True:
        
    #     DrawPath(obj.path)
    
    pygame.draw.rect(screen,(0,255,255), pygame.Rect(screenWidth/2,screenHeight/2,20,20))
  
    pygame.display.flip()

    clock.tick(30)


pygame.quit()

