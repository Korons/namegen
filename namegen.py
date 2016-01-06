#!/usr/bin/python2.7 
import random
import argparse
import sys
import string
import copy
from random import Random

# Creditcard code from https://github.com/grahamking/darkcoding-credit-card
visaPrefixList = [
        ['4', '5', '3', '9'],
        ['4', '5', '5', '6'],
        ['4', '9', '1', '6'],
        ['4', '5', '3', '2'],
        ['4', '9', '2', '9'],
        ['4', '0', '2', '4', '0', '0', '7', '1'],
        ['4', '4', '8', '6'],
        ['4', '7', '1', '6'],
        ['4']]

mastercardPrefixList = [
        ['5', '1'], ['5', '2'], ['5', '3'], ['5', '4'], ['5', '5']]

amexPrefixList = [['3', '4'], ['3', '7']]

discoverPrefixList = [['6', '0', '1', '1']]

dinersPrefixList = [
        ['3', '0', '0'],
        ['3', '0', '1'],
        ['3', '0', '2'],
        ['3', '0', '3'],
        ['3', '6'],
        ['3', '8']]

enRoutePrefixList = [['2', '0', '1', '4'], ['2', '1', '4', '9']]

jcbPrefixList = [['3', '5']]

voyagerPrefixList = [['8', '6', '9', '9']]


def completed_number(prefix, length):
    """
    'prefix' is the start of the CC number as a string, any number of digits.
    'length' is the length of the CC number to generate. Typically 13 or 16
    """

    ccnumber = prefix

    # generate digits

    while len(ccnumber) < (length - 1):
        digit = str(generator.choice(range(0, 10)))
        ccnumber.append(digit)

    # Calculate sum

    sum = 0
    pos = 0

    reversedCCnumber = []
    reversedCCnumber.extend(ccnumber)
    reversedCCnumber.reverse()

    while pos < length - 1:

        odd = int(reversedCCnumber[pos]) * 2
        if odd > 9:
            odd -= 9

        sum += odd

        if pos != (length - 2):

            sum += int(reversedCCnumber[pos + 1])

        pos += 2

    # Calculate check digit

    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10

    ccnumber.append(str(checkdigit))

    return ''.join(ccnumber)


def credit_card_number(rnd, prefixList, length, howMany):

    result = []

    while len(result) < howMany:

        ccnumber = copy.copy(rnd.choice(prefixList))
        result.append(completed_number(ccnumber, length))

    return result


def output(title, numbers):

    result = []
    result.append(title)
    result.append('-' * len(title))
    result.append('\n'.join(numbers))
    result.append('')

    return '\n'.join(result)

#
# Main
#

generator = Random()
generator.seed()        # Seed from current time

mastercard = credit_card_number(generator, mastercardPrefixList, 16, 1)
visa16 = credit_card_number(generator, visaPrefixList, 16, 1)
visa13 = credit_card_number(generator, visaPrefixList, 13, 1)
amex = credit_card_number(generator, amexPrefixList, 15, 1)
# Minor cards

discover = credit_card_number(generator, discoverPrefixList, 16, 1)
diners = credit_card_number(generator, dinersPrefixList, 14, 1)
enRoute = credit_card_number(generator, enRoutePrefixList, 15, 1)
jcb = credit_card_number(generator, jcbPrefixList, 16, 1)
voyager = credit_card_number(generator, voyagerPrefixList, 15, 1)
mastercard =''.join(mastercard)
visa16 = ''.join(visa16)
visa13 = ''.join(visa13)
amex = ''.join(amex)
discover = ''.join(discover)
diners = ''.join(diners)
enRoute = ''.join(enRoute)
jcb = ''.join(jcb)
voyager = ''.join(voyager)




parser = argparse.ArgumentParser(description='Generate fake data')
parser.add_argument("-n", help="Use female names", choices=['male','female'])
parser.add_argument("-o", help="Output to csv file")
parser.add_argument("-c", help="Country")
parser.add_argument("-y", help="Year range Ex 1950-1970")
parser.add_argument("-l", help="The number of times to loop")
parser.add_argument("-k", help="Creditcard type", choices=['mastercard','visa16','visa13','amex','discover','diners','enRoute','jcb','voyager'], default='mastercard')
args = parser.parse_args()

#Gobal vars

state = ''


