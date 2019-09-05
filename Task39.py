count=0
max=0
res=0;

for p in range(2,1000, 2):
    for a in range(1, p//3):
        b=p*(p-2*a)//(2*(p-a));
        c=p-a-b;
        if(a**2+b**2==c**2 and a+b+c==p):
            count+=1;
    if(count>max):
        max=count
        res=p
    count=0;
print(res);
input()
