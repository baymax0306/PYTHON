import urllib
import re

#读取html源码
sock = urllib.urlopen("www.baidu.com");
htmlSource = sock.read();
sock.close();

#匹配，输出结果（[0：3]表示取前3个）
print("open tags:")
print(re.findall(r"<[^/>][^>]*[^/>]>", htmlSource)[0:3])