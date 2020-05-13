

#coded by ss
# using sieve 
n=int(input())
c=0
prime=[True for i in range(n+1)]
p=2
while p*p<=n:
    if prime[p]:
        for j in range(p*p,n+1,p):
            prime[j]=False
        

    p+=1

print(prime)

for i in range(2,n+1):
    if prime[i] and i*i<n:c+=1




print(c)


   
