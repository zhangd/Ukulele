# HOBBIT SONG
inputNotes = [(3,0),(3,2),(3,4),(2,3),(3,4),(3,2),(3,0),(1,'-'),(2,0),(2,3),(1,0),(1,3),(1,2),(2,3),(2,0),(2,1),(2,0),(3,2)]








totalTime = 100
tabs = [['-']*totalTime,['-']*totalTime,['-']*totalTime,['-']*totalTime]

time = 0

for note in inputNotes:
	string,finger = note[0]-1,note[1]
	tabs[string][time] = finger
	time += 1

for string in tabs:
	stringBar = ""
	for bar in string:
		stringBar += str(bar)
	print stringBar