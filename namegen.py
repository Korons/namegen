import random

import util.names

def generate_name():
    """ Generate a fake name """
    male_firstnames, female_firstnames, lastnames = util.names.load_all_names()
    first = random.choice(male_firstnames)
    last = random.choice(lastnames)

    print first, last

generate_name()

