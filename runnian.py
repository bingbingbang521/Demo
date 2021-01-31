n = int(input("Please input the year:"))
if (n%4 == 0) | (n%100 == 0) & (n%400 != 0):
    print("Run nian!!!")