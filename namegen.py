import random
import util.names

country_file = 'countries.txt'
usa_states_file = 'usa_states.txt'
canada_states_file = 'canada_states.txt'

def generate_name():
	""" Generate a fake name """
	male_firstnames, female_firstnames, lastnames = util.names.load_all_names()
	first = random.choice(male_firstnames)
	last = random.choice(lastnames)
	print first, last
	base = "https://mailinator.com/inbox.jsp?to="
	email = base + first + "." + last
	print email

def generate_phonenum():
	""" Generate a phone number """
	phone_first = random.randint(111,999)
	phone_second = random.randint(111,999)
	phone_third = random.randint(1111,9999)
	print  phone_first, phone_second, phone_third

def generate_dob():
	""" Generate date of birth """
	year = random.randint(1950,2000)
	month = random.randint(1,12)
	day = random.randint(1,30)
	print year,'/',month,'/',day

def generate_country():
	with open(country_file) as cf:
		counties = cf.read().splitlines()
	country = random.choice(counties)
	if country == 'USA':
		with open(usa_states_file) as us:
			states = us.read().splitlines()
		state = random.choice(states)
		print country, state
	elif country == 'Canada':
		with open(canada_states_file) as cs:
			states = cs.read().splitlines()
		state = random.choice(states)
		print country, state
	else:
		print country


generate_name()
generate_phonenum()
generate_dob()
generate_country()
