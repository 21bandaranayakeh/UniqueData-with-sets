set1 = {0}

a = 0

while True:
    a = input('Please enter some data.')
    if a == '-1':
        break
    b = len(set1)
    set1.add(a)
    if len(set1) == b:
        set1.remove(a)



print(set1)
print(len(set1) - 1)
