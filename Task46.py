import  math
def IsSimple(x):
    if(x==1): return True
    if(x%2==0): return False
    for n in range(3,x,2):
        if(x % n == 0 and x!=n): return False;
    return True;

def FindPrevSimpleOdd(x):
    res=x-2
    while(not IsSimple(res)):
        res-=2;
    return res

def FindNextNotSimpleOdd(x):
    res=x
    while(IsSimple(res) or x==res):
        res+=2;
    return res

def CanBeTransformedIntoSum(x):
    simplePart=FindPrevSimpleOdd(x)
    while(simplePart>=1):
        if(math.sqrt((x-simplePart)//2) % 1 == 0): return True;
        simplePart=FindPrevSimpleOdd(simplePart)
    return ;

def main():
    res=FindNextNotSimpleOdd(3);
    while(CanBeTransformedIntoSum(res)):
        res=FindNextNotSimpleOdd(res)
    print(res)
    input()

if( __name__ == '__main__'):
    main();