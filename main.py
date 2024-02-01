from random import seed
from random import choice
from numpy.random import shuffle
import randomizeSuffel
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
			"resuffel","=10","=10","=21","=21","=21","=21",
			"=21","+1","+1","+2","+2","selfSkip","selfSkip","selfSkip","selfSkip",
			"Skip","Skip","Skip","Skip","Rev","Rev","Rev","Rev","Rev","Rev"
			,"=0","=0","=0"]
temp = sequence
shuffle(temp)

player1 = randomizeSuffel.distribution(temp,player1)
player2 = randomizeSuffel.distribution(temp,player2)
player3 = randomizeSuffel.distribution(temp,player3)
player4 = randomizeSuffel.distribution(temp,player4)
player5 = randomizeSuffel.distribution(temp,player5)

print(player1)
print(player2)
print(player3)
print(player4)
print(player5)
print(temp)