"""
Name: Mr. Smith
Date: 1-8-25
Description: List methods
"""

my_list = [1,2,3,1,2]

# count number of elements that meet criteria
num_of_twos = my_list.count(2)
print(num_of_twos)

# add (append) item to list
my_list.append(4)
print(my_list)

my_list.append([5,6]) #this adds a list to your list
print(my_list)


my_list.pop() # removes last item from list (undo)

# how to I add both 5 and 6, not in a list?
my_list.extend([5,6])
print(my_list)

# sorting lists
my_list.sort() # modifies the list
print(my_list)

# can I store the sorted list in another variable?
new_list = [4,6,4,2,9,0,-5]
sorted_list = sorted(new_list)
print(sorted_list)
print(new_list) # it has not changed

random_words = ["galaxy", "apple", "forest",
                "dolphin", "breeze",
                "gallon","canyon", "ember"]

print(sorted(random_words)) # prints the sorted list, but list unchange
print(random_words.sort()) # COMMON MISTAKE - .sort returns None not the list
print(random_words)

# remove first occurrence of an item
random_nums = [3,6,4,2,3,3,5,4]
random_nums.remove(4)
print(random_nums)

# remove item at specified index
# list is [3,6,2,3,3,5,4]
random_nums.pop(4)
print(random_nums)

# pop without an argument removes the last item
random_nums.pop()
print(random_nums)

# insert item a specific location
random_nums.insert(1,4)
print(random_nums)