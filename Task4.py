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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def getTextNumbers():
    telephone_numbers =set()
    for text in texts:
        telephone_numbers.add(text[0])
        telephone_numbers.add(text[1])
    return telephone_numbers

def getReceivedNumber():
    telephone_numbers =set()
    for call in calls:
        telephone_numbers.add(call[1])
    return telephone_numbers


telemarketers= set()
textNumber=getTextNumbers()
receivedNumber=getReceivedNumber()
for call in calls:
    if call[0] not in textNumber and call[0] not in receivedNumber:
        telemarketers.add(call[0])
    
sortedList= sorted(telemarketers)

print("These numbers could be telemarketers: ")
for num in sortedList:
    print(num)