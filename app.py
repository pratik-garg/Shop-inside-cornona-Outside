from models import *
from datetime import datetime

db.connect()

def greet():
	print("THANK YOU FOR SHOPPING !!!\n     visit again:)")

def bill(user):
	print("*"*10+" SHOP INSIDE , CORONA OUTSIDE!! "+ " *"*10)
	print("-"*4+"INVOICE"+"-"*4)
	print("NAME:"+user.username)
	# print("Product:"+product_name)
	# print("Price:"+price)

def signup():
	username = input("Create username: ")
	password = input("Create password: ")

	exists = len(User.select().where(User.username == username))

	if not exists:
		User.create(username=username, password=password)
		print("User created Successfully!\n\n")
	else:
		print("Username already exists. Please try new username.")


def login():
	username = input("Enter username: ")
	password = input("Enter password: ")

	user = User.select().where(User.username == username)

	if len(user):
		user = user.get()

		if user.password == password:
			print("\nLogin Successfull!\n")
			return user
		else:
			print("Invalid Password.\n\n")

	else:
		return None

def electronics(user):
	print("\n1.Mobile phones\n2.Laptops\n3.Computer Accessories\n4.Power Bank\n")
	ch = input("\n-->")
	if ch == "1":
		product_name = "IPhone"
		price = 100000

	elif ch =="2":
		product_name = "Dell"
		price = 50000

	elif ch =="3":
		product_name = "keyboard"
		price =  1000

	elif ch == "4":
		product_name = "Syska"
		price = 1500

	else:
		print("Not available\n")

	Product.create(owner = user,product_name = product_name,price = price)
	bill(user)
	print("PRODUCT:"+product_name)
	print("PRICE:",price)
	print("Yaay!!! you got a corona mask free!!!\n")


def furniture(user):
	print("\n1.Dining Table\n2.Chair\n3.Beds \n4.Wooden almirah\n")
	ch = input("\n-->")
	if ch == "1":
		product_name = "Dining Table"
		price = 10000

	elif ch =="2":
		product_name = "Chair"
		price = 5000

	elif ch =="3":
		product_name = "Beds"
		price =  100000

	elif ch == "4":
		product_name = "Almirah"
		price = 15000

	else:
		print("Not available\n")
		

	Product.create(owner = user,product_name = product_name,price = price)
	bill(user)
	print("PRODUCT:"+product_name)
	print("PRICE:",price)
	print("Yaay!!! you got a corona mask free!!!\n")

def fashion(user):
	print("\n1.Shirts\n2.T-shirts\n3.Jeans \n4.Jackets\n")
	ch = input("\n-->")
	if ch == "1":
		product_name = "Raymond"
		price = 2500

	elif ch =="2":
		product_name0= "U.S POLO"
		price = 5000

	elif ch =="3":
		product_name = "FLYING MACHINE"
		price =  1000

	elif ch == "4":
		product_name = "ALLEN SOLLY"
		price = 1500

	else:
		print("Not available\n")
		

	Product.create(owner = user,product_name = product_name,price = price)
	bill(user)
	print("PRODUCT:"+product_name)
	print("PRICE:",price)
	print("Yaay!!! you got a corona mask free!!!\n")

def books(user):
	print("\n1.Novels\n2.Vtu textsbooks\n3.Comics \n4.Magazines\n")
	ch = input("\n-->")
	if ch == "1":
		product_name = "Turtles All The Way Down -John green"
		price = 250

	elif ch =="2":
		product_name= "K.S.C MATHS "
		price = 5

	elif ch =="3":
		product_name = "MARVEL"
		price =  100

	elif ch == "4":
		product_name = "PLAYBOY Magazine"
		price = 150

	else:
		print("Not available\n")
		

	Product.create(owner = user,product_name = product_name,price = price)
	bill(user)
	print("PRODUCT:"+product_name)
	print("PRICE:",price)
	print("Yaay!!! you got a corona mask free!!!\n")


# def show_cart(user):
# 	while _ in user.Product():
# 		print(_)

# def create_wallet(user):
# 	name = input("Enter Wallet Name: ")
# 	bal = input("Enter Starting Balance: ")
# 	wallet = Wallet.create(name=name, balance=bal, owner=user, last_transaction=datetime.now())
# 	print("\nWallet Created Successfully..\nCurrent Balance: 0")

# def add_transaction(user):
# 	wallets = user.wallets

# 	for wallet in wallets:
# 		print(wallet.id, wallet.name, wallet.balance)

# 	ch = int(input("\nChoose a Wallet ID: "))

# 	wallet = Wallet.get(Wallet.id == ch)
# 	is_expense = int(input("\nChoose Type:\n0. Income\n1. Expense\n-->"))

# 	if not is_expense:
# 		from_person = input("From Who: ")
# 	else:
# 		from_person = "None"

# 	trans_name = input("Enter Purpose: ")
# 	amount = float(input("Enter Amount: "))
# 	comment = input("Any comments? \n")

# 	Transaction.create(owner=user,
# 		wallet=wallet,
# 		name=trans_name,
# 		amount=amount,
# 		from_person=from_person,
# 		timestamp=datetime.now(),
# 		comment=comment,
# 		is_expense=bool(is_expense))

# 	if not is_expense:
# 		wallet.balance += amount
# 	else:
# 		if amount > wallet.balance:
# 			print("--! Balance not Sufficient. Please Add Money before you Borrow. !--")
# 		else: 
# 			wallet.balance -= amount
	
# 	wallet.save()


# def check_balance(user):
# 	wallets = user.wallets

# 	for wallet in wallets:
# 		print(wallet.id, wallet.name, wallet.balance)


# def see_transaction(user):
# 	trans = user.expenses

# 	for txn in trans:
# 		if txn.is_expense:
# 			print(txn.wallet, txn.name, f"-{txn.amount}", txn.timestamp)
# 		else:
# 			print(txn.wallet, txn.name, f"+{txn.amount}", txn.timestamp)

# def check_balance(user):
# 	wallets = user.wallets

# 	for wallet in wallets:
# 		print(wallet.id, wallet.name, wallet.balance)