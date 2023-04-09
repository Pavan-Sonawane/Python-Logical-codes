i=1
j=9
for row in range(10):
    for col in range(10):
        if row==0 or row==9:
            print("*",end="")
        elif row==i and col==j:
            print("*",end="")
            i=i+1
            j=j-1
        else:
            print(end=" ")
    print()