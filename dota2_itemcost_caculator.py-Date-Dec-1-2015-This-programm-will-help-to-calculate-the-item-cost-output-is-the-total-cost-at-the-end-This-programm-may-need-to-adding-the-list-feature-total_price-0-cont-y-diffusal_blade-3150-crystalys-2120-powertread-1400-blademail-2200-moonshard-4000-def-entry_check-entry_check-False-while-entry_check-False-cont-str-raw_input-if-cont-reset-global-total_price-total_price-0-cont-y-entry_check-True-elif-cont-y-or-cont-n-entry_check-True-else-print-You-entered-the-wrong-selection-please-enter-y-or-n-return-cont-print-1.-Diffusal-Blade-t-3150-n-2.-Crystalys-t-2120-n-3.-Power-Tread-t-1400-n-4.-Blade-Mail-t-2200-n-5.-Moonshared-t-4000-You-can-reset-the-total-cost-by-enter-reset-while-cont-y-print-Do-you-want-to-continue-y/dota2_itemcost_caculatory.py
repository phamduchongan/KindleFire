#Date: Dec 1, 2015 
#This programm will help to calculate the item cost (output is the total cost at the end)
#This programm may need to adding the list feature
total_price = 0
cont = "y"
diffusal_blade = 3150 
crystalys = 2120
powertread = 1400
blademail = 2200
moonshard = 4000

def entry_check():
	entry_check = False
	while entry_check == False:
		cont = str(raw_input("> "))
		if cont == "reset":
			global total_price
			total_price = 0
			cont = "y"
			entry_check = True
		elif cont == "y" or cont == "n":
			entry_check = True 
		else:
			print "You entered the wrong selection, please enter \"y\" or \"n\" "
	return cont	
	
print """
	1. Diffusal Blade \t(3150)\n
	2. Crystalys \t(2120)\n
	3. Power Tread \t(1400)\n
	4. Blade Mail \t(2200)\n
	5. Moonshared \t(4000)

	You can reset the total cost by enter "reset"
	"""

	
while cont == "y":
	print "Do you want to continue? y/n "	
	cont = entry_check()	 
	if cont == "n":
		exit()
	print "Now, enter the item selection! "
	item_num = int(raw_input("> ")) 
	if item_num == 1:
		total_price = total_price + diffusal_blade
	elif item_num == 2:
		total_price = total_price + crystalys
	elif item_num == 3:
		total_price = total_price + powertread
	elif item_num == 4:
		total_price = total_price + blademail 
	else:
		total_price = total_price + moonshard
	print "\n \tThe total cost of your item: %i\n" %total_price
	

