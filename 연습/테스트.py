data = [["날짜1", "지점1", 10, 5, 15],["날짜2", "지점2", 13, 6, 15]]

for row in data:
    if(float(row[2]) > float(-100.0)):
        print("this")
    print(f"this row: {row}")