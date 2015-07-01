# read jason file

import json
import fileinput

fpath = '1'

with open(fpath) as f:
    for line in f:
        # load json to dictionary
        tw_dict = json.loads(line)
        print tw_dict 
        # read item
        usr_dict = tw_dict['user']
        print "usr:\n", usr_dict
        
