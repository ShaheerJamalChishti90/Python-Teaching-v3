a = ["Mimi", "Indonesia", "Guy", 12, 6.0, 130, True]

# print(a[0], a[1], a[6]) #Accessing the items of the list

#Changing the list Items
# a[3] = 60

#Adding items to the list
# a.append("Palembang") #It is use to add any element to the end of the list
# a.insert(1, "Palembang")  #It is use to add any element to the specific index of the list
# print(a)

#Delete list items
# 3 Different ways

# a.remove(12)

# a.pop(2)

del a[0]
print(a)


#Sorting the list
thislist = [10, 5, 6, 2, 8]

thislist.sort(reverse= True)

print(thislist)
