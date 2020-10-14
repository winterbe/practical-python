# pcost.py
#
# Exercise 1.27
f = open("Data/portfolio.csv", "rt")
next(f)
result = 0.0
for line in f:
    row = line.split(",")
    share = int(row[1])
    price = float(row[2])
    result = result + (share * price)
print(result)
f.close()
