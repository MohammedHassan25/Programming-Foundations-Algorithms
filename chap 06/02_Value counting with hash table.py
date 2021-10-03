from typing import Counter


My_frist_letter_in_My_name = ['M', 'H', 'M', 'H', 'N']
Counter = dict()

for i in My_frist_letter_in_My_name:
    if i in Counter.keys():
        Counter[i] += 1
    else:
        Counter[i] = 1

print(Counter)