
#List is created with square brackets, 
#items in the list are separated by commas
#List can hold multiple types of data - string, integer, 
#list in python are mutable that means items in it can be removed or new items added
#List can have duplicate elements
mylist = ["fruit", 1, 55.6, True, "fruit"]

#you can print the entire list 
print(mylist)

#List can be empty
emptylist = list()  #or you can just do []
print(emptylist)

#In python, each item in the list is indexed, index starts from Zero
#In mylist above, "Fruit" is at index 0
#lets print the item at index 0 index
print(mylist[0])
#lets print item at index 1
print(mylist[1])

#you can check the size of the list which indicates how many items are there in the list
print(len(mylist))

#you can add additional item to the list 
mylist.append("car")
mylist.append(2)
mylist.append(False)
print(mylist)

#We can add the item at certain position.
#here we insert item at index 0 
mylist.insert(0, "phone")
print(mylist)

#you can remove item from the list
mylist.remove('fruit')
print(mylist)

#another way to remove item is to use pop method
#pop removes the last item
mylist.pop()
print(mylist)


#you can clear the list using clear method
mylist.clear()
print(mylist)



#lets create another list

newlist = [-1, 0,1,2,3,4,5,6,7,8,9]
print(newlist)

#you can sort the list
newlist.sort()
print(newlist)

#take a note that it changes existing list. 
#if you want to keep your original list the same and create new one 
#with sorted order then you can use sorted method

sorted_list = sorted(newlist)
print(newlist)
print(sorted_list)
#you can reverse the order of the list
#you can reverse using reverse method
newlist.reverse()
print(newlist)

#you can loop through the 


