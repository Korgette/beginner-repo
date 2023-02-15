#a game placing three aliens in random positions, asking a user to choose X/Y to shoot
#and then reporting a hit or a miss
import random
totalPoints = 0
totalShots = 0
cannon ={'x':0,'y':0}
gamePlay = 'Y'
#dicts defining aliens,points
alien_green = {'number':1,'colour':'green','points':5,'x':2,'y':2}
alien_blue = {'number':2,'colour':'blue','points':30,'x':5,'y':2}
alien_red = {'number':3,'colour':'red','points':10,'x':7,'y':7}

print('This is a game for guessing the co-ordinates of an alien.')
print('The limit of X and Y co-ordinates is 0-16')

while gamePlay == 'Y':
    #main loop for game
    #select random locations for aliens x,y coords
    alien_green['x'] = random.randint(2,14)
    alien_green['y'] = random.randint(2,14)
    alien_blue['x'] = random.randint(2,14)
    alien_blue['y'] = random.randint(2,14)
    alien_red['x'] = random.randint(2,14)
    alien_red['y'] = random.randint(2,14)
    print('where should we fire the cannon? x-cord')
    cannon['x'] = int(input())
    print('Where should we fire the cannon? y-cord')
    cannon['y'] =int(input())
    print('You fired at ' +str(cannon))
    totalShots=totalShots +1
    #check for hits on green
    if (int(cannon['x']) <= int(alien_green['x']) + 2
    and int(cannon['x']) >= int(alien_green['x']) -2
    and int(cannon['y']) <= int(alien_green['y']) + 2
    and int(cannon['y']) >= int(alien_green['y']) - 2):
        totalPoints = totalPoints + alien_green['points']
        print('You hit alien Green and scored ' + str(alien_green['points']))
    #check for hits on blue
    elif (int(cannon['x']) <= int(alien_blue['x']) + 2
    and int(cannon['x']) >= int(alien_blue['x']) -2
    and int(cannon['y']) <= int(alien_blue['y']) + 2
    and int(cannon['y']) >= int(alien_blue['y']) - 2):
        totalPoints = totalPoints + alien_blue['points']
        print('You hit alien Blue and scored ' +str(alien_blue['points']))
    #check for hits on red  
    elif (int(cannon['x']) <= int(alien_red['x']) + 2
    and int(cannon['x']) >= int(alien_red['x']) -2
    and int(cannon['y']) <= int(alien_red['y']) + 2
    and int(cannon['y']) >= int(alien_red['y']) - 2):
        totalPoints = totalPoints + alien_red['points']
        print('You hit alien red and scored ' +str(alien_red['points']))

    else:
        print('You missed!')

    #once max shots have expired, prompt user for continue/quit   
    if totalShots >5:
        print('Would you like to play again? Y/N')
        gamePlay = input().upper()
        totalShots = 0
    
    
    
print('You scored a total of ' + str(totalPoints) + ' points.')

#add alien size to dict(make higher point aliens smaller)
#check outputs are correct and that target parameters are working correctly
#print the outputs of alien colours
#using alien key 'colour' with loop could condense code massively - try.
#make room for input errors
#implement high score system?
#allow user to set number of turns(word it like old school 'insert coin')

# ADVANCED - eventually add a scaling Z co ordinate for distance
#make it a coefficient for cannon X and Y(increased distance means less area)
