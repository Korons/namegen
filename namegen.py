import random
import util.names

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
	counties = ['USA', 'Canada', 'Mexico', 'Sweden', 'Germany', 'Italy', 'Ireland', 'Netherlands', 'United Kingdom']
	country = random.choice(counties)
	if country == 'USA':
		states = ['Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii' ,'Idaho'
		'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
		'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
		'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
		'Wisconsin', 'Wyoming']
		state = random.choice(states)
		print country, state
	if country == 'Canada':
		states = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador',
		'Northwest Territories', 'Nova Scotia', 'Nunavut', 'Ontario', 'Prince Edward Island',
		'Quebec', 'Saskatchewan', 'Yukon']
		state = random.choice(states)
		print country, state
	else:
		print country

generate_name()
generate_phonenum()
generate_dob()
generate_country()

