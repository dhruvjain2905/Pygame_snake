import pygame
import numpy as np

pygame.init()

pyt = pygame.image.load("Downloads/python.png")
background = pygame.image.load("Downloads/forest.png")
screen = pygame.display.set_mode((800,800))

pygame.display.set_caption("Snake with Python")


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
 
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
 
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))

def mod_show_move(letter, pos, size):
    the_font = pygame.font.Font("freesansbold.ttf", size)
    show = the_font.render(letter, True, (255,255,255))
    screen.blit(show,pos)



def our_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen,(0,255,0),[x[0],x[1],40,40])
        


def end_screen(your_score):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                main()
        screen.fill((0,0,0))
        screen.blit(background, (0,0))
        screen.blit(pyt,(500,500))
        mod_show_move("Game Over", (220,260), 64)
        mod_show_move("Score: "+str(your_score), (230,420), 40)
        mod_show_move("Click to Restart", (230,350), 40)
        pygame.display.update()



def main():

    possiblex = np.arange(0,760,40)
    possibley = np.arange(0,760,40)

    snake_List = []
    Length_of_snake  = 1

   
    x1 = 0
    y1 = 360

    x1_change = 0
    y1_change = 0

    foodx = np.random.choice(possiblex, size = 1)
    foody = np.random.choice(possibley, size = 1)

    clock = pygame.time.Clock()

    while True:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -40
                    y1_change = 0

                elif event.key == pygame.K_RIGHT:
                    x1_change = 40
                    y1_change = 0

                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -40

                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 40

        if (x1 > 760 or x1 < 0) or (y1 > 760 or y1 < 0):
            end_screen(your_score)


        x1 += x1_change
        y1 += y1_change
        screen.fill((0,0,0))
        drawGrid(800,20,screen)

        #pygame.draw.circle(screen, (0,0,0), (x1+20,y1+20), 5)

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                end_screen(your_score)

        our_snake(snake_List)
        your_score = Length_of_snake - 1
        mod_show_move("Score: "+str(your_score),(50,40),40)

        pygame.draw.circle(screen, (0,0,0), (x1+10,y1+10), 5)
        pygame.draw.circle(screen, (0,0,0), (x1+30,y1+10), 5)
        pygame.draw.line(screen, (0,0,0), (x1+10,y1+30),(x1+30,y1+30), 5)


      
        #pygame.draw.rect(screen,(0,255,0),[x1,y1,40,40])
        pygame.draw.rect(screen,(255,0,0),[foodx,foody,40,40])

        pygame.display.update()



        if x1 == foodx and y1 == foody:
            Length_of_snake += 1
            foodx = np.random.choice(possiblex, size = 1)
            foody = np.random.choice(possibley, size = 1)

        clock.tick(12)
        pygame.display.update()




while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            main()
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    mod_show_move("Snake With Python",(100,200),50)
    mod_show_move("Click to start",(100,300),40)
    #mod_show_move("You may go first",(100,500),25)
    screen.blit(pyt,(500,500))
    pygame.display.update()


