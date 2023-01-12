# sum of items in dict

mydict = {'A': 71.07884,
          'B': 110,
          'C': 103.14484,
          'D': 115.08864,
          'E': 129.11552,
          'F': 147.1766,
          }

print(sum(value for key, value in mydict.items()))