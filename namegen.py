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
	alas_codes = [907]
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
	minn_codes = [218, 320, 507, 612, 651, 763, 952]
	miss_codes = [228, 601, 662, 769]
	misso_codes = [314, 417, 573, 636, 660, 816]
	mont_codes = [406]
	nebr_codes = [308, 402, 531]
	neva_codes = [702, 725, 775]
	nham_codes = [603]
	njer_codes = [201, 551, 609, 732, 848, 856, 862, 908, 973]
	nmex_codes = [505, 575]
	nyor_codes = [212, 315, 347, 516, 518, 585, 607, 631, 646, 716, 718, 845, 914, 917, 929]
	ncar_codes = [252, 336, 704, 828, 910, 919, 980, 984]
	ndak_codes = [701]
	ohio_codes = [216, 234, 330, 419, 440, 513, 567, 614, 740, 937]
	okla_codes = [405, 539, 580, 918]
	oreg_codes = [458, 503, 541, 971]
	penn_codes = [215, 267, 272, 412, 484, 570, 610, 717, 724, 814, 878]
	risl_codes = [401]
	scar_codes = [803, 843, 864]
	sdak_codes = [605]
	tenn_codes = [423, 615, 731, 865, 901, 931]
	texa_codes = [210, 214, 254, 281, 325, 346, 361, 409, 430, 432, 469, 512, 682, 713, 737, 806, 817, 830, 832, 903, 915, 936, 940, 956, 972, 979]
	utah_codes = [385, 435, 801]
	verm_codes = [802]
	virg_codes = [276, 434, 540, 571, 703, 757, 804]
	wash_codes = [206, 253, 360, 425, 509]
	wads_codes = [202]
	wvir_codes = [304, 681]
	wisc_codes = [262, 414, 534, 608, 715, 920]
	wyom_codes = [307]
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
	elif state == "Michigan":
		phone_first = random.choice(mich_codes)
	elif state == "Minnesota":
		phone_first = random.choice(minn_codes)
	elif state == "Mississippi":
		phone_first = random.choice(miss_codes)
	elif state == "Missouri":
		phone_first = random.choice(misso_codes)
	elif state == "Montana":
		phone_first = random.choice(mont_codes)
	elif state == "Nebraska":
		phone_first = random.choice(nebr_codes)
	elif state == "Nevada":
		phone_first = random.choice(neva_codes)
	elif state == "New Hampshire":
		phone_first = random.choice(nham_codes)
	elif state == "New Jersey":
		phone_first = random.choice(njer_codes)
	elif state == "New Mexico":
		phone_first = random.choice(nmex_codes)
	elif state == "New York":
		phone_first = random.choice(nyor_codes)
	elif state == "North Carolina":
		phone_first = random.choice(ncar_codes)
	elif state == "North Dakota":
		phone_first = random.choice(ndak_codes)
	elif state == "Ohio":
		phone_first = random.choice(ohio_codes)
	elif state == "Oklahoma":
		phone_first = random.choice(okla_codes)
	elif state == "Oregon":
		phone_first = random.choice(oreg_codes)
	elif state == "Pennsylvania":
		phone_first = random.choice(penn_codes)
	elif state == "Rhode Island":
		phone_first = random.choice(risl_codes)
	elif state == "South Carolina":
		phone_first = random.choice(scar_codes)
	elif state == "South Dakota":
		phone_first = random.choice(sdak_codes)
	elif state == "Tennessee":
		phone_first = random.choice(tenn_codes)
	elif state == "Texas":
		phone_first = random.choice(texa_codes)
	elif state == "Utah":
		phone_first = random.choice(utah_codes)
	elif state == "Vermont":
		phone_first = random.choice(verm_codes)
	elif state == "Virginia":
		phone_first = random.choice(virg_codes)
	elif state == "Washington":
		phone_first = random.choice(wash_codes)
	elif state == "Washington, DC":
		phone_first = random.choice(wads_codes)
	elif state == "West Virginia":
		phone_first = random.choice(wvir_codes)
	elif state == "Wisconsin":
		phone_first = random.choice(wisc_codes)
	elif state == "Wyoming":
		phone_first = random.choice(wyom_codes)

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
