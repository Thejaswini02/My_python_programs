# Write your code here :-)
import re
s='2002-06-20'
print('the date in format yyyy-mm-dd is :' +s)
t=(re.sub('2002-06-20','20-06-2002',s))
print('the date in format dd-mm-yyyy is :' +t)
