list = []
list0 = []
for i in range(5):
    num = int(input("enter the number"))

    if  num>0:
        list.append(num)
    elif num<0:
        list0.append(num)
    print("positive=" ,list,"negative=",list0)
