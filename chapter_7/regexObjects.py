import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
abbreviated = re.compile(r'\d{3}-\d{3}-\d{4}')

#searchs string for pattern
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

#you can also group using parentheses into a kind of list
random = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
ha = random.search('My number is 415-555-4242.')
print(ha.group(1))


#you can also use findall to find all occurences and put in a list
babyface = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(babyface.findall('Cell: 415-555-9999 Work: 212-555-0000'))

#there are character classes for simplicity
xmasRegex = re.compile(r'\d+\s\w+') #will match text that has one or more numeric digits (\d+), followed by a whitespace character (\s), followed by one or more letter/digit/underscore characters (\w+)
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
