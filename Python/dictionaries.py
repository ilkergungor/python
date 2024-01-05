
# ! CHANGEABLE, UNORDERED COLLECTION OF UNIQUE KEY:VALUE PAIRS
#! FAST CUZ USES HASHING, QUICK ACCESS

capitals =  {'USA': 'Washington DC',
                  'India' : 'New Delhi',
                  'China': 'Beijing',
                  'Russia' :'Moscow'
                  }

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})

print(capitals['Russia'])
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
      print(key, value)
      
capitals.pop('China')
print(capitals)

capitals.clear()
print(capitals)


