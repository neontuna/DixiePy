# we need to import the random function from python, we can abbreviate to rand
import random as rand
import os

# definining our makePass() function
def makePass():

	# Setup a couple of variables, a blank list for possiblePass and our lettersList
	possiblePass = []
	lettersList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'm', 'o', 'p', 'q',
		'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	vowelsList = ['a', 'e', 'o', 'u']
	constsLists = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'm', 'p', 'q', 'r', 's', 't', 
		'v', 'w', 'x', 'y', 'z']
		
	for i in range(0,6):
		firstChar = lettersList[rand.randrange(0,22,1)]
		possiblePass.append(firstChar)
	
	
	if possiblePass[0] == possiblePass[1]:
		return None
	elif possiblePass[1] == possiblePass[2]:
		return None
	elif possiblePass[2] == possiblePass[3]:
		return None
	elif possiblePass[3] == possiblePass[4]:
		return None
	elif possiblePass[4] == possiblePass[5]:
		return None
	elif any((True for x in vowelsList if x in possiblePass[0])):
		return None
	elif any((True for x in constsLists if x in possiblePass[1])):
		return None
	elif any((True for x in vowelsList if x in possiblePass[2])):
		return None
	elif any((True for x in vowelsList if x in possiblePass[3])):
		return None
	elif any((True for x in constsLists if x in possiblePass[4])):
		return None
	else:
		possiblePass.append(str(rand.randrange(10,99,1)))
		finalPass = ''.join(possiblePass)
		return finalPass

def makeGoodPass():
	bigList = []
	i = 0
	while i <= 20:
		p = makePass()
		
		#print p
		if p is not None:
			bigList.append(p)
			i += 1
	return bigList
	
##print makeGoodPass()
##os.system('cls')
##print "-" * 10
##print "\n\n"
#i = 0
#while i <= 20:
#	p = makePass()
	#print p
#	if p is not None:
#		print p
#		i += 1
		
##print "\n\n"
##print "-" * 10
