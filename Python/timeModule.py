import time

print(time.ctime(0))
print(time.ctime(1000000)) #! TIME SINCE EPOCH (ABOVE)
print(time.time()) #! CURRENT SECOND SINCE EPOCH (ABOVE)
print(time.ctime(time.time()))

print("----------------------------------------------------")

local = time.localtime()
print(local)

string_format_time = time.strftime("%B %d %Y %H:%M:%S", local)
print(string_format_time)

gmt = time.gmtime() #!GMT
print(gmt)

print("----------------------------------------------------")

time_string = "23, April, 2023"
string_parse_time = time.strptime(time_string, "%d, %B, %Y")
print(string_parse_time)

time_tuple = (2023, 12, 28, 19, 5, 25, 5, 362, 3)
asc = time.asctime(time_tuple)
print(asc)

mk = time.mktime(time_tuple) #! SECONDS SINCE EPOCH
print(mk)




