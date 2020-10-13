# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    month = month + 1
    extra = 1000
    if month > 12:
        extra = 0
    principal = principal * (1 + rate / 12) - payment - extra
    total_paid = total_paid + payment + extra

total_paid_rounded = round(total_paid * 100) / 100
total_paid_formatted = '{:,}'.format(total_paid_rounded)

print('Total paid', total_paid_formatted, 'over', month, 'months')
