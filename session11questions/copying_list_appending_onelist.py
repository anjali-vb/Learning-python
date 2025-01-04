#create a newlist from the old list and print the old list and the newlist but the old list nedds to be one sublist to be added in It so on the time of printing the two lists the changes in the olf list should not be affected int he new list
import copy     #we have to define the shallow copy or It will be resulting in a name error
old_list=[[1,2],[3,4],[5,6]]
new_list=copy.copy(old_list)    # shallow copy creates a new datastructure but the elements are not actually be shared
old_list.append([7,8])
print("the new_list is",new_list)
print("the old_list is",old_list)

