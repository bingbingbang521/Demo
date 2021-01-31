n = int(input("input Students Number:"))
data = {}
Subjects = {'Physics', 'Math', 'History'}
for i in range(0, n):
    name = input("Name:")
    marks = []
    for x in Subjects:
        marks.append(int(input("{}:".format(x))))
        data[name] = marks
for x,y in data.items():
    total = sum(y)
    if total < 120:
        print(x, "Failed")
    else:
        print(x, "Pass")

