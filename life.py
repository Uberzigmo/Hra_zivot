from random import randint
import time

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

size = 50
thr_x = 50 # procentualni pravdepodobnost, ze bude bunka ziva
play_field = draw_map(size,thr_x)

#for line in play_field: # vypsani prazdneho pole
#    for part in line:
#        print(part,end=' ')
#    print()

def find_all(my_list,sign): # vraci pocet zivych nebo mrtvych v okoli bunky
    return len([i for i, x in enumerate(my_list) if x == sign])

def kill_or_ress(field,list_of_positions,sign): # meni zivy ya mrtvy a naopak
    for position in list_of_positions:
        field[position[0]][position[1]] = sign
    return field


while True:
    kill = [] # plnim pocet bunek, ktere maji umrit
    ress = [] # plnim pocet bunek, ktere maji obzivnout

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

            if play_field[line][col] == 'x':
                if (find_all(okoli,'x') < 2):
                    kill.append([line,col])
                    #play_field[line][col] = 'O'
                elif find_all(okoli,'x') > 3:
                    kill.append([line,col])
                    #play_field[line][col] = '.'
                else:
                    pass
            else:
                if find_all(okoli,'x') == 3:
                    ress.append([line,col])
                    #play_field[line][col] = 'x'
                else:
                    pass

    play_field = kill_or_ress(play_field,kill,'.')
    play_field = kill_or_ress(play_field,ress,'x')

    for line in play_field: # vypsani pole
        for part in line:
            print(part,end=' ')
        print()
    time.sleep(0.25)
