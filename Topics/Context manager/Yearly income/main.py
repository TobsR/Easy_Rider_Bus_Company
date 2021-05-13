# write your code here
with open('salary.txt', encoding='utf-8') as salary_month, \
        open('salary_year.txt', 'w', encoding='utf-8') as salary_year:
    for lines in salary_month:
        salary_year.write(str(int(lines.rstrip()) * 12) + '\n')
