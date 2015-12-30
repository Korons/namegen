import random
import argparse

parser = argparse.ArgumentParser(description='Generate fake data')
parser.add_argument("-n", help="Use female names", choices=['male','female'])
parser.add_argument("-o",help="Output to csv file")
args = parser.parse_args()


country_file = 'countries.txt'
usa_states_file = 'usa_states.txt'
canada_states_file = 'canada_states.txt'
male_names = 'male-first.txt'
female_names = 'female-first.txt'
last_names = 'lastnames.txt'
def generate_name():
	""" Generate a fake name """
	if args.n == 'female':
		with open(female_names) as fen:
			fn = fen.read().splitlines()
	else:
		with open(male_names) as mn:
			fn = mn.read().splitlines()
	with open(last_names) as ln:
		lastname = ln.read().splitlines()
	first = random.choice(fn)
	last = random.choice(lastname)
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
		user_name_how = random.randint(1, 2)
		if user_name_how == 1:
			user_name = first[0] + last
		elif user_name_how == 2:
			user_name = first[0:2] + last[0:2]
		print user_name
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
