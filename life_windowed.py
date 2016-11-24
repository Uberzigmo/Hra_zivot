from random import randint
import time
import pygame
from pygame.locals import *
import sys

                                          


def draw_map(size,thr_x): # funkce na vytvoreni hraciho pole
    field = []
    for i in range(size):
        line = []
        for j in range(size):
            if randint(0,100)<thr_x:
                line.append('.')
            else:
                line.append('x')
        field.append(line)
    return field

size = 100
thr_x = 50 # procentualni pravdepodobnost, ze bude bunka ziva
play_field = draw_map(size,thr_x)




pygame.init()
pixel_size = 10

# Vyvtoreni okna s definovanym poctem policek
display_size = size*pixel_size
DISPLAY=pygame.display.set_mode((display_size,display_size),0,32)

WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)

# Vyplni pozadi barvou
DISPLAY.fill(GREEN)   

    
def find_all(my_list,sign):
    '''Najde pocet vyskytu nejakeho znaku v seznamu '''
    return len([i for i, x in enumerate(my_list) if x == sign])
    
def kill_or_ress(field,list_of_positions,sign):
    '''V poli vymeni vsechny znaky na pozicich uvedenych v list_of_positions za znak sign'''
    for position in list_of_positions:
        field[position[0]][position[1]] = sign
    return field
        

while True:
    kill = []
    ress = []

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    # Pro kazdy bod se najdou vsichni existujici sousedi
    for line in range(0,size):
        for col in range(0,size):
            okoli = []
            if (line == 0) and (col == 0):
                E = play_field[line][col+1]
                S = play_field[line+1][col]
                SE = play_field[line+1][col+1]
                okoli.extend([E,S,SE])
                
            elif (line == 0) and (col == size-1):
                W = play_field[line][col-1]
                SW = play_field[line+1][col-1]
                S = play_field[line+1][col]
                okoli.extend([W,SW,S])
            elif (line == size-1) and (col == size-1):
                N = play_field[line-1][col]
                W = play_field[line][col-1]
                NW = play_field[line-1][col-1]
                okoli.extend([N,W,NW])
            elif (line == size-1) and (col == 0):
                N = play_field[line-1][col]
                E = play_field[line][col+1]
                NE = play_field[line-1][col+1]
                okoli.extend([N,E,NE])
                
            elif (line == 0):
                S = play_field[line+1][col]
                W = play_field[line][col-1]
                E = play_field[line][col+1]
                SW = play_field[line+1][col-1]
                SE = play_field[line+1][col+1]
                okoli.extend([S,W,E,SW,SE])
            elif (line == size-1):
                N = play_field[line-1][col]
                W = play_field[line][col-1]
                E = play_field[line][col+1]
                NE = play_field[line-1][col+1]
                NW = play_field[line-1][col-1]
                okoli.extend([N,W,E,NE,NW])
            elif (col == 0):
                S = play_field[line+1][col]
                N = play_field[line-1][col]
                E = play_field[line][col+1]
                NE = play_field[line-1][col+1]
                SE = play_field[line+1][col+1]
                okoli.extend([S,N,E,NE,SE]) 
            elif (col == size-1):
                S = play_field[line+1][col]
                N = play_field[line-1][col]
                W = play_field[line][col-1]
                NW = play_field[line-1][col-1]
                SW = play_field[line+1][col-1]
                okoli.extend([S,N,W,NW,SW])      
            else:
                S = play_field[line+1][col]
                N = play_field[line-1][col]
                W = play_field[line][col-1]
                E = play_field[line][col+1]
                NE = play_field[line-1][col+1]
                NW = play_field[line-1][col-1]
                SW = play_field[line+1][col-1]
                SE = play_field[line+1][col+1]
                okoli.extend([S,N,W,E,NE,NW,SW,SE])
            
            
            # Pravidla hry - kdy bunka umira/oziva/preziva          
            if play_field[line][col] == 'x':
                if (find_all(okoli,'x') < 2): 
                    kill.append([line,col])
                elif find_all(okoli,'x')>3:
                    kill.append([line,col])
                else:
                    pass
            else:
                if find_all(okoli,'x')==3:
                    ress.append([line,col])
                else:
                    pass               
    # Zmeneni vsech bunek, ktere maji zmenit stav       
    play_field = kill_or_ress(play_field,kill,'.')
    play_field = kill_or_ress(play_field,ress,'x')                
 
    # vykresleni pole, prevedeni ASCII vystupu do zobrazovaciho okna
    for i in range(0,display_size,pixel_size): 
        for j in range(0,display_size,pixel_size):
            # Vykresli ctverec nejake barvy do okna DISPLAY na souradnice definovane souradnicemi i a j,
            i_field_position = i//pixel_size #prevedeni pozic z rozliseni grafickeho okna do rozliseni ascii pole
            j_field_position = j//pixel_size
            if play_field[i_field_position][j_field_position]=='.': 
                pygame.draw.rect(DISPLAY,WHITE,(i,j,i+pixel_size,j+pixel_size))
            else:
                pygame.draw.rect(DISPLAY,BLACK,(i,j,i+pixel_size,j+pixel_size))
    
    # prekresleni okna
    pygame.display.update()

    # zpozdeni vypoctu - v pripade vykreslovani do terminalu nutne, aby bylo mozno hru sledovat
    # pri vykreslovani do okna skoro zbytecne- vypocet zabere podstatne delsi dobu
    time.sleep(0.0005)
    
