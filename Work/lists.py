# lists.py
# Exercise 1.2x

mylist = ["a", "b", "c"]
if "x" not in mylist:
    print("Yo")

mylist.append("bla")
mylist.sort(reverse=True)

print(",".join(mylist))

nums = [101, 102, 103]
items = ["spam", mylist, nums]
print(items)
print(items[1][-1])
print(items[0][-1])
