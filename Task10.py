def IsPrime(x):
    if(x<=3): return x>1;
    if(x%2==0 or x%3==0): return False;
    i=5;
    while(i*i<=x):
        if(x % i==0 or x % (i+2)==0): return False;
        i+=6;
    return True;

def main():
    counter=2 #Из-за двойки
    for i in range(3,2000000,2):
        if(IsPrime(i)):
            counter+=i;
    print(counter)
if __name__ == '__main__':
    main()
