import re

template = r'are you ready??.?.?'
match = re.match(template, input())
print((match.end() - match.start()) if match else 0)
