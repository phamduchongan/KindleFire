#This program will calculate the damge of hero with stats
#Name: An Pham
#Collaborator: 
#Time: Nov 21, 2015 15:53 

global hero_str_result
global hero_agi_result
global hero_int_result

def hero_selection():
	print """1. Life Stealer (strength hero) \n 2. Phantom lancer (agility hero)\n 3. Phantom Assassin (agility hero)\n 4. Wrait King (strength hero) \n
	"""
	
	print "Please enter hero selection: "
	hero_num = int(raw_input("> "))
	return hero_num

def hero_attribute(hero_num):#This syntax isn't accepted 
	if hero_num == 1: # Life stealer 
		hero_str = 25 
		hero_agi = 18 
		hero_int = 15 
		#Hero growth stats
		str_growth = 2.4 
		agi_growth = 1.9 
		int_growth = 1.75 
	
	elif hero_num == 2: # Phantom lancer 
		hero_str = 21 
		hero_agi = 29
		hero_int = 21
		#Hero growth stats
		str_growth = 2.4
		agi_growth = 1.9
		int_growth = 1.75

	elif hero_num == 3: # Phantom Assassin
		hero_str = 20 
		hero_agi = 23
		hero_int = 13
		#Hero growth stats
		str_growth = 1.85 
		agi_growth = 3.15
		int_growth = 1
	else: #Wraith King
		hero_str = 22
		hero_agi = 18
		hero_int = 18
		#hero growth stats
		str_growth = 2.9
		agi_growth = 1.7
		int_growth = 1.6	
	return (hero_str,hero_agi,hero_int,str_growth,agi_growth,int_growth)

def hero_type(hero_num):
	if hero_num == 1:
		hero_type = "str"
	elif hero_num == 2:
		hero_type = "agi"
	elif hero_num == 3:
		hero_type = "agi"	
	else:
		hero_type = "str"


#the function will ask user what to do with the hero
def hero_build():
	print "What do you want to do with the hero?"
	print """1. Build hero with stat\n2. Build hero with item (not yet)\n3. Build hero with level
		"""
	
	user_choice = int(raw_input("> "))
	if user_choice == 1:
		print "You want to build hero with stats!"
		print "Please enter number of stats that you want to add: "
		hero_stats = int(raw_input("> "))
		print "This is hero stat: ", hero_stats
		print "You will be prompted to ask which hero are you going to choose !"
		hero_str, hero_agi, hero_int,str_growth,agi_growth,int_growth = hero_attribute(hero_selection()) #This function will take the result of hero_str, hero_agi,hero_int
		hero_str_result = hero_str + str_growth * hero_stats
		hero_agi_result = hero_agi + agi_growth * hero_stats
		hero_int_result = hero_int + int_growth * hero_stats	

	print "This is the research of your build: %i strength, %i agility, %i intelligence" %(hero_str_result, hero_agi_result, hero_int_result)	
	return hero_str_result, hero_agi_result, hero_int_result


hero_build()
