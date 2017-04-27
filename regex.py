import re


#匹配一个0－9之外的字符
print(re.search(r"[^0-9]", "A8") != None)
print(re.search(r"^[^0-9]$", "-") != None)
print(re.search(r"^[^0-9]$", "8") != None)