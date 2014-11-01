import os.path
import subprocess
import sys

import prob_util

CODEBASE_DIR = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).strip('\n')

MALE_NAME_FILE = os.path.join(CODEBASE_DIR, 'data', 'male-first.txt')
FEMALE_NAME_FILE = os.path.join(CODEBASE_DIR, 'data', 'female-first.txt')
LASTNAME_FILE = os.path.join(CODEBASE_DIR, 'data', 'lastnames.txt')

def load_name_data(fpath):
    """ Loads name data as list of names paired with frequency """

    with open(fpath, 'r') as fp:
        data = [x.split(' ') for x in fp.read().split('\n') if len(x) > 0]
    stat_data = [(x[0], float(x[1])) for x in data]
    total = [freq for _, freq in stat_data]
    scale = 100.0 / sum(total)
    stat_data = [(name, scale * freq / 100.0) for name, freq in stat_data]
    assert abs(1.0 - sum([freq for _,freq in stat_data])) < 1e-6, "Frequencies should sum to 1.0"
    return stat_data

def load_all_names():
    files = [MALE_NAME_FILE, FEMALE_NAME_FILE, LASTNAME_FILE]
    lists = [ ]
    for file in files:
        lists.append(load_name_data(file))

    male_freq_list = prob_util.freq_list_from_tuple_list(lists[0])
    female_freq_list = prob_util.freq_list_from_tuple_list(lists[1])
    last_freq_list = prob_util.freq_list_from_tuple_list(lists[2])

    return male_freq_list, female_freq_list, last_freq_list

"""
if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2] if len(sys.argv) > 2 else sys.argv[1]

    with open(infile, "r") as inf:
        raw = inf.read()

    raw = raw.split('\n')
    freq_names = []
    for line in raw:
        if len(line) < 1:
            continue
        line = [l for l in line.split(' ') if len(l) > 0]
        freq_names.append( (line[0], line[1]) )

    with open(outfile, "w+") as outf:
        for name, freq in freq_names:
            outf.write(name + ' ' + freq + '\n')
"""
