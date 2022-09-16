"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

telephone_numbers ={}

number=''
durations=0

for call in calls:
    duration= int(call[3])
    if call[0] in telephone_numbers:
        telephone_numbers[call[0]]=telephone_numbers[call[0]]+duration
    else:
        telephone_numbers[call[0]]=duration

    if telephone_numbers[call[0]] > durations:
        durations= telephone_numbers[call[0]]
        number=call[0]

    if call[1] in telephone_numbers:
        telephone_numbers[call[1]]=telephone_numbers[call[1]]+duration
    else:
        telephone_numbers[call[1]]=duration
    
    if telephone_numbers[call[1]] > durations:
        durations= telephone_numbers[call[1]]
        number=call[1]

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(number,durations))