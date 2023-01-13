# show details of state (CM Name, Capital, Population) using a dictionary.

import sys

d1 = {
    "jharkhand": {
        'CM Name': "abc",
        'Capital': "Ranchi",
        'Population': 10000
    },
    "Bihar": {
        'CM Name': "xyz",
        'Capital': "Patna",
        'Population': 18000
    },
    "West Bengal": {
        'CM Name': "abc",
        'Capital': "Ranchi",
        'Population': 10000
    }
}

s_name = sys.argv[1]

if s_name in d1:
    print(d1[s_name])
else:
    print("no details")