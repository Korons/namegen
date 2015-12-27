import random

import util.names

def generate_name():
    """ Generate a fake name """
    male_firstnames, female_firstnames, lastnames = util.names.load_all_names()
    first = random.choice(male_firstnames)
    last = random.choice(lastnames)

    print first, last

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

def throwaway_email():
	""" Generate a throwaway email """
	male_firstnames, female_firstnames, lastnames = util.names.load_all_names()
	first = random.choice(male_firstnames)
	last = random.choice(lastnames)
	base = "https://mailinator.com/inbox.jsp?to="
	email = base + first + "." + last
	print email

generate_name()
generate_phonenum()
generate_dob()
throwaway_email()
