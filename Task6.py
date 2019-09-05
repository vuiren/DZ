sumOfSquers=0;
squareOfSumOfNumbers=0;
for i in range(101):
    sumOfSquers+=i**2;
    squareOfSumOfNumbers+=i;
squareOfSumOfNumbers**=2;
print(squareOfSumOfNumbers-sumOfSquers);
input();