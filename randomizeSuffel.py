from random import seed
from random import choice
from numpy.random import shuffle
def distribution(temp,player):
    for _ in range(10):
        selection = choice(temp)
        # print(selection)
        player.append(selection)
        temp.remove(selection)
    return player
		
