import random       # modules
import sys
import os

name = "TIJ"
print("\n\tHello World!",name, "here!\n")
# DATATYPES: numbers strings lists tuples dictionaries
print(" # DATATYPES: numbers strings lists tuples dictionaries")
# OPS: + - * / % **exp //floor division
quote = "\"Always remember you're unique"
print("%s %s" % ('I like the quote', quote))
print("I don't like ", end="")   # avoid \n
print("newlines \n\n")

alphabeta = "abcdefghi"	# String
print(alphabeta[0:4])		# abcd
print(alphabeta[-5:])		# efghi
print(alphabeta[:-5])		# abcd
print(alphabeta[:4]+"nice!")
print("%c is %s initial, number %d, %.2f tackles/game"  
% ('V','Vontaze',55,5.55))
print(alphabeta.capitalize)
print(alphabeta.find("e"))
print(alphabeta.isalpha(), , "   .isaplha")
#print(alphabeta.replece ("abcdefghi","jklmnop"))
print(alphabeta.strip(), "   .strip")
quote = alphabeta.split()

# LISTS
print (" # LISTS:")
offence = ['QB', 'RB', 'WR']
print("offence: ",offence)
print('First item:', offence[0])
print(offence[1:3])    # element from 1 to 2
defence = ['DL', 'LB', 'DB']
team = [offence,defence]   # list of lists
print(team, ": list of lists")
print((team[1][1]),"\n")   # second list, second element

offence.append('TE')       # add at last
offence.insert(1, 'FB')    # add at position
offence.remove('TE')
offence.sort()
offence.reverse()      # reverse sort
del offence[3]         # delete fourth element
print(team, "  # list of lists")

team2 = offence +defence # merge 2 lists
print("team2",team2, "      # merge 2 lists")
print(len(team2), "           elements (len)")
print(max(team2), "    last element (max)\n\n")

# TUPLES cannot be changed
print (" # TUPLES:")
pi_tuple = (3,1,4,1,5,9)  # len(pi_tuple)... min... max
new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)
print (pi_tuple,"\n\n")

# DICTIONARIES OR MAPS not joinable
print (" # DICTIONARIES:")
super_villains = {'QB' : 'Dalton',
				  'RB' : 'Mixon',
				  'WR' : 'Green',
				  'TE' : 'Eifert',
				  'LB' : 'Burfict',
				  'DE' : 'Dunlap'}
print(super_villains['LB'])
del super_villains['TE']
super_villains['DE'] = 'Lawson'
print(len(super_villains))
print(super_villains.get('DE'),' get')
print(super_villains.keys(),' keys')
print(super_villains.values(),' values')
print('\n' * 2)



