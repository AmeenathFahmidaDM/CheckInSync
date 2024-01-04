#Hotel management system
import random
service=1000
rent=0
food_c=0
c_name=''
c_ad=''
cin=''
cout=''
rno=0
def cust_data():
	global c_name
	global c_ad
	global cin
	global cout
	global rno
	c_name =str(input(' enter your name :'))
	c_ad=str(input(' enter your address :'))
	cin=str(input(' enter check in date :'))
	cout=str(input(' enter checkout date :'))
	rno=random.randint(1,21)
	print(' Your room number:', rno)
	print('\n')
	hotel_main() 
def room_rent(): #rent_function
	print(' We have the following rooms for you\n 1.CLASS A--->INR 4000\n 2.CLASS B--->INR 3000\n 3.CLASS C--->INR 1500')
	(A,B,C)=(4000,3000,1500)
	#room basic rent per night
	#amount calculated at this function rent
	global rent
	while(1):
		rc=int(input(' Enter the number of your choice to proceed:'))
		if rc==1:
			#classA 4000
			n1=int(input(' How many nights you want to stay:'))
			print(' You have chosen room in CLASS A')
			rent=n1*A
			print(' Your room rent:',rent)
			break	
		elif rc==2:
			#classB 3000
			n2=int(input(' How many nights you want to stay:'))
			print(' You have chosen room in CLASS B')
			rent=n2*B
			print(' Your room rent:',rent)
			break
		elif rc==3:
			#classC 1500
			n3=int(input(' How many nights you want to stay:'))
			print(' You have chosen room in CLASS C')
			rent=n3*C
			print(' Your room rent:',rent)
			break
		else:
			print(' PLEASE ENTER A VALID KEY')	
	print('\n')
	hotel_main()
def food():
	print('          ******OUR RESTURANT MENU******           ')
	print(' 1.Drinks--->INR 50\n 2.Dessert--->INR 100\n 3.Breakfast--->INR 100\n 4.Lunch--->INR 200\n 5.Dinner--->INR 150\n 6.Exit')
	(d,des,b,l,di)=(50,100,100,200,150)
	global food_c
	food_c=0
	while(1):
		f=int(input(' Enter the number of your choice to proceed:'))
		if f==1: #drinks
			q1=int(input(' Enter quantity: '))
			f1=q1*d
			food_c+=f1
		elif f==2: # dessert
			q2=int(input(' Enter quantity:'))
			f2=q2*des
			food_c+=f2
		elif f==3: #Breakfast
			q3=int(input(' Enter quantity:'))
			f3=q3*b
			food_c+=f3
		elif f==4: #Lunch
			q4=int(input(' Enter quantity:'))
			f4=q4*l
			food_c+=f4
		elif f==5: #Dinner
			q5=int(input(' Enter quantity:'))
			f5=q5*di
			food_c+=f5
		elif f==6:
			break
		else:
			print(' PLEASE ENTER A VALID KEY')
	print(' Your total food cost :',food_c)
	print('\n')
	hotel_main()				
def total(): #displays cust details incl amount
	global c_name
	global c_ad
	global cin
	global cout
	global rno
	global rent
	global food_c
	print(' ***HOTEL BILL*** ')
	print(' CUSTOMER DETAILS')
	print(' Customer name:',c_name)
	print(' Customer address:',c_ad)
	print(' Check in date:',cin)
	print(' Check out date:',cout)
	print(' Your room number',rno)
	print(' Your room rent:',rent)
	print(' Your food bill:',food_c)
	sub=rent+food_c
	print(' Your sub total purchased:',sub)
	print(' Service charges:', service)
	total=sub+service
	print(' Your grand total:',total)
	print(' ***THANK YOU ! VISIT AGAIN*** ')	

				
def hotel_main(): #MAIN FUNCTION
	print(' 1.Enter customer details\n 2.Calculate room rent amount\n 3.Calculate food amount\n 4.Show total cost\n 5.Exit')# main display
	c=int(input('\n Enter the number of your choice to proceed:'))
	if c==1:
		cust_data()
	elif c==2:
		room_rent()
	elif c==3:
		food()
	elif c==4:
		total()
	elif c==5:
		exit()
#Start
print('          ******WELCOME TO ABCDXYZ HOTEL******           ')

hotel_main() #main function call
