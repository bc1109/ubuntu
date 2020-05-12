#! /usr/bin/python3

import re, pyperclip


#regex for phone numbers

phoneRegex = re.compile(r''' 
# 415-555-0000, 550-0000, (415) 555-0000 ext 12345, ext. 12345, x12345
 (
 ((\d\d\d) | (\(\d\d\d\)))?   # area code (optional)
 (\s|-)                       # first separator
 \d\d\d                       # first 3 digits
 -                            # separator
 \d\d\d\d                     # last 4 digits
 (((ext(\.)?\s) |x)            # extension  word-part (optional)
 (\d{2,5}))?
 )                             # extension number-part (optional)
''', re.VERBOSE)

#2 egex for email addresses

emailRegex = re.compile(r'''
# some.T_thing@something.com

[a-zA-Z0-9.+]+              #name part
@                           # @ symbol
[a-zA-Z0-9.+]+              #domain name part

''', re.VERBOSE)

#3 get the text off the clipboard
text = pyperclip.paste()

#4 extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


#5 copy the extracted email/phone to the clipboard

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)


