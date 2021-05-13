# read sample.txt and print the number of lines
my_file = open('sample.txt', 'r', encoding='utf-8')
print(len(my_file.readlines()))
my_file.close()
