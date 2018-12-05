from abc import ABCMeta
from functools import reduce
from copy import deepcopy
import time
# import mysql.connector

# decorator for timing - from Stack Overflow
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed

#cart class - acts as a shopping cart
class Cart:
		#initializer
		def __init__(self, cust):
			self.customer = cust
			self.items = []
		# adds item(s) to the cart
		def add_items(self, its):
			self.items.append(its)
		# returns the cart's total
		def total(self):
			return reduce(lambda a,b: a+b, map(lambda x: (x.quantity * x.cost), self.items)) if len(self.items) > 0 else 0
		# removes an item from the cart
		def remove_item(self, it):
			self.items.remove(it)
		# to string function
		def __str__(self):
			s = self.customer + "'s cart: \n"
			for i in self.items:
				s = s + str(i) + "\n"
			return s + "Total: ${:.2f}".format(self.total() / 100)
			# t = 0
			# for i in self.items:
			# 	print(i.quantity, i.cost)
			# 	t = t + (i.quantity * i.cost)
			# return t
#class for items
class Item:
	
	def __init__(self, name, cost, quantity):
		self.name = name
		self.cost = int(cost)
		self.quantity = int(quantity)
	
	def __str__(self):
		return "Item Name: {}, Cost: ${:.2f}, Quantity: {}".format(self.name, self.cost/ 100, self.quantity)
#class for "database"
class Database:
	# initializer calls the generator used to read files
	@timeit
	def __init__(self, file_name):
		self.items = {}
		self.db_connection = ""
		# gen = 
		for record in self.read_db_file(file_name):
			self.items[record[0]] = self.item_from_list(record)
		# self.db_connect()

	# deprecated
	def db_connect(self):
		self.db_connection =  mysql.connector.connect(
		  host="localhost",
		  user="root",
		  passwd="",
		  database="python")
		print(self.db_connection)
	
	# creates a item from a list
	def item_from_list(self, li):
		return Item(li[0], li[2], li[1])

	# generator function - takes a file name, parses out the line, and prints the info found
	def read_db_file(self,csv):
		with open(csv) as fil:
			fil.readline()	# skip the header line
			for line in fil:	# open the file and process line by line
				yield [x.strip().lower() for x in line.split(',')]

	#writes "database" back to file
	@timeit
	def write_db_file(self, csv):
		# mycursor = self.db_connection.cursor()
		# sql = "INSERT INTO shopping (item_name, quantity, price) VALUES (%s, %s, %s)"
		# val = []
		with open(csv, "w+") as fil:
			fil.write("item_name,quantity,price\n")
			for k, i in self.items.items():
				# print(i)
				fil.write("{},{},{}\n".format(i.name, i.quantity, i.cost))
				# val.append((i.name, i.quantity, i.cost))
		# print(val)
		# mycursor.executemany(sql, val)
		# self.db_connection.commit()

				
#prints the menu
def print_menu():
	print("Please select an option: ")
	print("a) Add an item to the cart\tb) Modify cart contents")
	print("c) Get cart total\td) Print database contents");
	print("e) Checkout\tq) Quit")

#allows the user to add to the cart
def AddItemToCart(db, cart):
	iName = (input("What item do you want to add to your cart? ")).lower()
	db_items = db.items
	found = db_items.get(iName, "")
	if found == "":
		print("That item is not contained in the database")
	else:
		print(found)
		quant = int(input("How many would you like to buy? "))
		while quant > found.quantity:
			quant = int(input("Sorry, the database only contains {} of {}, not {}.\n".format(found.quantity, found.name, quant)))
		found2 = deepcopy(found)
		found2.quantity = quant
		cart.add_items(found2)
		found.quantity = found.quantity - quant
		db_items[iName] = found

#allows the user to modify cart contents
def ModCart(db, cart):
	print(str(cart) + "\n")
	iName = input("What item would you like to modify? ")
	item = [i for i in cart.items if i.name == iName][0]
	if item == []:
		print("Sorry, that item is not in the cart.")
	else:
		quant = int(input("How many would you like to remove from your cart? "))
		while quant > item.quantity:
			quant = int(input("Sorry, you do not have that many in the cart"))
		if quant == item.quantity:
			cart.remove(item)
		else:
			item.quantity = item.quantity + quant
		db.items.get(iName).quantity = db.items.get(iName).quantity + quant
# --MAIN-- #
name = input("What is your name? ")
cart1 = Cart(name)
db = Database("db.csv")
for key, i in db.items.items():
	ite = i

print_menu()
option = input()
while option.lower() != "q" :
	print()
	if option.lower() == "a":
		AddItemToCart(db, cart1)
		print("_________________________")
	elif option.lower() == "b":
		ModCart(db, cart1)
		print("_________________________")
	elif option.lower() == "c":
		print(cart1)
		print("_________________________")
	elif option.lower() == "d":
		for k,i in db.items.items():
			print(i)
		print("_________________________")
	elif option.lower() == "e":
		print(cart1)
		print("\nThank you, {}! Have a nice day!".format(cart1.customer))
		db.write_db_file("db.csv")
		quit()
	elif option.lower() == "q":
		pass
	else:
		print("Please enter one of the above options")

	print()
	print_menu()
	option = input()