# The files with all the countries 
country_file = 'countries.txt'
# A file with all the states in the USA
usa_states_file = 'usa_states.txt'
# All the states in canada
canada_states_file = 'canada_states.txt'
german_states_file = 'german_states.txt'
mexico_states_file = 'mexico_states.txt'
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
	last = last[:1].upper() + last[1:]
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
			f.close
	elif country == 'Germany':
		with open(german_states_file) as cs:
			states = cs.read().splitlines()
		state = random.choice(states)
		if args.o:
			f = open(args.o,"a")
			f.write(country)
			f.write(';')
			f.write(state)
			f.write(';')
			f.close
	elif country == 'Mexico':
		with open(mexico_states_file) as cs:
			states = cs.read().splitlines()
		state = random.choice(states)
		if args.o:
			f = open(args.o,"a")
			f.write(country)
			f.write(';')
			f.write(state)
			f.write(';')
			f.close
		else:
			print country, state
	else:
		if args.o:
			f = open(args.o,"a")
			f.write(country)
			f.write(';')
			f.close
		else:
			print country
def creditcard():
	if args.k == 'mastercard':
		if args.o:
			f = open(args.o,"a")
			f.write(mastercard)
			f.write(';')
			f.write('\n')
			f.close
		else:
			print mastercard
	elif args.k == 'visa16':
		if args.o:
			f = open(args.o,"a")
			f.write(visa16)
			f.write(';')
			f.write('\n')
			f.close
		else:
			print visa16
	elif args.k == 'visa13':
		if args.o:
			f = open(args.o,"a")
			f.write(visa13)
			f.write(';')
			f.write('\n')
			f.close
		else:
			print visa13
	elif args.k == 'amex':
		if args.o:
			f = open(args.o,"a")
			f.write(amex)
			f.write(';')
			f.write('\n')
			f.close
		else:
			print amex
	elif args.k == 'discover':
		if args.o:
			f = open(args.o,"a")
			f.write(discover)
			f.write(';')
			f.write('\n')
			f.close
		else:
			print discover
	elif args.k == 'diners':
		if args.o:
			f = open(args.o,"a")
			f.write(diners)
			f.write(';')
			f.write('\n')
			f.close
		else:
			print diners
	elif args.k == 'enRoute':
		if args.o:
			f = open(args.o,"a")
			f.write(enRoute)
			f.write(';')
			f.write('\n')
			f.close
		else:
			print enRoute
	elif args.k == 'jcb':
		if args.o:
			f = open(args.o,"a")
			f.write(jcb)
			f.write(';')
			f.write('\n')
			f.close
		else:
			print jcb
	elif args.k == 'voyager':
		if args.o:
			f = open(args.o,"a")
			f.write(voyager)
			f.write(';')
			f.write('\n')
			f.close
		else:
			print voyager
	else:
		print "Error in credit card gen\nExiting"
		sys.exit()
