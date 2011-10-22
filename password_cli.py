#!/usr/bin/env python

# Copyright (C) 2008  Peter Gill
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import getopt
import password_rand

        
if __name__ == "__main__":
    # if console application output
    """
    "Password Generator"  Copyright (C) 2008 Peter Gill
    This program comes with ABSOLUTELY NO WARRANTY; for details type `password_gen.py w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `password_gen.py c' for details.
    """
    help_msg="""
    -l password length
    -q password quantity
    -k key type: 0-alpha, 1-alphanumeric, 2 numeric, 3-alphanumeric/special.
       Defaults to 3
    -d default 5 quanity, 10 length
    -v version
    -h - Display Help
    """
    length=10
    quantity=5
    key=3
    help=False
    version=False
    default=False
    
    # colon after the letter means option has an argument
    opts, args = getopt.getopt(sys.argv[1:], "l:q:k:dvh", ["length", 
        "quantity", "key", "default", "version", "help"]) 

    #print "opts: ", opts
    #print "args: ", args
    for o, v in opts:
        if o in ("-l"):
            length=int(v)
        elif o in ("-q"):
            quantity=int(v)
        elif o in ("-k"):
            key=int(v)
        elif o in ("-d"):
            default=True
        elif o in ("-v"):
            version=True
        elif o in ("-h"):
            help=True

            
    if version:
        print password_rand.VERSION
        sys.exit()
        
    if help or len(opts)==0:
        print help_msg
        sys.exit()

    pass_list = password_rand.randword(quantity, length, key)
    for x in pass_list:
        print x
        

