n = [1,2,5,10,3,100,9,24]
for e in n:
    if e < 5:
        n.remove(e)

print(n)

#fix bug
print("\nFixing bug...\nRemoved numbers less than 5:")
for e in n[:]:
    if e < 5:
        n.remove(e)

print(n)
