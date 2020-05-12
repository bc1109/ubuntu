import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumberRegex.search('My number is 813-442-2837')