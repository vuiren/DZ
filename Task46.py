import  math

def IsPrime(x):
    if(x<0): return False
    if(x<=3): return x>1;
    if(x%2==0 or x%3==0): return False;
    i=5;
    while(i*i<=x):
        if(x % i==0 or x % (i+2)==0): return False;
        i+=6;
    return True;

def FindPrevSimpleOdd(x):
    res=x-2
    while(not IsPrime(res) and res>0):
        res-=2;
    return res

def FindNextNotSimpleOdd(x):
    res=x
    while(IsPrime(res) or x==res):
        res+=2;
    return res

def CanBeTransformedIntoSum(x):
    simplePart=FindPrevSimpleOdd(x)
    while(simplePart>=1):
        if(math.sqrt((x-simplePart)//2) % 1 == 0): return True;
        simplePart=FindPrevSimpleOdd(simplePart)
    return False;

def main():
    res=FindNextNotSimpleOdd(3);
    while(CanBeTransformedIntoSum(res)):
        res=FindNextNotSimpleOdd(res);
    print(res)

if( __name__ == '__main__'):
    main();
