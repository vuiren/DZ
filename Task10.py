def IsPrime(x):
    if(x==1): return False
    if(x%2==0): return False
    for n in range(3,x,2):
        if(x % n == 0 and x!=n): return False;
    return True;

def main():
    counter=2 #Из-за двойки
    for i in range(3,2000000,2):
        if(IsPrime(i)):
            counter+=i;
    print(counter)
if __name__ == '__main__':
    main()