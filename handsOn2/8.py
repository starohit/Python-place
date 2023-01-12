sentence = input(" enter a sentence ")

l1 = sentence.split()
length = len(l1) // 2

if length % 2 == 0:
    print(l1[length - 1], l1[length])
else:
    print(l1[length])
