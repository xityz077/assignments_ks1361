# Create a list with the values [1,2,3,4,5]
list1 = [1, 2, 3, 4, 5]
# print(f"list1 = {list1}\n")

# Create a new list thta repeats those values 27 times
list2 = list1 * 27
# print(f"\nlist2 = {list2}\n")

# create new list with first 100 items
list3 = list2[:100]
# print(f"\nlist3 = {list3}\n")

# Print the last item in the list of 100 items
print(f"\nThe last item in the list of 100 items is {list3[-1]}\n")

# Print the number of times 3 appears in the list of 100 items
count_of_3 = list3.count(3)
print(f"\nThe number 3 appears, {count_of_3} times in the list\n")
