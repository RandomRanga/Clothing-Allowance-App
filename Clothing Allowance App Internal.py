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