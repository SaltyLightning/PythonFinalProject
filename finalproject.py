from abc import ABCMeta
from functools import reduce
from copy import deepcopy
import time
<<<<<<< HEAD
import mysql.connector
=======
>>>>>>> e7f822025490c79e9e86735e7349856d1a33bce2

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
<<<<<<< HEAD
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
=======
        print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
>>>>>>> e7f822025490c79e9e86735e7349856d1a33bce2
        return result
    return timed

class Cart:
		def __init__(self, cust):
			self.customer = cust
			self.items = []
		def add_items(self, its):
			self.items.append(its)
		def total(self):
			return reduce(lambda a,b: a+b, map(lambda x: (x.quantity * x.cost), self.items)) if len(self.items) > 0 else 0
		def remove_item(self, it):
			self.items.remove(it)
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

class Item:
	"""docstring for Item"""
	def __init__(self, name, cost, quantity):
		self.name = name
		self.cost = int(cost)
		self.quantity = int(quantity)
	
	def __str__(self):
		return "Item Name: {}, Cost: ${:.2f}, Quantity: {}".format(self.name, self.cost/ 100, self.quantity)

class Database:
	@timeit
	def __init__(self, file_name):
		self.items = {}
		self.db_connection = ""
		# gen = 
		for record in self.read_db_file(file_name):
			self.items[record[0]] = self.item_from_list(record)
<<<<<<< HEAD
		# self.db_connect()

	def db_connect(self):
		self.db_connection =  mysql.connector.connect(
		  host="localhost",
		  user="root",
		  passwd="",
		  database="python")
		print(self.db_connection)
	
=======
>>>>>>> e7f822025490c79e9e86735e7349856d1a33bce2

	def item_from_list(self, li):
		return Item(li[0], li[2], li[1])

	# generator function - takes a file name, parses out the line, and prints the info found
	def read_db_file(self,csv):
		with open(csv) as fil:
			fil.readline()	# skip the header line
			for line in fil:	# open the file and process line by line
				yield [x.strip().lower() for x in line.split(',')]

	@timeit
	def write_db_file(self, csv):
<<<<<<< HEAD
		# mycursor = self.db_connection.cursor()
		# sql = "INSERT INTO shopping (item_name, quantity, price) VALUES (%s, %s, %s)"
		# val = []
=======
>>>>>>> e7f822025490c79e9e86735e7349856d1a33bce2
		with open(csv, "w+") as fil:
			fil.write("item_name,quantity,price\n")
			for k, i in self.items.items():
				# print(i)
				fil.write("{},{},{}\n".format(i.name, i.quantity, i.cost))
<<<<<<< HEAD
				# val.append((i.name, i.quantity, i.cost))
		# print(val)
		# mycursor.executemany(sql, val)
		# self.db_connection.commit()

				
=======
>>>>>>> e7f822025490c79e9e86735e7349856d1a33bce2
				
def print_menu():
	print("Please select an option: ")
	print("a) Add an item to the cart\tb) Modify cart contents")
	print("c) Get cart total\td) Print database contents");
	print("e) Checkout\tq) Quit")

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
		db.write_db_file("db2.csv")
		quit()
	elif option.lower() == "q":
		pass
	else:
		print("Please enter one of the above options")

	print()
	print_menu()
	option = input()