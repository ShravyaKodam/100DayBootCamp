num = 3452
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))

'''
Concatenate two lists index-wise
Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
Given:

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
Expected output:

['My', 'name', 'is', 'Kelly']

'''
#Zip function(take 2 list values)

