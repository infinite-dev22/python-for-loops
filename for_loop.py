# forr loops in python
#for loop is used to loop in a known range of values.
# python only has one kind of for loop
# but it can be implemented in various ways
# to shorten code.
# here, i will show two ways.

# 1st way
# this is the normal basic way.

# for loop can be ised to print items in an iterable like a list, set, etc.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in list:
	print(number)
	
# for loop can be used to add items to a list
list1 =[]
for item in range(11, 21):
	list1.append(item)
print(list1)

#2nd way
#we can use a for loop to print items in my_list like this.
my_list = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
print([i for i in my_list])

#we can add items to my_list1 with a for loop like this.
my_list1 = []
my_list1.append([item for item in range(31, 41)])
print(my_list1)

#or
my_list2 = [item for item in range(41, 51)]
print(my_list2)