bridge = [['|']*4,['|']*4,['|']*4,['|']*4,['|']*4,['|']*4]

nothing = []
C = [(1,3)]
G = [(3,2),(2,3),(1,2)]
Am = [(4,2)]
F = [(4,2),(2,1)]
Em = [(1,2),(2,3),(3,4)]
D = [(4,2),(3,2),(2,2)]
Bflat = [(4,3),(3,2),(2,1),(1,1)]

chord = Bflat

for note in chord:
	string,finger = 4-note[0],note[1]-1
	bridge[finger][string] = "X"


for fret in bridge:
	stringBar = ""
	for string in fret:
		stringBar += str(string)
	print stringBar

