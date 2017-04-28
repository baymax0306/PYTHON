import re


#匹配一个0－9之外的字符
print(re.search(r"[^0-9]", "A8") != None)
print(re.search(r"^[^0-9]$", "-") != None)
print(re.search(r"^[^0-9]$", "8") != None)

print(re.search(r"^<[^/][^>]*>$", "<b>") != None)
print(re.search(r"^<[^/][^>]+>$", "<tag>") != None)
print(re.search(r"^</[^>]+>$", "</tag>") != None)
print(re.search(r"^<[^/]*/>$", "<b/>") != None)

print(re.search(r"\d{6}", "ab123456cd").group(0))

#13310934_20170426800
print(re.search(r"2017\d{4}", "13310934_20170426800").group(0))

for zipcode in re.findall(r"\d{6}", "zipcode1:201303, zipcode2:100857") :
    print(zipcode)



print("换行符的匹配：")
print(re.search(r"^.$", "\n") != None)
print(re.search(r"(?s)^.$", "\n") != None)
print(re.search(r"^[\s\S]$", "\n") != None)