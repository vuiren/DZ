def IsPalindrom(x):
    stringInterpretation=str(x);
    reversedString=stringInterpretation[::-1];
    return reversedString==stringInterpretation;

def FindLargestPalindrom():
    res = 0;
    for n1 in range(100, 999):
        for n2 in range(100, 999):
            if (IsPalindrom(n1 * n2) and n1*n2 > res):
                res=n1*n2;
    return res;

def main():
    print(FindLargestPalindrom())

if __name__ == '__main__':
    main()

