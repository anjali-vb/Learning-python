#Suppose we want to make a new copy of the old list and also we have to mute the sublist of the old list and append a sublist to the old list but the changes cannot be reflect in the new list

import deep_copy
old_list=[[1,2],[3,4],[5,6]]
new_list=deepcopy.deep_copy(old_list)
old_list.append([7,8])
old_list[1][1]=9
print("old_list is :",old_list)
print("new_list is :",new_list)
