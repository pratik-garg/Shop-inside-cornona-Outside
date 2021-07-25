from peewee import *

db = SqliteDatabase('wanted1.db')

class User(Model):
	username = CharField()
	password = CharField()

	class Meta:
		database = db

# class Wallet(Model):
# 	owner  = ForeignKeyField(User,backref = "wallets")
# 	name = CharField()
# 	balance  = FloatField()
# 	last_transaction  = DateTimeField()

# 	class Meta:
# 		database = db

# class product(Model):
# 	owner = ForeignKeyField(User,backref = "products")
# 	wal = ForeignKeyField(Wallet,backref = "wallet_expenses")
# 	name = CharField()
# 	from_person = CharField()
# 	amount = FloatField()
# 	timestamp = DateTimeField()
# 	comment = CharField()
# 	is_expense = BooleanField()

# 	class Meta:
# 		database = db

class Product(Model):
	owner = ForeignKeyField(User,backref = "products")
	product_name  = CharField()
	price =  FloatField()

	class Meta:
		database = db
# class cart(Model):
# 	owner = ForeignKeyField(User,backref = "carts")
# 	product = ForeignKeyField(Product,backref = "products")

if __name__ == "__main__":
	db.connect()
	db.create_tables([User,Product])