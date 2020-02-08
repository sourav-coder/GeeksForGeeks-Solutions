
#coded by ss

for _ in range(int(input())):
  n=int(input())
  a=list(map(int,input().strip().split()))
  from collections import  Counter
  ar=Counter(a)
  for i in a:
    if ar[i]==1:
      print(i)
      break

  else:print(0)
