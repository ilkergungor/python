
#! creates dictionaries using expressions
#! replaces loops and lambda functions

f_degrees = {"NY": 59, "LA":67, "AK":32, "TX":82, "MN":50}
print(f_degrees)
print("-----------------------------------------------------------")

c_degrees = {key.lower(): round((value-32)*(5/9)) for (key, value) in f_degrees.items()}
print(c_degrees)
print("-----------------------------------------------------------")

condition =  {"NY": "cloudy", "LA":"sunny", "AK":"snowy", "TX":"sunny", "MN":"rainy"}
sunny_weather = {key:value for (key, value) in condition.items() if value == "sunny"}
print(sunny_weather)
print("-----------------------------------------------------------")

description_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in f_degrees.items()}
print(description_cities)
print("-----------------------------------------------------------")

def check_temp(value):
      if value >= 70:
            return "HOT"
      elif 69 >=  value >= 40:
            return "WARM"
      else:
            return "COLD"

desc_cities = {key: check_temp(value) for (key, value) in f_degrees.items()}

print(desc_cities)



