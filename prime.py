from math import sqrt

n = int(input("请输入一个正整数："))
end = int(sqrt(n))
isPrime = True
for i in range(2, end+1):
    if (n % i == 0):
        isPrime = False
        break
print(isPrime)
