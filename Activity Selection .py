#code
# # # cook your dish here



for _ in range(int(input())):
   input()
   a=list(map(int,input().split()))
   b=list(map(int,input().split()))
   c=[]
   for i in range(len(a)):
      c.append((a[i],b[i]))
   c.sort(key=lambda x:x[1])
   # print(c)

   a=[]
   b=[]

   for i in c:
      a.append(i[0])
      b.append(i[1])
   # print(a,b)

   d=1

   i=1
   j=0
   while i<len(a):
      if a[i]>=b[j]:
         d+=1

         j=i
      i+=1

   print(d)








