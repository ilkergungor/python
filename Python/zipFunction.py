
#! zip(*iterables) aggregate items from 1 or more list, set, tuple, dict.
#! creates zip paired items stored in tuple for each items

usernames = ["abcde", "qwerty", "abcxyz"]      #! list
passwords = ("12345", "12345678", "123456") #! tuple
date = ["23/07/2022", "01/09/2020", "08/03/2023"] #! list

users = zip(usernames, passwords)
print(type(users))      #!type is ZIP
print(users)
print("--------------------------------------")

users = list(users)
print(type(users))      #!type is LIST
for i in users:
      print(i)

print("--------------------------------------")

users = dict(users)
print(type(users))      #!type is DICTIONARY
for key, value in users.items():
      print(key + " : " + value)

print("--------------------------------------")

set_users = set(users)   #!type is SET
print(type(set_users))
print(set_users)

print("--------------------------------------")

tuple_users= tuple(set_users)   #!type is TUPLE
print(type(tuple_users))
print(tuple_users)

print("--------------------------------------")
   
users = zip(usernames, passwords, date)
print(type(users))  
for i in users:
      print(i)
      
      
      