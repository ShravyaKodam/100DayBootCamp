name="Shravya Kodam"
n=0
for char in name:
    num=name.count(char)
    if num>n:
        n=n+num
        print(char, num)

    name="SShrrravya kkkodarrm"
    n=1
    for char in name:
        num=name.count(char)
        if num>n:
            n=n+num
            print(char, num)

name="Shravya kodam"
n=0
i=0
for char in name:
    i = i + 1
    num=name.count(char)
    if num>n:
        n=n+num
    if i == len(name)-1:
            print(char, num)


result=max(10,20)
print(result)
string= "mississippis"
print(string)

char_freq={}

for i in string:
    if i in char_freq:
        char_freq[i]=char_freq[i]+1
    else:
        char_freq[i] = 1
result= max(char_freq, key = char_freq.get)

print("Most frequent character: ",result)
'''
'''
# Python 3 code to demonstrate
# Maximum frequency character in String
# naive method
'''
# initializing string
test_str = "GeeksforGeeks"

# printing original string
print ("The original string is : " + test_str)

# using naive method to get
# Maximum frequency character in String
all_freq = {}
for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1
res = max(all_freq, key = all_freq.get)

# printing result
print ("The maximum of all characters in GeeksforGeeks is : " + str(res))
'''
'''
import os
os.system('CLS')
'''