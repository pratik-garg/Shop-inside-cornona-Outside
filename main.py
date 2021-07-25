from app import *

while True:
	#print("-"*150)
	print("*"*30+" SHOP INSIDE , CORONA OUTSIDE " + "*"*30)

	#print("-"*150)

	print("1.LOGIN\n2.SIGNUP\n3.EXIT")

	choice  = input("-->")

	if choice == "1":
		user = login()
		          

		while user is not None:
			print("<-----Category----->\n1.Electronics\n2.Furniture\n3.Fashion\n4.Books\n")
			ch = input("-->")
			if ch =="1":
				#electronics list function
				electronics(user)
				greet()

				break

			elif ch =="2":
				#furniture list function
				furniture(user)
				greet()

				break

			elif ch =="3":
				fashion(user)
				greet()
				#fashion list function
				break

			elif ch == "4":
				books(user)
				greet()
				#books list function
				break

			else:
				print("ENTER A VALID CHOICE\n")
				break


	elif choice  == "2":
		signup()

	else:
		break
		
