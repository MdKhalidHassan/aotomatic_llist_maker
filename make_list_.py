
def makeautolist(m,n)
    m=input("Give your list name:")
    n=int(input("How many element keep your list?:"))

    o=str(m)
    m=[]
    j=1
    while j<=n:
       j=j+1
       y= input(":")
       m.append(y)
       #print(m)
       #print(len(m))
    print(o,"=",m)
    print("Final lenth of:",o,len(m))


   print(" Elements are:")
   for i in m:
      print(i)