# This generates the phone number
def generate_phonenum():
	alab_codes_usa = [205, 251, 256, 334, 938]
	alas_codes_usa = [907]
	ariz_codes_usa = [480, 520, 602, 623, 928]
	arka_codes_usa = [479, 501, 870]
	cali_codes_usa = [209, 213, 310, 323, 408, 415, 424, 442, 510, 530, 559, 562, 619, 626, 650, 657, 661, 669, 707, 714, 747, 760, 805, 818, 831, 858, 909, 916, 925, 949, 951]
	colo_codes_usa = [303, 719, 720, 970]
	conn_codes_usa = [203, 475, 860]
	dela_codes_usa = [302]
	flor_codes_usa = [239, 305, 321, 352, 386, 407, 561, 727, 754, 772, 786, 813, 850, 863, 904, 941, 954]
	gero_codes_usa = [229, 404, 470, 478, 678, 706, 762, 770, 912]
	hawa_codes_usa = [808]
	idah_codes_usa = [208]
	illi_codes_usa = [217, 224, 309, 312, 331, 618, 630, 708, 773, 779, 815, 847, 872]
	indi_codes_usa = [219, 260, 317, 574, 765, 812]
	iowa_codes_usa = [319, 515, 563, 641, 712]
	kans_codes_usa = [316, 620, 785, 913]
	kent_codes_usa = [270, 502, 606, 859]
	loui_codes_usa = [225, 318, 337, 504, 985]
	main_codes_usa = [207]
	mary_codes_usa = [240, 301, 410, 443, 667]
	mass_codes_usa = [339, 351, 413, 508, 617, 774, 781, 857, 978]
	mich_codes_usa = [231, 248, 269, 313, 517, 586, 616, 734, 810, 906, 947, 989]
	minn_codes_usa = [218, 320, 507, 612, 651, 763, 952]
	miss_codes_usa = [228, 601, 662, 769]
	misso_codes_usa = [314, 417, 573, 636, 660, 816]
	mont_codes_usa = [406]
	nebr_codes_usa = [308, 402, 531]
	neva_codes_usa = [702, 725, 775]
	nham_codes_usa = [603]
	njer_codes_usa = [201, 551, 609, 732, 848, 856, 862, 908, 973]
	nmex_codes_usa = [505, 575]
	nyor_codes_usa = [212, 315, 347, 516, 518, 585, 607, 631, 646, 716, 718, 845, 914, 917, 929]
	ncar_codes_usa = [252, 336, 704, 828, 910, 919, 980, 984]
	ndak_codes_usa = [701]
	ohio_codes_usa = [216, 234, 330, 419, 440, 513, 567, 614, 740, 937]
	okla_codes_usa = [405, 539, 580, 918]
	oreg_codes_usa = [458, 503, 541, 971]
	penn_codes_usa = [215, 267, 272, 412, 484, 570, 610, 717, 724, 814, 878]
	risl_codes_usa = [401]
	scar_codes_usa = [803, 843, 864]
	sdak_codes_usa = [605]
	tenn_codes_usa = [423, 615, 731, 865, 901, 931]
	texa_codes_usa = [210, 214, 254, 281, 325, 346, 361, 409, 430, 432, 469, 512, 682, 713, 737, 806, 817, 830, 832, 903, 915, 936, 940, 956, 972, 979]
	utah_codes_usa = [385, 435, 801]
	verm_codes_usa = [802]
	virg_codes_usa = [276, 434, 540, 571, 703, 757, 804]
	wash_codes_usa = [206, 253, 360, 425, 509]
	wads_codes_usa = [202]
	wvir_codes_usa = [304, 681]
	wisc_codes_usa = [262, 414, 534, 608, 715, 920]
	wyom_codes_usa = [307]
	#Canada codes
	albe_codes_canada = [403, 587, 780]
	bcol_codes_canada = [236, 250, 604, 778]
	mani_codes_canada = [204, 431]
	nbru_codes_canada = [506]
	nela_codes_canada = [709]
	note_codes_canada = [867]
	nosc_codes_canada = [782, 902]
	nuna_codes_canada = [867]
	onta_codes_canada = [226, 249, 289, 343, 365, 416, 437, 519, 613, 647, 705, 807, 905]
	peis_codes_canada = [782, 902]
	queb_codes_canada = [418, 438, 450, 514, 579, 581, 819, 873]
	sask_codes_canada = [306, 639]
	yuko_codes_canada = [867]
	if state == "Alabama":
		phone_first = random.choice(alab_codes_usa)
	elif state == "Alaska":
		phone_first = random.choice(alas_codes_usa)
	elif state == "Arizona":
		phone_first = random.choice(ariz_codes_usa)
	elif state == "Arkansas":
		phone_first = random.choice(arka_codes_usa)
	elif state == "California":
		phone_first = random.choice(cali_codes_usa)
	elif state == "Colorado":
		phone_first = random.choice(colo_codes_usa)
	elif state == "Connecticut":
		phone_first = random.choice(conn_codes_usa)
	elif state == "Delaware":
		phone_first = random.choice(dela_codes_usa)
	elif state == "Florida":
		phone_first = random.choice(flor_codes_usa)
	elif state == "Georgia":
		phone_first = random.choice(gero_codes_usa)
	elif state == "Hawaii":
		phone_first = random.choice(hawa_codes_usa)
	elif state == "Idaho":
		phone_first = random.choice(idah_codes_usa)
	elif state == "Illinois":
		phone_first = random.choice(illi_codes_usa)
	elif state == "Indiana":
		phone_first = random.choice(indi_codes_usa)
	elif state == "Iowa":
		phone_first = random.choice(iowa_codes_usa)
	elif state == "Kansas":
		phone_first = random.choice(kans_codes_usa)
	elif state == "Kentucky":
		phone_first = random.choice(kent_codes_usa)
	elif state == "Louisiana":
		phone_first = random.choice(loui_codes_usa)
	elif state == "Maine":
		phone_first = random.choice(main_codes_usa)
	elif state == "Maryland":
		phone_first = random.choice(mary_codes_usa)
	elif state == "Massachusetts":
		phone_first = random.choice(mass_codes_usa)
	elif state == "Michigan":
		phone_first = random.choice(mich_codes_usa)
	elif state == "Minnesota":
		phone_first = random.choice(minn_codes_usa)
	elif state == "Mississippi":
		phone_first = random.choice(miss_codes_usa)
	elif state == "Missouri":
		phone_first = random.choice(misso_codes_usa)
	elif state == "Montana":
		phone_first = random.choice(mont_codes_usa)
	elif state == "Nebraska":
		phone_first = random.choice(nebr_codes_usa)
	elif state == "Nevada":
		phone_first = random.choice(neva_codes_usa)
	elif state == "New Hampshire":
		phone_first = random.choice(nham_codes_usa)
	elif state == "New Jersey":
		phone_first = random.choice(njer_codes_usa)
	elif state == "New Mexico":
		phone_first = random.choice(nmex_codes_usa)
	elif state == "New York":
		phone_first = random.choice(nyor_codes_usa)
	elif state == "North Carolina":
		phone_first = random.choice(ncar_codes_usa)
	elif state == "North Dakota":
		phone_first = random.choice(ndak_codes_usa)
	elif state == "Ohio":
		phone_first = random.choice(ohio_codes_usa)
	elif state == "Oklahoma":
		phone_first = random.choice(okla_codes_usa)
	elif state == "Oregon":
		phone_first = random.choice(oreg_codes_usa)
	elif state == "Pennsylvania":
		phone_first = random.choice(penn_codes_usa)
	elif state == "Rhode Island":
		phone_first = random.choice(risl_codes_usa)
	elif state == "South Carolina":
		phone_first = random.choice(scar_codes_usa)
	elif state == "South Dakota":
		phone_first = random.choice(sdak_codes_usa)
	elif state == "Tennessee":
		phone_first = random.choice(tenn_codes_usa)
	elif state == "Texas":
		phone_first = random.choice(texa_codes_usa)
	elif state == "Utah":
		phone_first = random.choice(utah_codes_usa)
	elif state == "Vermont":
		phone_first = random.choice(verm_codes_usa)
	elif state == "Virginia":
		phone_first = random.choice(virg_codes_usa)
	elif state == "Washington":
		phone_first = random.choice(wash_codes_usa)
	elif state == "Washington, DC":
		phone_first = random.choice(wads_codes_usa)
	elif state == "West Virginia":
		phone_first = random.choice(wvir_codes_usa)
	elif state == "Wisconsin":
		phone_first = random.choice(wisc_codes_usa)
	elif state == "Wyoming":
		phone_first = random.choice(wyom_codes_usa)
	elif state == "Alberta":
		phone_first = random.choice(albe_codes_canada)
	elif state == "British Columbia":
		phone_first = random.choice(bcol_codes_canada)
	elif state == "Manitoba":
		phone_first = random.choice(mani_codes_canada)
	elif state == "New Brunswick":
		phone_first = random.choice(nbru_codes_canada)
	elif state == "Newfoundland and Labrador":
		phone_first = random.choice(nela_codes_canada)
	elif state == "Northwest Territories":
		phone_first = random.choice(note_codes_canada)
	elif state == "Nova Scotia":
		phone_first = random.choice(nosc_codes_canada)
	elif state == "Nunavut":
		phone_first = random.choice(nuna_codes_canada)
	elif state == "Ontario":
		phone_first = random.choice(onta_codes_canada)
	elif state == "Prince Edward Island":
		phone_first = random.choice(peis_codes_canada)
	elif state == "Quebec":
		phone_first = random.choice(queb_codes_canada)
	elif state == "Saskatchewan":
		phone_first = random.choice(sask_codes_canada)
	elif state == "Yukon":
		phone_first = random.choice(yuko_codes_canada)

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
creditcard()
if args.l:
	run_range = args.l
	# we start at 1 and 0 here because we already ran once above this
	for x in range(1, int(run_range)):
		generate_name()
		generate_dob()
		generate_country()
		generate_phonenum()
		creditcard()
		print "\r{0}%".format((float(x)/int(run_range))*100), 
