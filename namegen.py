import random
import argparse
import sys
import string

parser = argparse.ArgumentParser(description='Generate fake data')
parser.add_argument("-n", help="Use female names", choices=['male','female'])
parser.add_argument("-o", help="Output to csv file")
parser.add_argument("-c", help="Country")
parser.add_argument("-y", help="Year range Ex 1950-1970")
parser.add_argument("-l", help="The number of times to loop")
args = parser.parse_args()

#Gobal vars

state = ''


# The files with all the countries 
country_file = 'countries.txt'
# A file with all the states in the USA
usa_states_file = 'usa_states.txt'
# All the states in canada
canada_states_file = 'canada_states.txt'
# A file of all the male names you want to choose from
male_names = 'male-first.txt'
# A file of all the female names you want to choose from
female_names = 'female-first.txt'
# A file with all the lastnames you want to choose from
last_names = 'lastnames.txt'

# This generates the name, email and username
def generate_name():
	char_set = string.ascii_uppercase + string.digits
	randstring = ''.join(random.sample(char_set*6, 6))
	if args.n == 'female':
		with open(female_names) as fen:
			fn = fen.read().splitlines()
	elif args.n =='male':
		with open(male_names) as mn:
			fn = mn.read().splitlines()
	else:
		morf = random.randint(1,2)
		if morf == 1:
			with open(male_names) as mn:
				fn = mn.read().splitlines()
		elif morf == 2:
			with open(female_names) as fen:
				fn = fen.read().splitlines()
		else:
			print "Error: Unexpected vaule in generate_name\nExiting"
			sys.exit()
	with open(last_names) as ln:
		lastname = ln.read().splitlines()
	first = random.choice(fn)
	last = random.choice(lastname)
	#Changes the names to lower case
	first = first.lower()
	last = last.lower()
	#Caps the first letter of each name
	first = first[:1].upper() + first[1:]
	last = last[:1].upper() + first[1:]
	# This if is for writing to a csv file
	if args.o:
		f = open(args.o,"a")
		f.write(first)
		f.write(';')
		f.write(last)
		f.write(';')
		f.close
	else:
		print first, last
		base = "https://mailinator.com/inbox.jsp?to="
		email = base + first + "." + last
		print email
		# I'm using a bunch of if/elif for this because python does not have a switch statment
		user_name_how = random.randint(1, 9)
		if user_name_how == 1:
			user_name = first[0] + last
		elif user_name_how == 2:
			user_name = first[0:2] + last[0:2]
		elif user_name_how == 3:
			user_name = first[2:5] + last[0:5]
		elif user_name_how == 4:
			user_name = first[1:2] + last
		elif user_name_how == 5:
			user_name = first[0:2] + first[3:4]
		elif user_name_how == 6:
			user_name = last[0:2] + last[1]
		elif user_name_how == 7:
			user_name = first[2:4] + last[0:3]
		elif user_name_how == 8:
			numbs = random.randint(10, 100)
			numbs = str(numbs)
			user_name = first[0] + last + " " + numbs
			user_name = user_name.replace(" ", "")
		elif user_name_how == 9:
			user_name = first + randstring
		else:
			print "Error: Unexpected vaule in generate_name\nExiting"
			sys.exit()
		print user_name


def generate_dob():
	if args.y:
		year_range = args.y
		# This is weird. Shouldn't it be 0:3 and 5:9? because the list should start at 0 and end at 3 which would be 4 numbers
		range_1 = year_range[0:4]
		range_2 = year_range[5:9]
		year = random.randint(int(range_1), int(range_2))
	else:
		year = random.randint(1950,2000)
	month = random.randint(1,12)
	day = random.randint(1,30)
	if args.o:
		f = open(args.o,"a")
		f.write(str(day))
		f.write(';')
		f.write(str(month))
		f.write(';')
		f.write(str(year))
		f.write(';')
		f.close

	else:
		print year,'/',month,'/',day

