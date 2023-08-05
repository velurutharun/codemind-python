a=int(input())
b=list(map(int,input().split()))
l=[]
for i in b:
    l.append(i*i)
print(*sorted(l))
    