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

import random
import string
import time

VERSION = "Password Generator version 1.1"

def randword(lines=1, linelength=10, key=None):
    """
    lines - How many password are to be generated
    linelength=10 is the default length of the generated password
    key - key type that is used. Alpha, alpha numeric, numeric, alpha numeric special"
    """
    random.seed(time.time())
    alphabet=""
    password_list=[]

    if key==0:
        alphabet += string.letters + string.digits
    elif key==1:
        alphabet += string.letters
    elif key==2:
        alphabet += string.digits
    elif key==3 or key==None:
        alphabet += string.letters + string.digits + string.punctuation
    else:
        print "Unrecognized key"
        return False
    
    count=0
    word = ""
    
    while True:
        if len(word) >= linelength:
            password_list.append(word)
            word = ""
            count += 1
            if count >= lines:
                return password_list
          
        word += alphabet[int(100*random.random())%len(alphabet)]
        
        
if __name__ == "__main__":
    pass_list=randword(5, 25)
    for x in pass_list:
        print x