def generate_country():	
	if args.c:
		country = args.c
	else:
		with open(country_file) as cf:
			counties = cf.read().splitlines()
		country = random.choice(counties)
	if country == 'USA':
		with open(usa_states_file) as us:
			states = us.read().splitlines()
		global state
		state = random.choice(states)
		if args.o:
			f = open(args.o,"a")
			f.write(country)
			f.write(';')
			f.write(state)
			f.write(';')
			f.write('\n')
			f.close
		else:
			print country, state
	elif country == 'Canada':
		with open(canada_states_file) as cs:
			states = cs.read().splitlines()
		state = random.choice(states)
		if args.o:
			f = open(args.o,"a")
			f.write(country)
			f.write(';')
			f.write(state)
			f.write(';')
			f.write('\n')
			f.close
		else:
			print country, state
	else:
		if args.o:
			f = open(args.o,"a")
			f.write(country)
			f.write('\n')
			f.close
		else:
			print country

# This generates the phone number
def generate_phonenum():
	alab_codes = [205, 251, 256, 334, 938]
	alas_codes = 907
	ariz_codes = [480, 520, 602, 623, 928]
	arka_codes = [479, 501, 870]
	cali_codes = [209, 213, 310, 323, 408, 415, 424, 442, 510, 530, 559, 562, 619, 626, 650, 657, 661, 669, 707, 714, 747, 760, 805, 818, 831, 858, 909, 916, 925, 949, 951]
	colo_codes = [303, 719, 720, 970]
	conn_codes = [203, 475, 860]
	dela_codes = [302]
	flor_codes = [239, 305, 321, 352, 386, 407, 561, 727, 754, 772, 786, 813, 850, 863, 904, 941, 954]
	gero_codes = [229, 404, 470, 478, 678, 706, 762, 770, 912]
	hawa_codes = [808]
	idah_codes = [208]
	illi_codes = [217, 224, 309, 312, 331, 618, 630, 708, 773, 779, 815, 847, 872]
	indi_codes = [219, 260, 317, 574, 765, 812]
	iowa_codes = [319, 515, 563, 641, 712]
	kans_codes = [316, 620, 785, 913]
	kent_codes = [270, 502, 606, 859]
	loui_codes = [225, 318, 337, 504, 985]
	main_codes = [207]
	mary_codes = [240, 301, 410, 443, 667]
	mass_codes = [339, 351, 413, 508, 617, 774, 781, 857, 978]
	mich_codes = [231, 248, 269, 313, 517, 586, 616, 734, 810, 906, 947, 989]
	if state == "Alabama":
		phone_first = random.choice(alab_codes)
	elif state == "Alaska":
		phone_first = random.choice(alas_codes)
	elif state == "Arizona":
		phone_first = random.choice(ariz_codes)
	elif state == "Arkansas":
		phone_first = random.choice(arka_codes)
	elif state == "California":
		phone_first = random.choice(cali_codes)
	elif state == "Colorado":
		phone_first = random.choice(colo_codes)
	elif state == "Connecticut":
		phone_first = random.choice(conn_codes)
	elif state == "Delaware":
		phone_first = random.choice(dela_codes)
	elif state == "Florida":
		phone_first = random.choice(flor_codes)
	elif state == "Georgia":
		phone_first = random.choice(gero_codes)
	elif state == "Hawaii":
		phone_first = random.choice(hawa_codes)
	elif state == "Idaho":
		phone_first = random.choice(idah_codes)
	elif state == "Illinois":
		phone_first = random.choice(illi_codes)
	elif state == "Indiana":
		phone_first = random.choice(indi_codes)
	elif state == "Iowa":
		phone_first = random.choice(iowa_codes)
	elif state == "Kansas":
		phone_first = random.choice(kans_codes)
	elif state == "Kentucky":
		phone_first = random.choice(kent_codes)
	elif state == "Louisiana":
		phone_first = random.choice(loui_codes)
	elif state == "Maine":
		phone_first = random.choice(main_codes)
	elif state == "Maryland":
		phone_first = random.choice(mary_codes)
	elif state == "Massachusetts":
		phone_first = random.choice(mass_codes)
	else:
		phone_first = random.randint(100,999)
	phone_second = random.randint(100,999)
	phone_third = random.randint(1000,9999)
	if args.o:
		f = open(args.o,"a")
		f.write(str(phone_first))
		f.write(str(phone_second))
		f.write(str(phone_third))
		f.write(';')
		f.close
	else:
		print  phone_first, phone_second, phone_third

generate_name()
generate_dob()
generate_country()
generate_phonenum()

if args.l:
	run_range = args.l
	# we start at 1 and 0 here because we already ran once above this
	for x in range(1, int(run_range)):
		generate_name()
		generate_phonenum()
		generate_dob()
		generate_country()
