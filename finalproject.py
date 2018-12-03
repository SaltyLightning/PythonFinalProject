from abc import ABCMeta
from functools import reduce

class Cart:
		def __init__(self, cust):
			self.customer = cust
			self.items = []
		def add_items(self, its):
			self.items.append(its)
		def total(self):
			return reduce(lambda a,b: a+b, map(lambda x: (x.quantity * x.cost), self.items))
			# t = 0
			# for i in self.items:
			# 	print(i.quantity, i.cost)
			# 	t = t + (i.quantity * i.cost)
			# return t

class Item:
	"""docstring for Item"""
	def __init__(self, name, cost, quantity):
		self.name = name
		self.cost = int(cost)
		self.quantity = int(quantity)
	
	def __str__(self):
		return "{}, {}, {}".format(self.name, self.cost, self.quantity)

class Database:
	def __init__(self, file_name):
		self.items = {}
		# gen = 
		for record in self.read_db_file(file_name):
			self.items[record[0]] = record

	# generator function - takes a file name, parses out the line, and prints the info found
	def read_db_file(self,csv):
		with open(csv) as fil:
			fil.readline()	# skip the header line
			for line in fil:	# open the file and process line by line
				yield [x.strip() for x in line.split(',')]
				
def print_menu():
	print("Please select an option: ")
	print("a) Add an item to the cart\tb) Remove an item from the cart")
	print("c) Get cart total\tq) Quit")

name = input("What is your name? ")
cart1 = Cart(name)
db = Database("db.csv")
for key, i in db.items.items():
	ite = Item(i[0],i[1],i[2])

print_menu()
option = input()
while option.lower() != "q" :
	print()
	if option.lower() == "a":
		print("a")
		print("_________________________")
	elif option.lower() == "b":
		print("a")
		print("_________________________")
	elif option.lower() == "c":
		print("a")
		print("_________________________")
	elif option.lower() == "q":
		pass
	else:
		print("Please enter one of the above options")

	print()
	print_menu()
	option = input()