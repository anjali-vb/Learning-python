#print a new list which is the copy of the old list by aliasing and also change an element in the sublist of the old list which will be also reflecting in the new list


#Control copying =Assignment just creates a new object to the same object and creates an alias for the existing datastructure
old_list=[[1,2],[3,4],[5,"sky"]]
old_list=new_list         
new_list[2][1]=6           #changed the string element at the index 1 of the 3rd sublist
print("old_list is",old_list)
print("new_list is",new_list)
