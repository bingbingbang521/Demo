import random


target = random.randint(1, 10)
num = 1
while True:
    guessnum = int(input("请输入一个1~100之间的数字："))
    if(guessnum == target):
        print("Bingo!!! 你一共猜了{}次".format(num))
        break
    else:
        num += 1
        print("Sorry, Try again!")