name = "Sponge Bob"


first_name = name[0:6] #! FIRST SIX LETTERS
print(first_name)

last_name = name[7:]
print(last_name)

new_name = name[0:10:2] #!EVERY 2ND LETTERS
print(new_name)

different_name = name[::2] #!EMPTY PARAM MEANS 0
print(different_name)

reversed_name = name[::-1] #! -1 MEANS COUNTING BACKWARDS
print(reversed_name)

website = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)

print(website[slice])
print(website2[slice])

