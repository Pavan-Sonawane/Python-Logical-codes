num=int(input("enter number"))
a=0
b=1
c=0
if num<0:
   print("Enter correct number")
else:
      for i in range(0,num):
         print(c ,end=",")
         a=b
         b=c
         c=a+b

