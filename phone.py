import re
p=re.compile('\d{3}[-|\.|\s]\d{3}[-|\.|\s]\d{4}')
r=p.findall('345-766-9087 and 2346432 357 and 234-456-4567 is an American number')
print(r)

a=re.compile('\w+\d+\w*@gmail\.com')
t=a.findall('email id is thejubnl2002@gmail.com,  thanu234@gmail.com and tanu345')
print(t)
