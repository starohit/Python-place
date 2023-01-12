# total int key in dict

d1 = {
    "a": "b",
    1: "ro",
    2: "se",
    "d": "dd",
    3: "gg"
}
i1 = [i for i in d1 if type(i) == int]
print(len(i1))
