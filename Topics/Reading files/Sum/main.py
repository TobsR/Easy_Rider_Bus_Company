# read sums.txt
my_file = open('sums.txt', 'r', encoding='utf-8')
my_file_length = 0
for lines in my_file:
    x, y = lines.split()
    print(int(x) + int(y))
my_file.close()
