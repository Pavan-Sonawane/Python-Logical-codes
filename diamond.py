for i in range(8):
    for j in range(-8,-i):
        print(" ", end='')
    for k in range(i+1):
        print("*", end=' ')
    print("")
for a in range(8):
    for b in range(a):
        print(" ", end='')
    for c in range(a,8):
        print("*", end=' ')
    print("")
