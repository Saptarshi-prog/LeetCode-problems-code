# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 20:04:48 2020

@author: Saptarshi
"""

num = int(input())

TENS = {30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}

ZERO_TO_TWENTY = (
    'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
    'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
    'Nineteen', 'Twenty'
)

def number_to_english(n):
    if any(not x.isdigit() for x in str(n)):
        return ''

    if n <= 20:
        return ZERO_TO_TWENTY[n]
    elif n < 100 and n % 10 == 0:
        return TENS[n]
    elif n < 100:
        return number_to_english(n - (n % 10)) + ' ' + number_to_english(n % 10)
    elif n < 1000 and n % 100 == 0:
        return number_to_english(int(n/100)) + ' Hundred'
    elif n < 1000:
        return number_to_english(int(n/100)) + ' Hundred ' + number_to_english(n % 100)
    elif n<1000000 and n>=1000 and n%1000==0:
        return number_to_english(int(n/1000)) + ' Thousand'
    elif n < 1000000:
        return number_to_english(int(n/1000)) + ' Thousand ' + number_to_english(n % 1000)
    elif n<1000000000 and n>=1000000 and n%1000000==0:
        return number_to_english(int(n/1000000)) + ' Million'
    elif n<1000000000 and n>=1000000:
        return number_to_english(int(n/1000000)) + ' Million ' + number_to_english(n%1000000)
    elif n<2**31-1 and n>=1000000000 and n%1000000000==0:
        return number_to_english(int(n/1000000000)) + ' Billion'
    elif n<=2**31-1 and n>=1000000000:
        return number_to_english(int(n/1000000000)) + ' Billion ' + number_to_english(n%1000000000)
    
    return ''



print(number_to_english(num))

