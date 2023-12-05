num=int(input("enter a num:"))
i=1
j=num
while i<=num:
    print(j*" "+ "* "*i)
    i+=1
    j-=1
i=1
j=num
while i<=num:
    print(i*" "+ "* "*j)
    i+=1
    i-=1