

if(len(pn) != 12):
    return False
if(pn[3] != '-' or pn[7] != '-'):
    return False

for i in range(0,3):
    if(not pn[i].isdigit()):

for i in range(4,7):
    if(not pn[i].isdigit()):
        return False

for i in range(8,12):
    if(not pn[i].isdigit()):
        return False
    
return True

import re

phoneNumberRegex = re.compile(r'^\d{3}-\d{3}-\d{4}')
mo_phoneNumber = phoneNumberRegex.search('My number is 415-555-4242.')
print(mo_phoneNumber.group())
mo_phone_string = phoneNumberRegex.search('My number is 415-555-4242.')
print(mo_phone_string.group())

phoneNumberRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo_phoneNumber = phoneNumberRegex.search('My number is 415-555-4242.')
print(mo_phoneNumber.group(0))
print(mo_phoneNumber.group(1))
print(mo_phoneNumber.group(2))

#Using the method groups() we get a tuple, and we can use tuple unpacking
print(mo_capture_pn.groups())
area_code, phone_number = mo_capture_pn.groups()
print(area_code)
print(phone_number)

# The preceding capture group is optional 
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
mo2 = batRegex.search('The adventures of Batwoman')
print(mo1)
print(mo2)

# matches on zero or more instances
batREgex = re.compile(r'Bat(wo)*man')
mo1 = batREgex.search('The adventures of Batman')
mo2 = batREgex.search('The adventures of Batwoman')
mo3 = batREgex.search('The adventures of Batwowowoman')
print(mo1)
print(mo2)
print(mo3)

batREgex = re.compile(r'Bat(wo)+man') # This will not accept 'Batman' 

#Character Classes:
# /d - any numeric digit from 0 to 9
# /D - any char not from 0 to 9
# /w - any letter, numeric digit, or underscore 
# /s - any space, tab, or newline
# [a-z] - any lowercase character
# [A-Z] - any uppercase character
# [a-zA-Z] - both upper and lower
# [0-5] - any number between 0 and 5 inclusive

# <(.*)> - will greedily match anything between two angle brackets
# <(.*?)> - will match anything between two angle brackets in a non greedily way 

# Exercise

regex = "\d+\s\w+"

this_Regex = re.compile(r'\d+\s\w+')
mo = this_regex.earch("67 b")
mo2 = this_Regex.search("67ten")

print(mo)
print(mo2)

# Exercise
# Write a regular expresion to validate a basic E-mail address
# Format: at least one alphanumber  character, followed by an '@', then a period and then three letters

email_regex = "\w+@[a-zA-Z]+.w{3}"

# Using a period by itself will match on any character. To match the period you have to use an excape character
email = re.compile(r'\w+@[a-zA-Z]+.w{3}')
mo = email.search("jjackson@moobly.com")
mo1 = email.search("jjackson@mooblyX.com")

print(mo)
print(mo1)

