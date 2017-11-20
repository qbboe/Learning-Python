import random       # modules
import sys
import os

class Player :
	__name = None	# or ""
	__height = 0	# -- means private
	__weight = 0
	
	def __init__(self, name,height, weight) :    	# constructor 	
		self.__name = name
		self.__height = height
		self.__weight = weight
		
# set/get 	
	def set_name(self, name) :	# object, attribute
		self.__name = name
	def set_height(self, height) :	
		self.__height = height
	def set_weight(self, weight) :	
		self.__weight = weight
		
	def get_name(self) :
		return self.__name
	def get_height(self) :
		return self.__height
	def get_weight(self) :
		return self.__weight
	def get_type(self) :
			print("Player")
			
	def toString(self) :
		return "{} is {} cm and {} kg".format(self.__name,
											self.__height,	
											self.__height)

Burfict = Player('Vontaze',185,112)											
print(Burfict.toString())	

class Team(Player) :
	__number = ""
	
	def __init__(self, name, height, weight, number) :
		self.__number = number
		super(Team, self).__init__(name,height,weight)
		
	def set_number(self, number) :
		self.__number = number
	def get_number(self) :
		return self.__number
	def get_type(self) :
		print("Team")
	def toString(self) :		# overloading
		return "{} is {} cm and {} kg, number {}".format(self.__name,
													self.__height,	
													self.__height,
													self.__number)

	def multiple_tackles(self, how_many = None) :
		if how_many is None :
			print(self.get_number())
		else :
			print(self.get_number() * how_many)
			
VB = Team('Vontaze',185,112,'55')
print(VB.toString())

# POLYMORPHISMS
class TeamTesting
	def get_type(self, player) :
		player.get_type()

test_team = TeamTesting(Burfict)
test_team.get_type(VB)
VB.multiple_tackles(4)
VB.multiple_tackles()
#print()
# INHERITANCE

	