def draw_map(size = 20): # funkce na vytvoreni hraciho pole
    field = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append('.')
        field.append(line)
    return field
play_field = draw_map()

for line in play_field: # vypsani pole
    for part in line:
        print(part,end=' ')
    print()
