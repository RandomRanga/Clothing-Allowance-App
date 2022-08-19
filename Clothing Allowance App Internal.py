from tkinter import *
from tkinter import ttk

class Child:
	'''Collects all info about each child, 
	stores it and then displays it.'''

	# Collects and stores all childs info.

	def __init__(self, name, allowance, bonus_cost):
		self.name = name
		self.allowance = allowance
		self.bonus_cost = bonus_cost

	
	def get_details(self):
		print("Name: {}" .format(self.name))
		print("Allowance: ${}" .format(self.allowance))
		print("Bonus cost: ${}" .format(self.bonus_cost))
		print("-----------------")

# Puts children info in, and prints it.
child1 = Child("Nikau", 300, 50)
child1.get_details()
child2 = Child("Hana", 300, 50)
child2.get_details()
child3 = Child("Tia", 300, 50)
child3.get_details()
