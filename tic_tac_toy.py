import pygame
import random

def drow_grid(screen):
    pygame.draw.line(screen,"black",(100,0),(100,300),2)
    pygame.draw.line(screen,"black",(200,0),(200,300),2)
    pygame.draw.line(screen,"black",(0,100),(300,100),2)
    pygame.draw.line(screen,"black",(0,200),(300,200),2)
    pygame.draw.line(screen,"black",(0,300),(300,300),2)

def draw_tic_tac_toe(scr,items):
    for i in range(3):
        for j in range(3):
            if items[i][j] == "o":
                pygame.draw.circle(scr, (255, 0, 0), (j * 100 + 50, i * 100 + 50), 45)
            elif items[i][j] == "x":
                pygame.draw.line(scr, (0, 0, 255), (j * 100 + 5, i * 100 + 5),(j * 100 + 95, i * 100 + 95), 3)
                pygame.draw.line(scr, (0, 0, 255), (j * 100 + 95, i * 100 + 5),(j * 100 + 5, i * 100 + 95), 3)

def computer(save):
    print(save)
    while True:
        i = random.randint(0,2)
        j = random.randint(0,2)
        print(i,j)
        if save[i][j] == "":
            save[i][j] = "o"
            break
    return save


def check_win(save):
    for i in range(3):
        if save[i].count("x") == 3:
            return "user"
        elif save[i].count("o") == 3:
            return "computer"
        
        elif save[0][0]==save[1][0]==save[2][0]=="x":
            return "user"
        elif save[0][0]==save[1][0]==save[2][0]=="o":
            return "computer"
        elif save[0][1]==save[1][1]==save[2][1]=="x":
            return "user"
        elif save[0][1]==save[1][1]==save[2][1]=="o":
            return "computer"
        elif save[0][2]==save[1][2]==save[2][2]=="x":
            return "user"
        elif save[0][2]==save[1][2]==save[2][2]=="o":
            return "computer"
        

        elif save[0][0]==save[1][1]==save[2][2]=="x":
            return "user"
        elif save[0][0]==save[1][1]==save[2][2]=="o":
            return "computer"


        elif save[0][0]==save[0][1]==save[0][2]=="x":
            return "user"
        elif save[0][0]==save[0][1]==save[0][2]=="o":
            return "computer"
        elif save[1][0]==save[1][1]==save[1][2]=="x":
            return "user"
        elif save[1][0]==save[1][1]==save[1][2]=="o":
            return "computer"
        elif save[2][0]==save[2][1]==save[2][2]=="x":
            return "user"
        elif save[2][0]==save[2][1]==save[2][2]=="o":
            return "computer"
        


        elif save[0][0]==save[1][0]==save[2][0]=="x":
            return "user"
        elif save[0][0]==save[1][0]==save[2][0]=="o":
            return "computer"
   







def main():
    save = [["","",""],
            ["","",""],
            ["","",""]]
    
    figures = ["x","o"]
    move = 0
    
    pygame.init()
    screen = pygame.display.set_mode((300,400))
    screen.fill("white")
    drow_grid(screen)
    fond = pygame.font.SysFont("timesnewroman",30)
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            event.type
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if save[pos[1] // 100][pos[0] // 100] == "":
                    save[pos[1] // 100][pos[0] // 100] = "x"
                    save = computer(save)
                    if check_win(save)== "user":
                        scr = (fond.render("Победил человек",True,"black"))     
                        screen.blit(scr,(30,350))  
                        break
                    elif check_win(save)=="computer":
                        scr1 = (fond.render("Победил Компьютер",True,"black"))  
                        screen.blit(scr1,(30,350))
                        break



                draw_tic_tac_toe(screen,save)
                pygame.display.update()
    


if __name__ =="__main__":
    main()


 