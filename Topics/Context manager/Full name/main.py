with open('name.txt') as f1, open('surname.txt') as f2, \
        open('full_name.txt', 'w') as f3:
    f3.write(f1.read() + ' ' + f2.read())
