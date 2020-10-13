# mortgage.py
#
# Exercise 1.7

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    month = month + 1
    if extra_payment_start_month <= month <= extra_payment_end_month:
        monthly_extra = extra_payment
    else:
        monthly_extra = 0

    principal = principal * (1 + rate / 12) - payment - monthly_extra
    total_paid = total_paid + payment + monthly_extra
    if principal < 0:
        total_paid = total_paid - abs(principal)
        principal = 0

    print(month, round(total_paid, 2), round(principal, 2))

total_paid_formatted = '{:,}'.format(round(total_paid, 2))

print('Total paid', total_paid_formatted, 'over', month, 'months')
