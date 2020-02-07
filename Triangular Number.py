


# mathematical(0.25s)

#coded by ss


#code
a=[1,3,6,10,15]
c=len(a)
while(1):
  c+=1
  if c==100000+2:break
  d=(a[len(a)-1]-a[len(a)-2])+1+a[len(a)-1]
  a.append(d)






for _ in range(int(input())):
  n=int(input())
  if n in a:print(1)
  else:print(0)
