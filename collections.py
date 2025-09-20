# lists
# fruits = ["apple","banana","mango","cherry"]
# print(fruits)   #print list
# print(type(fruits))   #type of fruits
# print(len(fruits))   #length of fruit
# print(fruits[2])   #fruit at 2nd index



#check if an item is not available in list or not
# fruits = ["apple","banana","mango","cherry"]
# if "banana" in fruits:
#     print ("banana is part of list")
# if "kiwi" in fruits:
#     print ("kiwi is part of list")
# else:
#     print ("kiwi is not part of list")


#add element in list
# fruits.append("kiwi")
# print(fruits)


#remove element from list
# fruits.remove("apple")
# print(fruits)


#insert element in list
# fruits.insert(2,"orange")
# print(fruits)


#extend list
# morefruits = ["papaya","grapes","watermelon"]
# fruits.extend(morefruits)
# print(fruits)


#remove element from list
fruits = ["apple", "banana", "mango", "banana"]
# fruits.remove("banana") 
# print(fruits)

# fruits.pop(2)
# print(fruits)

# fruits.pop()
# print(fruits)


# fruits = ["apple", "banana", "mango", "orange"]
# fruits[1] = "grapes"          # Change item at index 1
# print(fruits)



# fruits = ["apple", "banana", "mango", "orange", "kiwi"]
# print(fruits)
# fruits[1:4] = ["grapes", "pineapple", "papaya"]                  # Change items from index 1 to 3 (banana, mango, orange)
# print(fruits)



# fruits = ["apple", "banana", "mango", "orange", "kiwi"]
# print(fruits)
# fruits[1:4] = ["grapes", "pineapple", "papaya","dragonfruit","pomegrante"]                  
# print(fruits)



# Sorting a list
# list = [1,2,4,5,3,7,4,8]
# list.sort()
# print(list)


# list = [1,2,4,5,3,7,4,8]
# list.sort(reverse=True)
# print(list)


# fruits = ["apple", "banana", "mango", "orange", "kiwi"]
# fruits.sort()
# print(fruits)
# fruits.sort(reverse=True)
# print(fruits)



# reverse the list
# fruits = ["apple", "banana", "mango", "orange", "kiwi"]
# fruits.reverse()
# print(fruits)



# list comprehension
# list = [10,12,11,54,53,62,45,43]
# new_list = [i for i in list if i > 25]
# print(new_list)


# fruits = ["apple", "banana", "mango", "orange", "kiwi"]
# new_fruits = [fruit for fruit in fruits if "a" in fruit]
# print(new_fruits)


# copy a list
# fruits = ["apple", "banana", "mango", "orange", "kiwi"]
# new_fruits = fruits.copy()
# print(new_fruits)




# tuple
# colors = ("red","yellow","green")
# print(colors)
# print(type(colors))
# print(len(colors))


# color = ("red",)
# print(color)
# print(type(color))



# accesing item at tuple
# colors = ("red","yellow","green")
# print(colors[1])


# check if an item exist in tuple
# colors = ("red","yellow","green")
# if "green" in colors:
#     print("green is part of tuple")

# unpacking a tuple
# colors = ("red","yellow","green")
# color1,color2,color3 = colors
# print(color1,color2,color3)

# reverse
# num = (1,2,3,4,5,6,7)

# list = []

# for x in reversed(num):
#     list.append(x)

# result = tuple(list)
# print(result)





# Sets
# names = {"jasim","aman","pawan","avinash"}
# print(names)
# print(len(names))
# print(type(names))


# accessing items of set
# names = {"jasim","aman","pawan","avinash"}
# for x in names:
#     print(x)


# check if an item is exist in a set
# names = {"jasim","aman","pawan","avinash"}
# if "aman" in names:
#     print("aman is in set")


# add element
# names = {"jasim","aman","pawan","avinash"}
# names.add("Nia")
# print(names)


# add sequence
# names = {"jasim","aman","pawan","avinash"}
# names_list = {"nia","ria","dia"}
# names.update(names_list)
# print(names)


# remove element
# names = {"jasim","aman","pawan","avinash"}
# names.remove("pawan")
# print(names)


# names = {"jasim","aman","pawan","avinash"}
# names.discard("ria")   #this will not throw error if value is not present in set 
# print(names)


# s1 = {1,2,3}
# s2 = {3,4,5,6}
# s3 = s1.union(s2)
# print(s3)


# s1 = {1,2,3}
# s2 = {3,4,5,6}
# s3 = s1.intersection(s2)
# print(s3)








# Dictionary
# phone_number = {
#     "john":897457,
#     "ria":785956,
#     "joy":754864
# }
# print(phone_number)
# print(type(phone_number))
# print(len(phone_number))


# phone_number = {
#     "john":897457,
#     "ria":785956,
#     "joy":754864
# }
# print(phone_number["john"])
# print(phone_number.keys())

# phone_number["john"] = 7847854865
# print(phone_number)
# phone_number["kia"] = 458542
# print(phone_number)



# phone_number = {
#     "john":897457,
#     "ria":785956,
#     "joy":754864
# }
# phone_number.clear()    #this is empty the dictionary
# print(phone_number)



# phone_number = {
#     "john":897457,
#     "ria":785956,
#     "joy":754864
# }
# for x in phone_number:
#     print(phone_number[x])



# phone_number = {
#     "john":897457,
#     "ria":785956,
#     "joy":754864
# }
# for x,y in phone_number.items():
#     print(x,y)



# phones = {
#     "number1":{
#         "joy":78,
#         "john":79,
#         "jay":80
#     },
#     "number2":{
#         "nia":81,
#         "ria":82,
#         "dia":83
#     }
# }
# print(phones["number1"]["jay"])


