def IsSimple(x):
    if(x==1): return True
    if(x%2==0): return False
    for n in range(3,x,2):
        if(x % n == 0 and x!=n): return False;
    return True;

def ShuffleForward(x):
    res=x[len(x)-1]
    for i in range(0,len(x)-1):
        res+=x[i] #[1,2,3,4]  [4,1,2,3]
    return res

def IsRoundSimple(x):
    stringRepresentation=str(x)
    for i in range(0, len(stringRepresentation)):
        if(not IsSimple(int(stringRepresentation))): return False;
        stringRepresentation=ShuffleForward(stringRepresentation)
    return True

def main():
    counter=1 #Из-за двойки
    for i in range(3,1000000, 2):
        if(IsRoundSimple(i)):
            counter+=1;
    print(counter)


if __name__ == '__main__':
    main();