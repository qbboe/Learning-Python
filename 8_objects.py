import random       # modules
import sys
import os

class Player :
	__name = None	# or "", lack of values
	__height = 0	# __ means private variable
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
		return str(self.__height)
	def get_weight(self) :
		return str(self.__weight)
		
	def get_type(self) :
			print("Player")
			
	def toString(self) :
		return "{} is {} cm and {} kg".format(self.__name,
											self.__height,	
											self.__height)

Burfict = Player('Vontaze',185,112)	# create Player object 								

print(Burfict.toString())	

class LB(Player) :		# INHERITANCE
	__number = ""
	
	def __init__(self, name, height, weight, number) :
		self.__number = number
		
		super(LB, self).__init__(name,height,weight)
		
	def set_number(self, number) :
		self.__number = number
	def get_number(self) :
		return self.__number
	def get_type(self) :
		print("LB")
		
	def toString(self) :		# overloading
		return "{} is {} cm and {} kg, number {}".format(self.get_name(),
													self.get_height(),	
													self.get_weight(),
													self.get_number())

	def multiple_tackles(self, how_many = None) :
		if how_many is None :
			print(self.get_number())
		else :
			print(self.get_number() * how_many)
			
VB = LB('Vontaze',185,112,'55')

print(VB.toString())

# POLYMORPHISM
class TeamTesting :
	def get_type(self, player) :
		player.get_type()
		
test_team = TeamTesting()

test_team.get_type(Burfict)
test_team.get_type(VB)

VB.multiple_tackles(4)


	