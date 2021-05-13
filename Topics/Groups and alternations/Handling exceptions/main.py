import re


# put your regex in the variable template
template = r"([VNT][a-z]+)Error"
string = input()
# compare the string and the template
result = re.match(template, string)
if result:
    print(result.group(1))
else:
    print(result)
