import random
#initialise grid,count, flags for wins
grid = [['1','2','3'],
        ['4','5','6'],
        ['7','8','9']]

count = 0
game = True
pc_win = False
player_win = False

l = len(grid)
h = len(grid[0])

print(*grid,sep='\n')

def player_choice():
    #function for player choice, present current grid
    #if player selects a taken grid number, restart recall function
    global count
    print('Current grid: ')
    print(*grid,sep='\n')
    print('Please select a number:')
    p_choice = str(input())
    if p_choice in grid[0] or p_choice in grid[1] or p_choice in grid[2]:
        for i in grid:
            for j in range(h):
                if i[j] == p_choice:
                    i[j] = 'O'
    else:
        print('error! that has already been chosen')
        player_choice()
    count += 1
    

def check_diag():
    #check diagonals for win conditions, update if present
    global pc_win
    global player_win
    if grid[0][0] == 'X' and grid [1][1] == 'X' and grid [2][2] == 'X':
        pc_win = True
    elif grid [2][0] == 'X' and grid [1][1] == 'X' and grid [0][2] == 'X':
        pc_win = True
    else:
        if grid[0][0] == 'O' and grid [1][1] == 'O' and grid [2][2] == 'O':
            player_win = True
        elif grid [2][0] == 'O' and grid [1][1] == 'O' and grid [0][2] == 'O':
            player_win = True

            
    
def check_column():
    #check columns for win conditions, update if present
    global pc_win
    global player_win
    if grid[0][0]== 'X' and grid[1][0] == 'X' and grid[2][0] == 'X':
        pc_win = True
    elif grid[0][1] == 'X' and grid[1][1] == 'X' and grid[2][1] == 'X':
        pc_win = True
    elif grid[0][2] == 'X' and grid[1][2] =='X' and grid[2][2] == 'X':
        pc_win = True
    if grid[0][0]== 'O' and grid[1][0] == 'O' and grid[2][0] == 'O':
        player_win = True
    elif grid[0][1] == 'O' and grid[1][1] == 'O' and grid[2][1] == 'O':
        player_win = True
    elif grid[0][2] == 'O' and grid[1][2] =='O' and grid[2][2] == 'O':
        player_win = True

def check_win():
    #check for victory flags, if True, end game
    print('checking...')
    global pc_win
    global player_win
    check_column()
    check_diag()
    if ['X','X','X'] in grid:
        pc_win = True
    elif ['O','O','O'] in grid:
        player_win = True
    else:
        print('no win yet')

def grid_choice(x=random.randint(0,l-1),y=random.randint(0,h-1)):
    #function for computer choice
    global count
    if grid[x][y] == 'X' or grid [x][y] == 'O':
        x = random.randint(0,l-1)
        y = random.randint(0,h-1)
        grid_choice(x,y)
    else:
        grid[x][y] = 'X'
        count += 1

#main loop for game, using a count to ensure the game does not loop endlessly
while pc_win == False and player_win == False and count < 9:
    grid_choice()
    player_choice()
    check_win()
    print(*grid,sep='\n')
    print('count: ' +str(count))
if player_win == True:
    print('You won!')
else:
    print('Better luck next time.')


