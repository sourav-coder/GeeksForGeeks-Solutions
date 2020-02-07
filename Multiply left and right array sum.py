




#coded by sourav sarkar


for _ in range(int(input())):
      n=int(input())
      a=list(map(int,input().split()))
      print(sum(a[:len(a)//2])*sum(a[len(a)//2:]))
