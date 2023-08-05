a=int(input())
b=list(map(int,input().split()))
l=[]
for i in b:
    if b.count(i)>len(b)/2:
        l.append(i)
print(*list(set(l)))