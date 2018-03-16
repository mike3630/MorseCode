import playsound
import sys

inputString = ''

for i in range (1, len(sys.argv)):
	inputString = inputString + sys.argv[i]

print(inputString)
inputLen = len(inputString)

for x in range(0, inputLen):
	inputChar = inputString[x].upper()
	print(inputChar)
	fileToPlay = 'MorseSounds/' + str(inputChar) + '.mp3'
	playsound.playsound(fileToPlay,True)