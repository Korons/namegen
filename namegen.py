import random
import argparse
import sys
import string

parser = argparse.ArgumentParser(description='Generate fake data')
parser.add_argument("-n", help="Use female names", choices=['male','female'])
parser.add_argument("-o", help="Output to csv file")
parser.add_argument("-c", help="Country")
parser.add_argument("-y", help="Year range Ex 1950-1970")
args = parser.parse_args()

# The files with all the countries 
country_file = 'countries.txt'
# A file with all the states in the USA
usa_states_file = 'usa_states.txt'
# Al the states in canada
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

# This generates the phone number
def generate_phonenum():
	""" Generate a phone number """
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

def generate_dob():
	""" Generate date of birth """
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
	with open(country_file) as cf:
		counties = cf.read().splitlines()
	if args.c:
		country = args.c
	else:
		country = random.choice(counties)
	if country == 'USA':
		with open(usa_states_file) as us:
			states = us.read().splitlines()
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


generate_name()
generate_phonenum()
generate_dob()
generate_country()


