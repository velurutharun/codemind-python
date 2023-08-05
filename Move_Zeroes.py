a=int(input())
b=list(map(int,input().split()))
l=[]
ll=[]
for i in b:
    if i==0:
        l.append(i)
    else:
        ll.append(i)
print(*ll+l)
