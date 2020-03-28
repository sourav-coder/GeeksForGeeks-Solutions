

#coded by ss

def main(n,arr):
    i = 0
    while i < n:
        temp = arr[i]
        count =0
        for j in arr[i:]:
            if j < temp:
                count +=1
        i+=1
        yield count


T = int(input())
for i in range(T):
    
    n = int(input())
    arr= list(map(int,input().split()))
    print(" ".join(str(i) for i in main(n,arr)))
