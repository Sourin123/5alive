# choose a random element from a list
from random import seed
from random import choice
from numpy.random import shuffle
# seed random number generator
seed(1)
#creating the players
player1,player2,player3,player4,player5 = [],[],[],[],[]
# prepare a sequence
sequence = ["0","0","0","0","0","0","0","0",
			"1","1","1","1","1","1","1","1",
			"2","2","2","2","2","2","2","2",
			"3","3","3","3","3","3","3","3",
			"4","4","4","4","4","4","4","4",
			"5","5","5","5","6","6","7","bomb",
			"suffel","=10","=10","=21","=21","=21","=21",
			"=21","+1","+1","+2","+2","selfSkip","selfSkip","selfSkip","selfSkip",
			"Skip","Skip","Skip","Skip","Rev","Rev","Rev","Rev","Rev","Rev"]
temp = sequence
shuffle(temp)
print(sequence)
print(temp)
# make choices from the sequence
for _ in range(10):
	selection = choice(temp)
	print(selection)
	player1.append(selection)
	temp.remove(selection)
	selection2 = choice(temp)
	player2.append(selection2)
	temp.remove(selection2)
	selection3 = choice(temp)
	player3.append(selection3)
	temp.remove(selection3)
	selection4 = choice(temp)
	player4.append(selection4)
	temp.remove(selection4)
	selection5 = choice(temp)
	player5.append(selection5)
	temp.remove(selection5)
	
print(player1)
print(player2)
print(player3)
print(player4)
print(player5)

	
	
	