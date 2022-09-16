"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def getPrefix(phone_number):
  first_char = phone_number[0:1]
  if first_char == "(":
    return phone_number[1:phone_number.index(")")]
  if first_char in ("7","8","9"):
    return phone_number[0:4]
  raise Exception('Invalid')


def partA():
  numbers = set()
  for call in calls :
    sendingNumber= call[0]
    if sendingNumber[0:5]=="(080)":
      numbers.add(getPrefix(call[1]))
  
  sorted_list= sorted(numbers)

  print("The numbers called by people in Bangalore have codes:")
  for number in sorted_list:
    print(number)

def partB():
  total =0
  samesame=0

  for call in calls:
    sendingNumber= call[0]
    receivingNumber = call[1]
    if sendingNumber[0:5]=="(080)":
      if receivingNumber[0:5]=="(080)":
        samesame+=1
      total +=1
  
  print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format((samesame/total)*100))


partA()
partB()