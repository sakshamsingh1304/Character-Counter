x=input('Enter your name')
print('---------------------------------------------------------------------------')
print('Hi',x,'.')
print('WELCOME TO PYTHON PROJECT')
print('---------------------------------------------------------------------------')
print('Topic: Character counter')
print('---------------------------------------------------------------------------')
input('Enter any key and press enter to continue')
print('---------------------------------------------------------------------------')

import re

a = input("Enter the string: ")
all_freq = {}

for i in a:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

order = r'[0 -9]'
FormattedString = re.sub(order, '', a)
print('---------------------------------------------------------------------------')
print("occurrence of each entry: ")
print(str(all_freq))
print('---------------------------------------------------------------------------')
print("length of the given string is: ")
print(len(a))
print('---------------------------------------------------------------------------')
print("string after removing digits(if any): ")
print(FormattedString)
print('---------------------------------------------------------------------------')

