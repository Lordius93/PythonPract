a = 0
lip = []
while a <= 100:
    print(a)
    a += 1
    lip.append(a)
    continue
    print(lip)
myFile = open("E:\pytest\pytest.txt", "w")
myFile.write(str(lip))